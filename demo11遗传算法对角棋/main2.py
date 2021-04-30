import pygame,sys,random,time
from pygame.locals import *
pygame.init()
background=pygame.image.load("background.png")
chess_pieces1=pygame.image.load("chess_pieces1.png")
chess_pieces2=pygame.image.load("chess_pieces2.png")
display=pygame.display.set_mode((494,420),0,32)
moveDistance=100
blue=(0,0,255)
green=(0,255,0)
dictionary=\
{
    # ('right' 'down' 'left' 'up')
    1:('right', 'down', 0,      0,      (100,100)),
    2:('right', 'down','left',  0,      (200,100)),
    3:(0,       'down','left',  0,      (300,100)),
    4:('right', 'down', 0,      'up',   (100,200)),
    5:('right', 'down','left',  1,      (200,200)),
    6:(0,       'down','left',  'up',   (300,200)),
    7:('right', 0,      0,      'up',   (100,300)),
    8:('right', 'down', 'left', 'up',   (200,300)),
    9:(0,       0,      'left', 'up',   (300,300)),
    11:(0,      0,      0,      'up',   (200,400))
}
class player():
    def __init__(self,positionId,picture):
        self.positionId=positionId
        self.picture=picture
    def move(self):
        global gameOver
        lastPositionId = self.positionId
        a=''
        haveSpaceToMove=False
        while not haveSpaceToMove:
            a=random.choice(dictionary[self.positionId])
            for i in range(2):
                if self !=playerArray[i]:
                    if (a=='right' and self.positionId+1!=playerArray[i].positionId) or (a=='left' and self.positionId-1!=playerArray[i].positionId) or (a=='down' and self.positionId+3!=playerArray[i].positionId) or (a=='up' and self.positionId-3!=playerArray[i].positionId):
                        haveSpaceToMove=True
        if a=='right':
            self.positionId +=1
        elif a=='left':
            self.positionId -= 1
        elif a=='up':
            self.positionId -= 3
        elif a=='down':
            self.positionId += 3
        print(self.positionId)
        moveLogFile = open("moveLog.txt", 'a')
        if self==playerHuman:
            #moveLogFile.write(str(lastPositionId)+'-->'+str(self.positionId)+'  ')
            moveLogFile.write(str(lastPositionId)+' '+str(self.positionId)+ '      ')
        else:
            #moveLogFile.write(str(lastPositionId)+'-->'+str(self.positionId)+'      ')
            moveLogFile.write(str(lastPositionId)+' '+str(self.positionId)+'      ')
        moveLogFile.close()

        if self.positionId==11:
            moveLogFile = open("moveLog.txt", 'a')
            moveLogFile.write('\n')
            moveLogFile.close()
            gameOver=True

    def draw(self):
        display.blit(self.picture,(dictionary[self .positionId][4][0]-16,dictionary[self .positionId][4][1]-16))

def display_checkerboard():
    pygame.draw.line(display, (0, 0, 0), (100, 200), (300, 200), 1)
    pygame.draw.line(display, (0, 0, 0), (200, 100), (200, 400), 1)
    pygame.draw.rect(display, (0, 0, 0), (100, 100, 200, 200), 1)
    for i in range(1,12):
        if i!=10:
            pygame.draw.circle(display,blue,(dictionary[i][4][0],dictionary[i][4][1]),10)
def findTheBestMove():
    file=open('moveLog.txt','r')
    for i in file:
        print(i)
def howToMove():
    s=1

playerHuman=player(1,chess_pieces1)
playerFox=player(3,chess_pieces2)
playerArray=(playerHuman,playerFox)
gameStartTime=time.time()
lastMoveTime=0
successfulTime=0
whoseTurn='playerHuman'
gameOver=0
analysis_data=0
if analysis_data == True:
        file = open("moveLog.txt", 'r')
        probabilityLogfile = open("probabilityLog.txt", 'w')
        for line in file:
            a = line.split()
            for i in range(len(a)):
                a[i] = int(a[i])
            for i in range(len(a)):
                if i % 2 == 0 and i+3<len(a):
                    probabilityLogfile.write(str(a[i]) + str(a[i + 1]) + str(a[i + 2]) + str(a[i + 3]) + '\n')
        probabilityLogfile.close()
        file.close()

while True:

    if gameOver==False:
        gameNowTime=time.time()
        #display.blit(background ,(0,0))
        display.fill((100,177,255))
        display_checkerboard()
        playerHuman.draw()
        playerFox.draw()
        if gameNowTime - lastMoveTime > 1 and whoseTurn=='playerHuman':
            playerHuman .move()
            lastMoveTime=gameNowTime
            whoseTurn = 'playerFox'
        if  gameNowTime - lastMoveTime > 1 and whoseTurn=='playerFox':
            playerFox .move()
            lastMoveTime=gameNowTime
            whoseTurn = 'playerHuman'

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()