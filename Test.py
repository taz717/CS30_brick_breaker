'''
Moataz Khallaf A.K.A Hackerman
BrickBreaker
4/26/2019
'''
from myClass import text, box, getSpriteColision, mySprite
import pygame
pygame.init  # Loads PyGame Module commands in the program

# Display Variables

TITLE = "TestsimulatorEXXXD"  # Appears in window title
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
GREEN = (0, 230, 64)
BLUE = (0, 0, 255)
PINK = (255, 53, 127)

# Create the window

screen = pygame.display.set_mode(SCREENDIM)  # creates the main surface where all assets are placed
pygame.display.set_caption(TITLE)  # updates the windows title
screen.fill(GREY)  # fills the entire surface with the colour ie. erase

clock = pygame.time.Clock()  # starts a clock object to measure time

# Code starts here
running = True

box1 = box((WIDTH/2 - 50), (HEIGHT/2 - 50), 100, 100, 10, 10)
box1.setColor(GREEN)
box2 = box(300, 300, 30, 30, 10, 0)
box2.setColor(RED)
box3 = box((WIDTH/2 - 15), 0, 30, 30, 0, 10)
box3.setColor(RED)
box4 = box(30, 30, 30, 30, 10, 10)
box4.setColor(RED)

while running:
    for event in pygame.event.get():  # returns all inputs and triggers into an array
        if event.type == pygame.QUIT:  # if red x was clicked
            running = False

    pressedkey = pygame.key.get_pressed()

    #box1.playerMove(pressedkey)
    box2.autoMove()
    box3.autoMove()
    box4.autoMove()

    if getSpriteColision(box1, box2) or getSpriteColision(box1, box3):
        box1.setColor(WHITE)
    else:
        box1.setColor(GREEN)

    if getSpriteColision(box1, box2):
        box2.Xbounce()

    if getSpriteColision(box1, box3):
        box3.Ybounce()

    if getSpriteColision(box1, box4):
        box4.bounce()
        box1.setPos(999, 999)

    screen.fill(GREY)

    screen.blit(box1.getSurface(), box1.getPos())
    screen.blit(box2.getSurface(), box2.getPos())
    screen.blit(box3.getSurface(), box3.getPos())
    screen.blit(box4.getSurface(), box4.getPos())


    clock.tick(FPS)  # will pause game until FPS time is reached
    pygame.display.flip()  # update screen with changes

pygame.quit()