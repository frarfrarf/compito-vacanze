import pygame
import sys
from pygame.locals import *
import random
from objects import *


pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

pygame.display.set_caption('Scelte')

clock = pygame.time.Clock()

fps=60
background = pygame.image.load('immagini/cielonotte3.png')
background = pygame.transform.scale(background,window_size)

#text_font = pygame.font.SysFont("Spectral" , 30)

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
           
                
    if start and not sfera:     #lettura
        pygame.display.set_caption('lettura')
        LETTURA_MOUSE_POS= pygame.mouse.get_pos()
        
        LETTURA_BACK = Button((110, 460), (100, 50), screen, "TORNA INDIETRO")
        LETTURA_BACK.draw()

         
        if LETTURA_BACK.rect.collidepoint(MOUSE_POS):

            LETTURA_BACK.changeColor()
            LETTURA_BACK.draw()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LETTURA_BACK.checkForInput(LETTURA_MOUSE_POS):
                    start = False
        
        carta=Carta(screen, (300,50),(250,420))
        carta.draw()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if carta.checkForInput(MOUSE_POS):
                   carta.genera((250,420))


        pygame.display.update()

    
    if start and sfera:    #sfera
        pygame.display.set_caption('sfera')
        SFERA_MOUSE_POS= pygame.mouse.get_pos()
        
        SFERA_BACK = Button((110, 460), (100, 50), screen, "TORNA INDIETRO")
        SFERA_BACK.draw()

        if SFERA_BACK.rect.collidepoint(MOUSE_POS):
            SFERA_BACK.changeColor()
            SFERA_BACK.draw()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SFERA_BACK.checkForInput(SFERA_MOUSE_POS):
                    start = False

        pygame.display.update()

    if not start:    #main menu
        LETTURA_BUTTON= Button((100, 300), (120, 50), screen, "LETTURA TAROCCHI")
        SFERA_BUTTON= Button((43, 460), (120, 50), screen, "CONSULTA LA SFERA")
        LETTURA_BUTTON.draw()
        SFERA_BUTTON.draw()

        if LETTURA_BUTTON.rect.collidepoint(MOUSE_POS):

            LETTURA_BUTTON.changeColor()
            LETTURA_BUTTON.draw()
        
        
        if SFERA_BUTTON.rect.collidepoint(MOUSE_POS):

            SFERA_BUTTON.changeColor()
            SFERA_BUTTON.draw()

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         sys.exit()

        
          
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LETTURA_BUTTON.checkForInput(MOUSE_POS):
                   start= True
                if SFERA_BUTTON.checkForInput(MOUSE_POS):
                     start = True
                     sfera = True
                     
    
    


    pygame.display.update()
    clock.tick(fps)