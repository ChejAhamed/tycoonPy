
import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((800,800))


pygame.display.set_caption("Tycoon")

backgroundImage = pygame.image.load('tycoon.png')
#Colors

red = (255,0,0)
green = (0, 255, 0)
purple = (255,0,255)
black = (0,0,0)

#Object Classes

   
run = True
playing = True
while run:
    
    screen.blit(backgroundImage,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if playing:
        ###
    else:
        screen.fill(black)

        font = pygame.SysFont('Time New Roman', 60)
        title = font.render('TYCOON', False, green)
        titleRect = title.get_rect()
        titleRect.center = (800//2, 100)

    pygame.display.update()

pygame.quit()