import pygame,sys,random
from pygame.locals import *
pygame.init()
display=pygame.display.set_mode((640,480),0,32)
human_picture=pygame.image.load('player1.png')
fox_picture=pygame.image.load('player2.png')
class road():
    def __init__(self,position):
        self.who_owns='none'
        self.color='none'

road_position=[[0 for i in range(20)] for i in range(20)]
for i in range(1,19):
    road_position[i][1]=1
for i in range(1,14):
    road_position[18][i]=1
for i in range(1,19):
    road_position[i][13]=1
for i in range(1,14):
    road_position[1][i]=1
white=(255,255,255)
class player():
    def __init__(self,picture,id):
        self.picture=picture
        self.position=[1,1]
        self.environment=''
        self.last_move='up'
        self.id=id
    def display_player(self):
        display.blit(self.picture,(32*self.position[0],32*self.position[1]))
    def observation_environment(self):
        environment = []
        if road_position[self.position[0] + 1][self.position[1]] == 1:
            environment.append('right')
        if road_position[self.position[0] - 1][self.position[1]] == 1:
            environment.append('left')
        if road_position[self.position[0]][self.position[1] - 1] == 1:
            environment.append('up')
        if road_position[self.position[0]][self.position[1] + 1] == 1:
            environment.append('down')
        return environment
    def move_once(self):
        if self.last_move=='left':
            opposite_last_move='right'
        elif self.last_move=='right':
            opposite_last_move='left'
        elif self.last_move=='up':
            opposite_last_move='down'
        elif self.last_move=='down':
            opposite_last_move='up'
        not_go_back_environment=self.environment.copy()
        not_go_back_environment.remove(opposite_last_move)
        if not_go_back_environment[0]=='left':
            self.position[0] -= 1
        elif not_go_back_environment[0]=='right':
            self.position[0] +=1
        elif not_go_back_environment[0] == 'down':
            self.position[1]+=1
        elif not_go_back_environment[0] == 'up':
            self.position[1]-=1
        self.last_move=not_go_back_environment[0]
    def move_manyTimes(self,times):
        for i in range(times):
            self.environment = self.observation_environment()
            self.move_once()
    def press_space_and_then_move(self):
        global whose_turn,key_SPACE_have_loosed
        if whose_turn == self.id:
            if key_SPACE_have_loosed==True:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    self.move_manyTimes(random.randint(1, 6))
                    whose_turn += 1
                    if whose_turn==2:
                        whose_turn=0
                key_SPACE_have_loosed=False

def display_road():
    for i in range(20):
        for j in range(15):
            if road_position[i][j]==1:
                pygame.draw.rect(display, (white), (i*32, j*32, 32, 32), 1)
human = player(human_picture,0)
fox=player(fox_picture,1)
key_SPACE_have_loosed=True
whose_turn=0
while True:
    display.fill((173,173,155))
    display_road()
    human.display_player()
    fox.display_player()
    human.press_space_and_then_move()
    fox.press_space_and_then_move()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] ==False:
        key_SPACE_have_loosed =True

    '''
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and space_have_loosed==True:
        human.move_manyTimes(random.randint(1,6))
        space_have_loosed =False
    if keys[pygame.K_SPACE]==False:
        space_have_loosed=True
    '''
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
