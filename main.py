import pygame
import sys
from pygame.locals import *
import random
from objects import *
from pygame import mixer


pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

pygame.display.set_caption('Scelte')

clock = pygame.time.Clock()

fps=60
background = pygame.image.load('immagini/cielonotte3.png')
background = pygame.transform.scale(background,window_size)

#text_font = pygame.font.SysFont("Spectral" , 30)

# mixer.init()

# mixer.music.load('non mi convince.mp3')   #scegli canzoncella
# mixer.music.set_volume(15)
# mixer.music.play

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
           
    carta=Carta(screen, (300,50),(250,420))   

    while start and not sfera:                                       #lettura
        # sfondino = pygame.image.load('immagini/cielonotte lettura.png')
        # sfondino = pygame.transform.scale(sfondino,window_size)

        # screen.fill((0 ,0 ,0))
        # screen.blit (sfondino, (0,0))

        pygame.display.set_caption('lettura')

        LETTURA_MOUSE_POS= pygame.mouse.get_pos()
        
        LETTURA_BACK = Button((700, 50), (50, 50), screen, "<--")
        LETTURA_BACK.draw()

        girata = False    
        

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
                    sfera = False
                    
                if carta.checkForInput(LETTURA_MOUSE_POS):
                   girata= True
                #    carta.genera((250,420))
                #    carta.draw()
                   
        if girata== True:
             screen.fill((0 ,0 ,0))
             screen.blit (background, (0,0))
             carta.genera((250,420))
             carta.draw()
             if LETTURA_BACK.rect.collidepoint(MOUSE_POS):

                LETTURA_BACK.changeColor()
                LETTURA_BACK.draw()
    

        elif girata == False:
            carta.draw()
       

        #for event in pygame.event.get():
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if carta.checkForInput(LETTURA_MOUSE_POS):
            #        carta.genera((250,420))
            #        carta.draw()



        pygame.display.update()

    
    while start and sfera:                                      #sfera
        # sfondone= pygame.image.load('immagini/cielonotte sfera.png')
        # sfondone = pygame.transform.scale(sfondone,window_size)

        # screen.fill((0 ,0 ,0))
        # screen.blit (sfondone, (0,0))
        
        
        pygame.display.set_caption('sfera')
        SFERA_MOUSE_POS= pygame.mouse.get_pos()
        
        SFERA_BACK = Button((700, 50), (50, 50), screen, "<--")
        SFERA_BACK.draw()
        scritta = False

        if SFERA_BACK.rect.collidepoint(MOUSE_POS):
            SFERA_BACK.changeColor()
            SFERA_BACK.draw()
        
        sferascuscu=Sfera(screen, (240,50),(342,443))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SFERA_BACK.checkForInput(SFERA_MOUSE_POS):
                    start = False
                    sfera = False
                if sferascuscu.checkForInput(MOUSE_POS):
                   #sferascuscu.scrivi()
                   scritta= True
        
        
        sferascuscu.draw()
        
        if scritta== True:
            screen.fill((0 ,0 ,0))
            screen.blit (background, (0,0))
            sferascuscu.scrivi()
        
        if SFERA_BACK.rect.collidepoint(MOUSE_POS):
            SFERA_BACK.changeColor()
            SFERA_BACK.draw()
        
        
        
        
        
        # for event in pygame.event.get():
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         if sferascuscu.checkForInput(MOUSE_POS):
        #            sferascuscu.scrivi()

        pygame.display.update()

    if not start:                                           #main menu
        LETTURA_BUTTON= Button((250, 220), (300, 50), screen, "Lettura tarocchi")
        SFERA_BUTTON= Button((250, 320), (300, 50), screen, "Consulta la sfera")
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
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LETTURA_BUTTON.checkForInput(MOUSE_POS):
                   start= True
                if SFERA_BUTTON.checkForInput(MOUSE_POS):
                     start = True
                     sfera = True
               
    
    


    pygame.display.update()
    clock.tick(fps)