'''
Moataz Khallaf A.K.A Hackerman
BrickBreaker
4/26/2019
'''
from myClass import *
import pygame, random
pygame.init()  # Loads PyGame Module commands in the program

# Display Variables

TITLE = "Single player pong"  # Appears in window title
FPS = 30
WIDTH = 800
HEIGHT = 600
SCREENDIM = (WIDTH, HEIGHT)

# Colour variables

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 255)
BLUE = (0, 0, 255)
PINK = (255, 53, 127)

# Create the window

screen = pygame.display.set_mode(SCREENDIM)  # creates the main surface where all assets are placed
pygame.display.set_caption(TITLE)  # updates the windows title
screen.fill(GREY)  # fills the entire surface with the colour ie. erase

clock = pygame.time.Clock()  # starts a clock object to measure time

#           <Variables and objects>

running = True  # for the general program to run
startTrigger = False  # for the game to start
life = 3  # life system because 3rd try = best try
nextLvlTrigger = 0
scoreNum = 0

#       <Sprites>
#           <title>

title = text("BorkBroker")
title.setPos(WIDTH/2 - title.getText().get_width()/2, 4)

#           <Bar>

bar = box(0, 0, WIDTH, 40, 0, 0)
bar.setColor(BLACK)

#           <Score>

score = text('score'+str(scoreNum))
score.setColor(WHITE)

#           <Player>

player = box((WIDTH/2 - 50), (HEIGHT - 25), 200, 15, 15, 0)  # x, y, width, height, xspeed, yspeed
player.setColor(GREEN)  # width is buffed because honestly this isn't about the gameplay

#           <Ball>

ball = box((WIDTH/2), (HEIGHT - 45), 15, 15, 5, 4)
ball.setColor(BLUE)

#           <Lives>

lives = text('Lives ' + str(life))
lives.setPos(730, 0)
lives.setColor(WHITE)

#           <EndScreen>

endScreen = text("You are done, now please give A++... reminder ESC to exit")
endScreen.setPos(999, 999)

#           <StartMenu>

start = text("SPACE to start, ESC to exit")
start.setPos(WIDTH/2 - start.getText().get_width()/2, HEIGHT/2 - start.getText().get_height()/2)

#           <BlockSpawns>

blockArrRow1 = []  # 4 rows each have 9 bricks
for i in range(8):
    blockArrRow1.append(box(i*100 + 6, 70, 90, 40, 3, 3))
    blockArrRow1[i].setColor(PINK)

blockArrRow2 = []
for i in range(8):
    blockArrRow2.append(box(i*100 + 6, 130, 90, 40, 3, 3))
    blockArrRow2[i].setColor(PINK)

blockArrRow3 = []
for i in range(8):
    blockArrRow3.append(box(i*100 + 6, 190, 90, 40, 3, 3))
    blockArrRow3[i].setColor(PINK)

blockArrRow4 = []
for i in range(8):
    blockArrRow4.append(box(i*100 + 6, 250, 90, 40, 3, 3))
    blockArrRow4[i].setColor(PINK)

blockArrRow5 = []
for i in range(8):
    blockArrRow5.append(box(999 + 6, 999, 90, 40, 3, 3))
    blockArrRow5[i].setColor(PINK)


blockArr = [blockArrRow1, blockArrRow2, blockArrRow3, blockArrRow4, blockArrRow5]

#           <Actual Code starts here>

while running:
    for event in pygame.event.get():  # returns all inputs and triggers into an array
        if event.type == pygame.QUIT:  # if red x was clicked
            running = False

#                 <MISC>

    pressedKeys = pygame.key.get_pressed()
    color = (random.randrange(0,255), random.randrange(0, 255), random.randrange(0, 255))
    start.setColor(color)
    title.setColor(color)

#                  <DIFF>

    if ball.getXSPD() < 30:
        ball.setXSPD(increaseDiff(ball.getXSPD()))  # Spd increased by *0.0007 every frame???
        ball.setYSPD(increaseDiff(ball.getYSPD()))

#              <Triggers>

    if pressedKeys[pygame.K_ESCAPE]:  # to exit
        quit()

    if pressedKeys[pygame.K_SPACE]:
            startTrigger = True  # to start

    player.playerMove(pressedKeys)

    if startTrigger:
        ball.autoMove()

    if nextLvlTrigger == 32:
        for i in range(len(blockArrRow5)):
            blockArrRow5[i].setPos(i*100 + 6, (50+i) *70)

        nextLvlTrigger += 1


    if nextLvlTrigger == 41:
        endScreen.setColor(color)
        endScreen.setPos(WIDTH/2 - endScreen.getText().get_width()/2, HEIGHT/2 - endScreen.getText().get_height()/2)

    if ball.getY() > HEIGHT:
        startTrigger = False  # loosing system
        start.setPos(WIDTH/2 - start.getText().get_width()/2, HEIGHT/2 - start.getText().get_width()/2)
        ball.setPos(WIDTH/2 - ball.getSurface().get_width()/2, HEIGHT/2 - ball.getSurface().get_width()/2)
        life -= 1
        lives.setColor(color)
        if life == 0:
            print("Error 404: Restart system missing XD")
            running = False

        lives.setText("lives " + str(life))

#           <Collisions>

    for i in range(len(blockArr)):
        for j in range(8):

            if getSpriteColision(blockArr[i][j], ball):
                ball.Ybounce()
                blockArr[i][j].setPos(999, 999)
                nextLvlTrigger += 1
                scoreNum += 10
                score.setColor(color)

    score.setText('score ' + str(scoreNum))

    if getSpriteColision(player, ball):
        ball.Ybounce()

    if getSpriteColision(bar, ball):
        ball.Ybounce()

    screen.fill(GREY)

#           <ScreenBlits>

    for i in range(len(blockArrRow1)):
        screen.blit(blockArrRow1[i].getBox(), blockArrRow1[i].getPos())
        screen.blit(blockArrRow2[i].getBox(), blockArrRow2[i].getPos())
        screen.blit(blockArrRow3[i].getBox(), blockArrRow3[i].getPos())
        screen.blit(blockArrRow4[i].getBox(), blockArrRow4[i].getPos())
        screen.blit(blockArrRow5[i].getBox(), blockArrRow5[i].getPos())


    screen.blit(ball.getSurface(), ball.getPos())
    screen.blit(player.getSurface(), player.getPos())
    if pressedKeys[pygame.K_SPACE]:
        start.textRemove()
    screen.blit(bar.getSurface(), bar.getPos())
    screen.blit(start.getText(), start.getPos())
    screen.blit(lives.getText(), lives.getPos())
    screen.blit(score.getText(), score.getPos())
    screen.blit(endScreen.getText(), endScreen.getPos())
    screen.blit(title.getText(), title.getPos())


    clock.tick(FPS)  # will pause game until FPS time is reached
    pygame.display.flip()  # update screen with changes

pygame.quit()