
import pygame
from pygame.locals import *
#Initialize the pygame
class Board():
    def __init__(self):
        
        pygame.init()

        width = 1000
        height = 1000
        #create the window
        window = pygame.display.set_mode((1400,1000))
        pygame.display.set_caption("Tycoon")

        #background Image loaded
        backgroundImage = pygame.image.load('tycoon.png')
        #icon set to be image from loaded for the background
        pygame.display.set_icon(backgroundImage)

        playerOne = pygame.image.load('boris.jpg')
        #Positions
        initialPosition = 910, 910
        position1 = 800,910
        position2 = 720,900
        position3 = 640,920
        position4 = 560,910
        position5 = 480,910
        position6 = 390,910
        position7 = 310,900
        position8 = 230,910
        position9 = 150,910
        position10Jail = 50,890
        position10Visit = 20,930
        position11 = 30,910
        position12 = 30,790
        position13 = 30,710
        position14 = 20,630
        position15 = 20,545
        position16 = 30,465
        position17 = 20,385
        position18 = 40,305
        position19 = 20,220
        position20 = 25,140
        position21 = 40,50
        position22 = 150,20
        position23 = 230,40
        position24 = 310,20
        position25 = 390,20
        position26 = 480,25
        position27 = 560,20
        position28 = 640,20
        position29 = 720,20
        position30 = 800,20
        position31 = 910,40
        position32 = 930,140
        position33 = 930,220
        position34 = 910,300
        position35 = 930,380
        position36 = 920,465
        position37 = 910,545
        position38 = 930,625
        position39= 920,710
        position40= 930,790


        runing = True
        while runing:
            window.blit(backgroundImage,(0,0))
            window.blit(playerOne,(position25))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runing = False


            pygame.display.update()
        pygame.quit()





