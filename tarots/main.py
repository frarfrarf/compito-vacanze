import pygame
import sys
from pygame.locals import *
import random
from objects import *


pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

pygame.display.set_caption('predizioni')

clock = pygame.time.Clock()

fps=60
background = pygame.image.load('cielonotte3.png')
background = pygame.transform.scale(background,window_size)

#text_font = pygame.font.SysFont("Spectral" , 30)

def lettura():
    pygame.display.set_caption("lettura")

    while True:
        LETTURA_MOUSE_POS= pygame.mouse.get_pos()
        
        LETTURA_BACK = Button((110, 460), (70, 50), screen, "TORNA INDIETRO")
        LETTURA_BACK.draw()
        LETTURA_BACK.changeColor(LETTURA_MOUSE_POS)
        LETTURA_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LETTURA_BACK.checkForInput(LETTURA_MOUSE_POS):
                    start = False

        pygame.display.update()

start= False 
sfera= False

while True:

    screen.fill((0 ,0 ,0))
    screen.blit (background, (0,0))
    
    MOUSE_POS = pygame.mouse.get_pos()
    

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
           
                
    if start and not sfera: pass
    
    if start and sfera:
         pass

    if not start:
        LETTURA_BUTTON= Button((640, 460), (70, 50), screen, "LETTURA TAROCCHI")
        SFERA_BUTTON= Button((43, 460), (70, 50), screen, "CONSULTA LA SFERA")
        LETTURA_BUTTON.draw()
        SFERA_BUTTON.draw()
        # for button in [LETTURA_BUTTON]:
        #         button.changeColor(MOUSE_POS)
        #         button.update(screen)
        
        # for button in [SFERA_BUTTON]:
        #         button.changeColor(MOUSE_POS)
        #         button.update(screen)

        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LETTURA_BUTTON.checkForInput(MOUSE_POS):
                   start= True
                if SFERA_BUTTON.checkForInput(MOUSE_POS):
                     start = True
                     sfera = True
                     
    
    


    pygame.display.update()
    clock.tick(fps)