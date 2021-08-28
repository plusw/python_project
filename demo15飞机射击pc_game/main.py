import pygame, sys, random, time
from pygame.locals import *
import math
pygame.init()
#
ufoFireTimeInterval=6
#
ifPlayAgain=False
game_time=0
time.sleep(3)
playAgain=pygame.image.load('playAgain.png')
gameOver=pygame.image.load('gameOver.png')
music_playerFire=pygame.mixer.Sound('laser.wav')
music_explosion=pygame.mixer.Sound('explosion.wav')
icon=pygame.image.load('ufo.png')
#player
CanFire= False
playerX = 500
playerY = 500
LastFireTime=0
playerBulletStartLocationX=[0 for i in range(200)]
playerBulletStartLocationY=[0 for i in range(200)]
playerBulletLocationX=[0 for i in range(200)]
playerBulletLocationY=[0 for i in range(200)]
playerBulletFiredNumber=0
playerBulletThatHitSpaceShip=-1
playerUnvalidBullet=0
player = pygame.image.load('player.png')
hitNumber=-1
playerAlive=True
bullet=pygame.image.load('playerBullet.png')
#animation
lastFlameTime=0
explosionLocationX=[0 for i in range(7)]
explosionLocationY=[0 for i in range(7)]
playExplosionAnimationNumber=0
unvalidAnimationNumber=0
animationFlamePositionArray=[(6,5.5),(6,5.5),(9.5,9),(16.5,15),(23,21.5),(35.5,31),(25,23),(24.5,22),(22.5,20.5),(19.5,20)]
animationNumber=0
animationExplosion0=pygame.image.load('explosion.png')
animationExplosion1=pygame.image.load('explosion.png')
animationExplosion2=pygame.image.load('explosion2.png')
animationExplosion3=pygame.image.load('explosion3.png')
animationExplosion4=pygame.image.load('explosion4.png')
animationExplosion5=pygame.image.load('explosion5.png')
animationExplosion6=pygame.image.load('explosion6.png')
animationExplosion7=pygame.image.load('explosion7.png')
animationExplosion8=pygame.image.load('explosion8.png')
animationExplosion9=pygame.image.load('explosion9.png')
explosionAnimationArray=[animationExplosion0 ,animationExplosion1,animationExplosion2,animationExplosion3,animationExplosion4,animationExplosion5,animationExplosion6,animationExplosion7,animationExplosion8,animationExplosion9]
#UFO
ufoX=[100,200,300,400,500]
ufoY=[100,110,125,136,150]
ufoVx=[3,3,3,3,3]
ufoVy=[-1,-1,-1,-1,-1]
ufoMoveTowarADeirectionTime=3
ufoLastChangeDirectionTime=[0,1,2,3,4]
ufoAlive=[True,True,True,True,True]
ufo=pygame.image.load('ufo.png')
ufoLeft=pygame.image.load('ufoLeft.png')
ufo_bullet=pygame.image.load('ufoBulletYellow.png')
ufoBulletStartLocationX=[[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)]]
ufoBulletStartLocationY=[[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)]]
ufoBulletLocationX=[[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)]]
ufoBulletLocationY=[[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)]]
ufoBulletFiredNumber=[0,0,0,0,0]
ufoUnvalidBullet=[0,0,0,0,0]
ufoCanFire=[False,False,False,False,True]
ufoBulletLocus=[[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)]]
ufoBulletThatHitPlayerNumber=(-1,-1)
ufoLastFireTime=[0,2,4,6,9]
#SPACESHIP
spaceShipBulletThatHitPlayer=(-1,-1)
spaceShip=pygame.image.load('spaceShip.png')
spaceShipBullet=pygame.image.load('ufoBullet.png')
angle=0
spaceShipRect = spaceShip.get_rect()
spaceShipX=54
spaceShipY=54
spaceShipVx=1
spaceShipVy=1
spaceShipBulletLocationX=[[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)]]
spaceShipBulletLocationY=[[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)],[0 for i in range(100)]]
spaceShipBulletStartLocationArray=[(54,0),(0,54),(-54,0),(0,-54)]
spaceShipFireNumber=0
spaceShipLastFireTime=0
spaceShipCanFire=False
spaceShipUnValidBullet=0
spaceShipAlive=True
#
pygame.display.set_caption('The war in space')
pygame.display.set_icon(icon)
display = pygame.display.set_mode((1200, 600), 0, 32)
fpsClock = pygame.time.Clock()
FPS = 30
def player_move():
    if playerAlive ==True:
        global playerX,playerY
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerX -= 5
        elif keys[pygame.K_RIGHT]:
            playerX += 5
        if keys[pygame.K_UP]:
            playerY-=4
        elif keys[pygame.K_DOWN]:
            playerY+=4
        if playerX<0:
            playerX=0
        elif playerX+64>1200:
            playerX=1200-64
        if playerY+64>600:
            playerY=600-64
        elif playerY<0:
            playerY=0
        display.blit(player,(playerX,playerY))
def player_fire(playerX,playerY):
    if playerAlive ==True:
        global game_time,LastFireTime,playerBulletLocationX,playerBulletStartLocationY,playerBulletStartLocationX,playerBulletStartLocationY,playerBulletFiredNumber
        if game_time - LastFireTime > 2:
            playerCanFire = True
        else:
            playerCanFire=False
        if playerCanFire==True:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                LastFireTime=game_time
                music_playerFire.play()
                playerBulletStartLocationX[playerBulletFiredNumber] = playerX + 23
                playerBulletStartLocationY[playerBulletFiredNumber]=playerY
                playerBulletLocationX[playerBulletFiredNumber] = playerBulletStartLocationX
                playerBulletLocationY[playerBulletFiredNumber] = playerBulletStartLocationY
                playerBulletFiredNumber += 1
def playerBulletBeFired():
    global playerBulletLocationX,playerBulletLocationY,playerUnvalidBullet
    for i in range(playerUnvalidBullet,playerBulletFiredNumber):
        playerBulletLocationY[0][i]= playerBulletLocationY[0][i] - 8
        if hitNumber!=i and playerBulletThatHitSpaceShip!=i:
            display.blit(bullet, (playerBulletLocationX[0][i], playerBulletLocationY[0][i]))
    if playerBulletFiredNumber>0 and playerUnvalidBullet<=playerBulletFiredNumber:
        if playerBulletLocationY[0][playerUnvalidBullet]+32<0:
            playerUnvalidBullet+=1
def display_space_Ship():
    if spaceShipAlive:
        global angle
        rotateSpaceShip = pygame.transform.rotate(spaceShip, angle)
        angle=angle+speed/1.732*3
        newRect = rotateSpaceShip.get_rect(center=spaceShipRect.center)
        display.blit(rotateSpaceShip, newRect)
def spaceShip_move():
    if spaceShipAlive:
        global spaceShipRect,spaceShipX,spaceShipY,spaceShipVx,spaceShipVy,speed
        spaceShipRect.centerx=spaceShipX
        spaceShipRect .centery =spaceShipY
        spaceShipX+=spaceShipVx
        spaceShipY+=spaceShipVy
        speed=math.sqrt(math.pow(spaceShipVx, 2) + (math.pow(spaceShipVy, 2)))
        if spaceShipX>1200-108:
            spaceShipVx=-1
        elif spaceShipX<0:
            spaceShipVx=1
        if spaceShipY<0:
            spaceShipVy=1
        elif spaceShipY>600-108:
            spaceShipVy=-1
def spaceShipFire():
    global spaceShipUnValidBullet
    if spaceShipAlive and playerAlive :
        global spaceShipCanFire,spaceShipFireNumber,spaceShipLastFireTime
        if spaceShipCanFire:
            #fire
            spaceShipLastFireTime=game_time
            for i in range(20):
                spaceShipBulletLocationX[i][spaceShipFireNumber]=spaceShipX#+spaceShipBulletStartLocationArray[i][0]
                spaceShipBulletLocationY[i][spaceShipFireNumber]=spaceShipY#+spaceShipBulletStartLocationArray[i][1]
            spaceShipFireNumber += 1
            if spaceShipFireNumber==100:
                spaceShipFireNumber -= 1
            if spaceShipUnValidBullet==99:
                spaceShipFireNumber =0
                spaceShipUnValidBullet=0
            spaceShipCanFire = False
        if game_time -spaceShipLastFireTime>9:
            spaceShipCanFire=True
def spaceShipBulletBeFired():
    global spaceShipUnValidBullet
    for j in range(spaceShipUnValidBullet,spaceShipFireNumber):
        for i in range(20):
            if spaceShipBulletThatHitPlayer!=(j,i):
                spaceShipBulletLocationX[i][j]+=math.sin(i*3.14159/10)*5
                spaceShipBulletLocationY[i][j]+=math.cos(i*3.15159/10)*5
                display.blit(spaceShipBullet,(spaceShipBulletLocationX[i][j],spaceShipBulletLocationY[i][j]))
            if spaceShipBulletLocationX[i][j]>2400:
                spaceShipUnValidBullet+=1
def ufo_move():
    global ufoMoveTowarADeirectionTime
    for i in range(5):
        if ufoAlive[i] ==True:
            global ufoX,ufoVx,ufoY,ufoVy
            if playerX<ufoX[i]:
                display.blit(ufoLeft,(ufoX[i],ufoY[i]))
            else:
                display.blit(ufo,(ufoX[i],ufoY[i]))
            ufoX[i] += ufoVx[i]
            ufoY[i] += ufoVy[i]
            if game_time-ufoLastChangeDirectionTime[i]>ufoMoveTowarADeirectionTime:
                #Can Change Direction
                ufoMoveTowarADeirectionTime=random.randint(1,4)
                ufoLastChangeDirectionTime[i]=game_time
                if ufoX[i]>playerX and ufoX[i]<playerX+400:
                    ufoVx[i] = random.randint(-10, 40) * 0.1
                    ufoVy[i] = random.randint(-20, 20) * 0.1
                elif ufoX[i]<playerX and ufoX[i]>playerX-400:
                    ufoVx[i] = random.randint(-30, 10) * 0.1
                    ufoVy[i] = random.randint(-20, 20) * 0.1
            if ufoX[i] + 32 > 1200:
                ufoLastChangeDirectionTime[i] =game_time
                ufoVx[i]=random.randint(-30,-1)*0.1
            elif ufoX[i] < 0:
                ufoLastChangeDirectionTime[i] = game_time
                ufoVx[i]=random.randint(1,30)*0.1
            if ufoY[i]<0:
                ufoLastChangeDirectionTime[i] = game_time
                ufoVy[i] = random.randint(1, 20) * 0.1
            elif ufoY[i]>300:
                ufoLastChangeDirectionTime[i] = game_time
                ufoVy[i] = random.randint(-20, -1) * 0.1
def ufoFire():
    global ufoFireTimeInterval
    if playerAlive:
        for i in range(5):
            if ufoAlive[i] :
                global ufoX,ufoY,ufoLastFireTime,ufoCanFire,ufoBulletFiredNumber
                if ufoCanFire[i]:
                    #fire
                    ufoBulletLocus[i][ufoBulletFiredNumber[i]]=(0.01*((playerX+32)-(ufoX[i]+40.1)),0.01*((playerY+32)-(ufoY[i]+21)))
                    ufoCanFire[i] =False
                    ufoLastFireTime[i]=game_time
                    ufoBulletStartLocationX[i][ufoBulletFiredNumber[i]]=ufoX[i]+30.5
                    ufoBulletStartLocationY[i][ufoBulletFiredNumber[i]]=ufoY[i]+30
                    ufoBulletLocationX[i][ufoBulletFiredNumber[i]]=ufoBulletStartLocationX[i][ufoBulletFiredNumber[i]]
                    ufoBulletLocationY[i][ufoBulletFiredNumber[i]] = ufoBulletStartLocationY[i][ufoBulletFiredNumber[i]]
                    ufoBulletFiredNumber[i] += 1
                    if ufoBulletFiredNumber[i]==100:
                        ufoBulletFiredNumber[i]-=1
                    if ufoUnvalidBullet[i]==99:
                        ufoBulletFiredNumber[i] =0
                        ufoUnvalidBullet[i]=0
                if  game_time-ufoLastFireTime[i]>ufoFireTimeInterval:
                    ufoCanFire[i] =True
def ufoBulletBeFired():
    for j in range(5):
        global ufoUnvalidBullet,ufoBulletThatHitPlayerNumber
        for i in range(ufoUnvalidBullet[j],ufoBulletFiredNumber[j]):
            if ufoBulletThatHitPlayerNumber!=(j,i):
                ufoBulletLocationX[j][i]+=ufoBulletLocus[j][i][0]
                ufoBulletLocationY[j][i]+=ufoBulletLocus[j][i][1]
                display.blit(ufo_bullet,(ufoBulletLocationX[j][i],ufoBulletLocationY[j][i]))
            if ufoBulletLocationY[j][i] >900 or ufoBulletLocationX[j][i] <-500 or ufoBulletLocationX[j][i] >1800:
                ufoUnvalidBullet[j]+=1
def isCollision_ufoBullet_and_player( ufoBulletLocationX,ufoBulletLocationY,playerX,playerY):
    distance = math.sqrt(math.pow(ufoBulletLocationX+ 10 - (playerX + 32), 2) + (math.pow(ufoBulletLocationY + 10 - (playerY + 32), 2)))
    if distance < 31:
        return True
def isCollision_playerBullet_and_ufo(playerBulletLocationX, playerBulletLocationY, ufoX,ufoY):
    distance = math.sqrt(math.pow(ufoX + 40.5 - (playerBulletLocationX + 10), 2) + (math.pow(ufoY + 21 - (playerBulletLocationY + 10), 2)))
    if distance < 31:
        return True
def isCollision_spaceShipBullet_and_player(spaceShipBulletLocationX,spaceShipBulletLocationY,playerX,playerY) :
    distance = math.sqrt(math.pow(spaceShipBulletLocationX + 9 - (playerX + 32), 2) + (math.pow(spaceShipBulletLocationY + 9 - (playerY + 32), 2)))
    if distance < 30:
        return True
def isCollision_spaceShip_and_playerBullet(spaceShipLocationX,spaceShipLocationY,playerBulletX,playerBulletY) :
    distance = math.sqrt(math.pow(spaceShipLocationX - (playerBulletX + 10), 2) + (math.pow(spaceShipLocationY - (playerBulletY + 10), 2)))
    if distance < 50:
        return True
def explosionAnimation(locationX,locationY):
    global animationNumber,lastFlameTime,unvalidAnimationNumber
    display.blit(explosionAnimationArray[animationNumber], (locationX-animationFlamePositionArray[animationNumber][0], locationY-animationFlamePositionArray[animationNumber][1]))
    if game_time -lastFlameTime >0.2:
        lastFlameTime = game_time
        animationNumber +=1
    if animationNumber ==10:
        animationNumber =0
        unvalidAnimationNumber+=1
while True:
    game_time+=0.1
    display.fill((0, 0, 0))
    if playerAlive == False or (ufoAlive == [False, False, False, False, False] and spaceShipAlive == False):
        display.blit(gameOver, (100, 100))
        if ifPlayAgain==False:
            display.blit(playAgain, (1000, 400))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            ifPlayAgain =True
            playExplosionAnimationNumber = 0
            unvalidAnimationNumber = 0
            playerAlive = True
            ufoAlive = [True, True, True, True, True]
            spaceShipAlive = True
    ufoBulletBeFired()
    playerBulletBeFired()
    spaceShipBulletBeFired()
    player_move()
    player_fire(playerX, playerY)
    ufoFire()
    ufo_move()
    spaceShip_move()
    spaceShipFire()
    display_space_Ship()
    if playerAlive==True:
        for j in range(5):
            if playerAlive==False:
                break
            for i in range(ufoUnvalidBullet[j], ufoBulletFiredNumber[j]):
                if ufoBulletThatHitPlayerNumber!=(j,i):
                    if isCollision_ufoBullet_and_player( ufoBulletLocationX[j][i],ufoBulletLocationY[j][i],playerX, playerY):
                        music_explosion.play()
                        ufoBulletThatHitPlayerNumber = (j,i)
                        explosionLocationX[playExplosionAnimationNumber]=playerX+32
                        explosionLocationY[playExplosionAnimationNumber]=playerY+32
                        playExplosionAnimationNumber+=1
                        playerAlive = False
                        break
        for j in range(spaceShipUnValidBullet, spaceShipFireNumber):
            if playerAlive==False:
                break
            for i in range(20):
                if spaceShipBulletThatHitPlayer!=(j,i):
                    if isCollision_spaceShipBullet_and_player(spaceShipBulletLocationX[i][j],spaceShipBulletLocationY[i][j],playerX,playerY ) :
                        music_explosion.play()
                        explosionLocationX[playExplosionAnimationNumber] = playerX + 32
                        explosionLocationY[playExplosionAnimationNumber] = playerY + 32
                        playExplosionAnimationNumber += 1
                        playerAlive = False
                        spaceShipBulletThatHitPlayer=(j,i)
                        break
    if spaceShipAlive:
        for i in range(playerUnvalidBullet,playerBulletFiredNumber):
            if playerBulletThatHitSpaceShip!=i:
                if isCollision_spaceShip_and_playerBullet(spaceShipX,spaceShipY,playerBulletLocationX[0][i],playerBulletLocationY[0][i]):
                    music_explosion.play()
                    explosionLocationX[playExplosionAnimationNumber] = spaceShipX
                    explosionLocationY[playExplosionAnimationNumber]=  spaceShipY
                    playExplosionAnimationNumber += 1
                    spaceShipAlive = False
                    playerBulletThatHitSpaceShip = i
                    break
    for i in range(5):
        if ufoAlive[i] ==True:
            for j in range(playerUnvalidBullet,playerBulletFiredNumber):
                if hitNumber!=j:
                    if isCollision_playerBullet_and_ufo(playerBulletLocationX[0][j], playerBulletLocationY[0][j], ufoX[i], ufoY[i]):
                        music_explosion.play()
                        explosionLocationX[playExplosionAnimationNumber] = ufoX[i]+39.5
                        explosionLocationY[playExplosionAnimationNumber] = ufoY[i]+21
                        playExplosionAnimationNumber+=1
                        hitNumber =j
                        ufoAlive[i] = False
                        break
    for i in range(unvalidAnimationNumber,playExplosionAnimationNumber):
        explosionAnimation(explosionLocationX[i],explosionLocationY[i])
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)





