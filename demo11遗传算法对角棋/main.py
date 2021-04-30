import pygame,sys,random,time
from pygame.locals import *
pygame.init()
background=pygame.image.load("background.png")
chess_pieces1=pygame.image.load("chess_pieces1.png")
chess_pieces2=pygame.image.load("chess_pieces2.png")
blue=(0,255,0)
display=pygame.display.set_mode((494,401),0,32)
c=[[0,0,0],[0,0,0],[0,0,0]]
for s in range(3):
    for b in range(3):
        c[s][b] = (100 * s + 100 - 15, 100 * b + 100 - 15)
P1x=[0,0,0]
P1y=[0,0,0]
P2x=[0,0,0]
P2y=[0,0,0]
P1x[0]=0
P1x[1]=0
P1x[2]=0
P1y[0]=0
P1y[1]=1
P1y[2]=2
P2x[0]=2
P2x[1]=2
P2x[2]=2
P2y[0]=0
P2y[1]=1
P2y[2]=2

player1_chess_pieces=[0,0,0]
player2_chess_pieces=[0,0,0]
player1_chess_pieces[0]=c[P1x[0]][P1y[0]]
player1_chess_pieces[1]=c[P1x[1]][P1y[1]]
player1_chess_pieces[2]=c[P1x[2]][P1y[2]]
player2_chess_pieces[0]=c[P2x[0]][P2y[0]]
player2_chess_pieces[1]=c[P2x[1]][P2y[1]]
player2_chess_pieces[2]=c[P2x[2]][P2y[2]]
player1_turn=True
player1_win=False
player2_win=False
gameover=False
def display_checkerboard():
    #global c
    for s in range(3):
        for b in range(3):
            pygame.draw.circle(display,blue,(100*s+100,100*b+100),10)
def display_chess_pieces_player1():
    display.blit(chess_pieces1,player1_chess_pieces[0])
    display.blit(chess_pieces1,player1_chess_pieces[1])
    display.blit(chess_pieces1,player1_chess_pieces[2])
def display_chess_pieces_player2():
    display.blit(chess_pieces2,player2_chess_pieces[0])
    display.blit(chess_pieces2,player2_chess_pieces[1])
    display.blit(chess_pieces2,player2_chess_pieces[2])
def direction_dictionary(n):
    directions = {
        0: (0, -1),
        1: (1, 0),
        2: (0, 1),
        3: (-1, 0),
        4: (1, -1),
        5: (1, 1),
        6: (-1, 1),
        7: (-1, -1)
    }
    return directions.get(n,None)

def move_rule(x,y,direction):
    next_step=direction_dictionary(direction)
    Xnext_step=next_step[0]
    Ynext_step=next_step[1]
    if (x+Xnext_step==P1x[0] and y+Ynext_step== P1y[0]) \
            or(x+Xnext_step==P1x[1] and y+Ynext_step== P1y[1]) \
            or(x+Xnext_step==P1x[2] and y+Ynext_step== P1y[2]) \
            or (x + Xnext_step == P2x[0] and y + Ynext_step == P2y[0]) \
            or (x + Xnext_step == P2x[1] and y + Ynext_step == P2y[1]) \
            or (x + Xnext_step == P2x[2] and y + Ynext_step == P2y[2])\
            or x+Xnext_step>2 or x+Xnext_step<0 or y+Ynext_step>2\
            or y+Ynext_step<0:
        return False
    else:
        return True
def winning_or_losing_rule():
    global player1_win,player2_win
    for a in range(3):
        if player1_chess_pieces[a]==c[1][1]:
            for a in range(3):
                if player1_chess_pieces[a]==c[0][0]:
                    for a in range(3):
                        if player1_chess_pieces[a]==c[2][2]:
                            player1_win=True
                if player1_chess_pieces[a]==c[2][0]:
                    for a in range(3):
                        if player1_chess_pieces[a]==c[0][2]:
                            player1_win=True
        elif player2_chess_pieces[a]==c[1][1]:
            for a in range(3):
                if player2_chess_pieces[a]==c[0][0]:
                    for a in range(3):
                        if player2_chess_pieces[a]==c[2][2]:
                            player2_win=True
                if player2_chess_pieces[a]==c[2][0]:
                    for a in range(3):
                        if player2_chess_pieces[a]==c[0][2]:
                            player2_win=True
def player1_move_chess_pieces():
    global P1x,P1y,player1_turn
    player1_turn=False
    a=random.randint(0,2)
    direction=random.randint(0,7)
    while move_rule(P1x[a], P1y[a], direction)==False:
        a = random.randint(0, 2)
        direction = random.randint(0, 7)
    if direction==0:
        P1y[a]-=1
        player1_chess_pieces[a]=c[P1x[a]][P1y[a]]
    elif direction==1:
        P1x[a]+=1
        player1_chess_pieces[a]=c[P1x[a]][P1y[a]]
    elif direction==2:
        P1y[a]+=1
        player1_chess_pieces[a]=c[P1x[a]][P1y[a]]
    elif direction==3:
        P1x[a]-=1
        player1_chess_pieces[a]=c[P1x[a]][P1y[a]]
    elif direction == 4:
        P1x[a] += 1
        P1y[a] -= 1
        player1_chess_pieces[a] = c[P1x[a]][P1y[a]]
    elif direction == 5:
        P1x[a] += 1
        P1y[a] += 1
        player1_chess_pieces[a] = c[P1x[a]][P1y[a]]
    elif direction==6:
        P1x[a]-=1
        P1y[a]+=1
        player1_chess_pieces[a]=c[P1x[a]][P1y[a]]
    elif direction==7:
        P1x[a]-=1
        P1y[a]-=1
        player1_chess_pieces[a] = c[P1x[a]][P1y[a]]

def player2_move_chess_pieces():
    global P2x, P2y,player1_turn
    player1_turn = True
    a = random.randint(0, 2)
    direction = random.randint(0, 7)
    while move_rule(P2x[a], P2y[a], direction) == False:
        a = random.randint(0, 2)
        direction = random.randint(0, 7)
    if direction == 0:
        P2y[a] -= 1
        player2_chess_pieces[a] = c[P2x[a]][P2y[a]]
    elif direction == 1:
        P2x[a] += 1
        player2_chess_pieces[a] = c[P2x[a]][P2y[a]]
    elif direction == 2:
        P2y[a] += 1
        player2_chess_pieces[a] = c[P2x[a]][P2y[a]]
    elif direction == 3:
        P2x[a] -= 1
        player2_chess_pieces[a] = c[P2x[a]][P2y[a]]
    elif direction == 4:
        P2x[a] += 1
        P2y[a] -= 1
        player2_chess_pieces[a] = c[P2x[a]][P2y[a]]
    elif direction == 5:
        P2x[a] += 1
        P2y[a] += 1
        player2_chess_pieces[a] = c[P2x[a]][P2y[a]]
    elif direction == 6:
        P2x[a] -= 1
        P2y[a] += 1
        player2_chess_pieces[a] = c[P2x[a]][P2y[a]]
    elif direction == 7:
        P2x[a] -= 1
        P2y[a] -= 1
        player2_chess_pieces[a] = c[P2x[a]][P2y[a]]
def Whose_turn():
    winning_or_losing_rule()
    gameOver()
    if gameover==False:
        if player1_turn==True:
            player1_move_chess_pieces()
        else:
            player2_move_chess_pieces()
def gameOver():
    global gameover
    if player1_win==True or player2_win ==True:
        gameover=True
while True:
    display.blit(background, (0, 0))
    display_checkerboard()
    display_chess_pieces_player1()
    display_chess_pieces_player2()
    Whose_turn()
    time.sleep(0.5)

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()