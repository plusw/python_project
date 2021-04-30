import pygame, sys,time
from pygame.locals import *
pygame.init()
startGame=False
icon=pygame.image.load('icon.jpg')
pygame.display.set_icon(icon)
pygame.display.set_caption('Pennant Puzzle')
picture = pygame.image.load('london.jpg')
picture =pygame .transform .scale(picture ,(960,540))
fpsClock = pygame.time.Clock()
FPS = 30
WINDOWWIDTH = 420
WINDOWHEIGHT = 520
display = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.mouse.set_visible(True)
white=(255,255,255)
red1=(254,67,101)
red2=(252,157,154)
yellow1=(249,205,173)
yellow2=(200,200,169)
green1=(131,175,155)
green2=(64,116,52)
green4=(174,221,129)
green5=(104,194,53)
green6=(6,128,67)
green7=(38,157,128)
red=(255,0,0)
blue=(0,0,255)
black=(0,0,0)
white1=(255,100,100)
white3=(220,200,220)
pink=(255,0,255)
green=(0,255,0)
green3=(101,147,74)
brown=(159,125,80)
yellow=(255,255,0)
blue1=(38,188,213)
white2=(179,168,150)
gray=(128,128,128)
rectExist=True
#font = pygame.font.SysFont("my_font.ttf", 32)
font=pygame.font.SysFont('arial',23)
#font = pygame.font.SysFont(None, 32)
rectNumber=16
rect=[0 for i in range(rectNumber)]
moveSpeed=5
array=[]
smallRectPosition=[[0,400],     [100,300],  [200,300],  (300,400)]
smallRectSize=    [(100,100),   (100,100),  (100,100),  (100,100)]
smallRectColor=   [green ,      green1 ,    green2 ,    green3 ]
middleRectSize=    [(100,200),  (100,200),  (100,200),  (100,200),  (200,100)]
middleRectPosition=[(0,0),      (300,0),    (0,200),    (300,200),  (100,200)]
middleRectColor=   [green6  ,   yellow2 ,   red1 ,      red2 ,      yellow ]
bigRectPosition=[(100,0)]
bigRectSize=    [(200,200)]
bigRectColor=   [white3]
borderRectPosition=[(0,-10),    (400,-10)  ,(-10,-10), (0,500),    (300,500),  (100,500)]
borderRectSize=    [(400,10),   (10,520),   (10,520),   (100,10),   (100,10),   (200,10)]
borderRectColor=   [brown ,     brown ,     brown ,     brown ,     brown,      brown]
rectColor=middleRectColor +smallRectColor +bigRectColor+borderRectColor
everyRectPosition=middleRectPosition+smallRectPosition +bigRectPosition+borderRectPosition
rectSize=middleRectSize +smallRectSize +bigRectSize+borderRectSize
for i in range(16):
    array+=[list(everyRectPosition[i])]
everyRectPosition=array
for i in range (rectNumber):
    for j in range(2):
        if j==0:
            everyRectPosition[i][j] +=10
        else:
            everyRectPosition[i][j]+=10

class rect_class():
    def __init__(self,size,color,position):
        self.width = size[0]
        self.length = size[1]
        self.positionX = position[0]
        self.positionY = position[1]
        self.shape_body = ((self.positionX, self.positionY), (self.width, self.length))
        self.rect = pygame.Rect(self.shape_body)
        super(rect_class, self).__init__()
        self.surf = pygame.Surface((self.width, self.length))
        self.surf.fill(color)
    def draw(self):
        display.blit(self.surf ,self.rect)
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            self.rect.move_ip(0, -moveSpeed)
            for i in range(rectNumber):
                if rectDirectionay[i] != self:
                    if self.rect.colliderect(rectDirectionay[i].rect):
                        self.rect.move_ip(0, moveSpeed)
        if keys[K_s]:
            self.rect.move_ip(0, moveSpeed )
            for i in range(rectNumber):
                if rectDirectionay[i] != self:
                    if self.rect.colliderect(rectDirectionay[i].rect):
                        self.rect.move_ip(0, -moveSpeed)
        if keys[K_a]:
            self.rect.move_ip(-moveSpeed , 0)
            for i in range(rectNumber):
                if rectDirectionay[i] != self:
                    if self.rect.colliderect(rectDirectionay[i].rect):
                        self.rect.move_ip(moveSpeed , 0)


        if keys[K_d]:
            self.rect.move_ip(moveSpeed , 0)
            for i in range(rectNumber):
                if rectDirectionay[i] !=self :
                    if self.rect.colliderect(rectDirectionay[i].rect):
                        self.rect.move_ip(-moveSpeed , 0)

def isRectClicked(event):
    global select
    for i in range(0,rectNumber-5):
        if i!=10:
            if rectDirectionay[i].rect.collidepoint(event.pos):
                select =rectDirectionay[i]

def openTheDoor():
    global rectNumber,rectExist,gameOverTime,isGameOver,gameLastTime
    if rect[9].rect.left==110 and rect[9].rect.top==310 and rectExist==True:
        del rect[15]
        isGameOver =True
        rectExist=False
        rectNumber-=1
        gameOverTime=time.time()
        gameLastTime=gameOverTime - gameStartTime
def whenGameOver():
    if isGameOver:
        drawText('time:'+str(format(gameLastTime,'.1f')+' s'),font,display,20,20,white)
def drawText(text, font, surface, x, y,color):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
gameStartTime=time.time()
gameLastTime=0
isGameOver=False
for i in range(rectNumber):
    rect[i]=rect_class(rectSize[i],rectColor[i],everyRectPosition[i])
rectDirectionay=rect
select=rect[5]
while True:
    if startGame:
        display.blit(picture,(-270,10))
        for i in range(rectNumber):
            if i!=15:
                rect[i].draw()
        select.move()
        openTheDoor()
        whenGameOver()
    else:
        #display.blit()
        drawText('Pennant Puzzle', font, display, 135, 0,white)
        drawText('It is a slider game. ',font,display,5,30,white )
        drawText('10 pieces placed on a square board. ', font, display, 5, 80, white)
        drawText('The goal is to move the largest piece to',font,display,5,130,white )
        drawText('the buttom', font, display, 5, 180, white )
        drawText('Use mouse and "w, a, s, d" to move', font, display, 5, 230, white)
        drawText('Press any key to continue', font, display, 90, 400, white)
    for event in pygame.event.get():
        if event.type==KEYDOWN and startGame==False:
            startGame=True
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event .type ==MOUSEBUTTONDOWN :
            if event.button==1:
                isRectClicked(event)

    pygame.display.update()
    fpsClock.tick(FPS)
