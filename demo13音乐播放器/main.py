import pygame,sys,os
from pygame.locals import *
pygame.init()
width=600
height=600
icon=pygame.image.load('icon4.png')
picture1=pygame.image.load('icon3.png')
display=pygame.display.set_mode((width,height))
pygame.display.set_caption('Music')
pygame.display.set_icon(icon)
green=(0,255,0)
black=(0,0,0)
yellow=(255,255,0)
white=(255,255,255)
white_less1=(150,150,150)
blue1=(38,188,213)
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
blue=(0,0,200)
brown=(159,125,80)
class music():
    def __init__(self,name,Id):
        self.name=name
        self.name_color=black
        self.id=Id
        self.position=[0,Id*40]
        self.shape_body = ((self.position[0], self.position[1]), (width-255, 40))
        self.rect = pygame.Rect(self.shape_body)
playList=[0 for i in range(1000)]
biggest_id=0
path = os.getcwd()
file = os.listdir(path)
for a in file:
    if a.endswith('.mp3') or a.endswith('.wav'):
        playList[biggest_id]=music(a,biggest_id)
        biggest_id+=1
will_play_list=[]
will_play_witch_position=[width-255,height-255]
will_play_witch_shape_body=((will_play_witch_position[0],will_play_witch_position[1]), (255, 255))
will_play_witch_rect=pygame.Rect(will_play_witch_shape_body)
mode='normal'
haveSongsWillPlay=False
j=0
witchIsPlaying='none'
def move_up_or_down():
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        for i in range(biggest_id):
            playList[i].position[1]-=4
    elif keys[pygame.K_DOWN]:
        for i in range(biggest_id):
            playList[i].position[1]+=4
def drawText(text,position,color):
    font = pygame.font.SysFont('arial', 23)
    text=font.render(text,True,color)
    rect=text.get_rect()
    rect.left=position[0]
    rect.top=position[1]
    display.blit(text,rect)
def isRectClicked(event):
    global mode,haveSongsWillPlay,will_play_list,witchIsPlaying
    n=0
    if will_play_witch_rect.collidepoint(event.pos) and mode=='normal' and n==0:
        mode='decide_what_will_play'
        n+=1
    if will_play_witch_rect.collidepoint(event.pos) and mode == 'decide_what_will_play' and n==0:
        mode='normal'
        haveSongsWillPlay=True
        n+=1
    if mode=='decide_what_will_play':
        for i in range(0,biggest_id):
            if playList[i].rect.collidepoint(event.pos):
                select =playList[i]
                if select not in will_play_list :
                    will_play_list.append(select)
                    break
                else:
                    will_play_list.remove(select)
                    break


    if mode=='normal':

        for i in range(0,biggest_id):
            if playList[i].rect.collidepoint(event.pos):
                select =playList[i]
                witchIsPlaying=select
                if select.name.endswith('.mp3'):
                    music=pygame.mixer.music.load(select.name)
                    pygame.mixer.music.play()
                elif select.name.endswith('.wav'):
                    sound = pygame.mixer.Sound(select.name)
                    sound.play()
while True:
    display.fill(white)
    display.blit(picture1,(width-225,height-225))
    move_up_or_down()
    if mode=='decide_what_will_play':
        for i in range(biggest_id):
            if playList[i] in will_play_list:
                playList[i].name_color = (0,160,160)
            else:
                playList[i].name_color = brown
        for i in range(biggest_id):
            drawText(str(i)+'  '+playList[i].name,playList[i].position,playList[i].name_color)
    if mode=='normal':
        for i in range(0, biggest_id):
            playList[i].name_color = black
        if witchIsPlaying!='none':
            witchIsPlaying.name_color=blue1
        for i in range(biggest_id):
            drawText(str(i)+'  '+playList[i].name,playList[i].position,playList[i].name_color)
    if pygame.mixer.music.get_busy() == False and haveSongsWillPlay == True:
        music = pygame.mixer.music.load(will_play_list[j].name)
        pygame.mixer.music.play()
        witchIsPlaying = will_play_list[j]
        j += 1
        will_play_list[j-1]='havePlayed'
        if j == len(will_play_list):
            j = 0
            haveSongsWillPlay = False
            will_play_list = []
    elif pygame.mixer.music.get_busy() == False and haveSongsWillPlay == False:
        witchIsPlaying='none'

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event .type ==MOUSEBUTTONDOWN :
            if event.button==1:
                isRectClicked(event)
    pygame.display.update()