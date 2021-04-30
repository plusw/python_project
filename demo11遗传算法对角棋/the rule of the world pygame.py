import pygame,sys,random,time
from pygame.locals import *
pygame.init()
background=pygame.image.load("background.png")
chess_pieces1=pygame.image.load("chess_pieces1.png")
chess_pieces2=pygame.image.load("chess_pieces2.png")
blue=(0,255,0)
display=pygame.display.set_mode((494,401),0,32)
positionDirectionary={
    1: (100,100),
    2: (200,100),
    3: (100,200),
    4: (200,200),
    5: (300,200)
}
a_characterDictionary={
    12: [['down',100]],
    13: [['right',100]],
    14: [['down',50],['right',50]],

    21: [['down',100]],
    23: [['down',50],['left',50]],
    24: [['left',100]],

    31: [['right',100]],
    32: [['up',50],['right',50]],
    34: [['up',100]],

    41: [['up',34],['left',33],['right',33]],
    42: [['left',50],['right',50]],
    43: [['up',50],['right',50]],
}
def random_choice_by_percentage(array):
    probability_list=[0 for i in range(len(array))]
    sum=0
    for i in range(len(array)):
        sum+=array[i][1]
        probability_list[i]=sum
    choice=random.randint(0,99)
    for i in range(len(probability_list)):
        if choice<probability_list[i]:
            final_choice=array[i][0]
            return final_choice
class animal():
    def __init__(self,characterDictionary,position_id):
        self.character=characterDictionary
        self.position_id=position_id
def display_background():
    for i in range(1,6):
        pygame.draw.circle(display, blue, (positionDirectionary[i][0], positionDirectionary[i][1]), 10)
def howToMove(sheep,wolf):
    environment=int(str(sheep.position_id)+str(wolf.position_id))
    move_direction=random_choice_by_percentage(a_characterDictionary[environment])
    if move_direction=='up':
        sheep.position_id-=2
    elif move_direction=='down':
        sheep.position_id+=2
    elif move_direction =='right':
        sheep.position_id +=1
    else:
        sheep.position_id -=1
    print(sheep.position_id)
    return sheep.position_id
def compete(sheep,wolf):
    over=False
    whoFirstMove = random.randint(0, 1)
    if whoFirstMove==0:
        while not over:
            sheep.position_id = howToMove(sheep, wolf)
            if sheep.position_id==5:
                over=True
                who_win='sheep'
            wolf.position_id =howToMove(wolf,sheep)
            if wolf.position_id==5:
                over=True
                who_win='wolf'
        return who_win

a=[0,0]
a[0]=animal(a_characterDictionary,1)
a[1]=animal(a_characterDictionary,2)
lastMoveTime=0
whoseTurn='a[0]'
gameOver=False
while True:
    gameNowTime=time.time()
    display.blit(background ,(0,0))
    display_background()
    if not gameOver:
        if gameNowTime - lastMoveTime > 1 and whoseTurn=='a[0]':
            lastMoveTime =gameNowTime
            howToMove(a[0], a[1])
            whoseTurn = 'a[1]'
            if a[0].position_id ==5:
                gameOver=True

        elif gameNowTime - lastMoveTime > 1 and whoseTurn=='a[1]':
            lastMoveTime = gameNowTime
            howToMove(a[1], a[0])
            whoseTurn = 'a[0]'
            if a[1].position_id ==5:
                gameOver=True
        display.blit(chess_pieces1,(positionDirectionary[a[0].position_id][0],positionDirectionary[a[0].position_id][1]))
        display.blit(chess_pieces2, (positionDirectionary[a[1].position_id][0], positionDirectionary[a[1].position_id][1]))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()