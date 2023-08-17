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
spiego= False
spiega= False

while True:

    screen.fill((0 ,0 ,0))
    screen.blit (background, (0,0))
    
    MOUSE_POS = pygame.mouse.get_pos()
    

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
           
    carta=Carta(screen, (300,50),(250,420))   
    sferascuscu=Sfera(screen, (240,50),(342,443))

    while start and not sfera and not spiego:                                       #lettura
        # sfondino = pygame.image.load('immagini/cielonotte lettura.png')
        # sfondino = pygame.transform.scale(sfondino,window_size)

        # screen.fill((0 ,0 ,0))
        # screen.blit (sfondino, (0,0))

        pygame.display.set_caption('Lettura')

        LETTURA_MOUSE_POS= pygame.mouse.get_pos()
        
        LETTURA_BACK = Button((700, 50), (50, 50), screen, "<--")
        LETTURA_BACK.draw()

        LETTURA_SPIEGAZIONE = Button((50, 400), (200, 50), screen, "come funziona")
        LETTURA_SPIEGAZIONE.draw()
        girata = False    
        

        if LETTURA_BACK.rect.collidepoint(MOUSE_POS):

            LETTURA_BACK.changeColor()
            LETTURA_BACK.draw()
    
        if LETTURA_SPIEGAZIONE.rect.collidepoint(MOUSE_POS):

            LETTURA_SPIEGAZIONE.changeColor()
            LETTURA_SPIEGAZIONE.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if LETTURA_BACK.checkForInput(LETTURA_MOUSE_POS):
                    start = False
                    sfera = False
                    spiego = False
                    spiega = False
                
                if LETTURA_SPIEGAZIONE.checkForInput(LETTURA_MOUSE_POS):
                    spiego = True

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
        
        pygame.display.set_caption('Sfera')
        SFERA_MOUSE_POS= pygame.mouse.get_pos()

        scritta = False

        SFERA_BACK = Button((700, 50), (50, 50), screen, "<--")
        SFERA_BACK.draw()

        SFERA_SPIEGAZIONE = Button((50, 400), (200, 50), screen, "come funziona")
        SFERA_SPIEGAZIONE.draw()
        

        if SFERA_BACK.rect.collidepoint(MOUSE_POS):
            SFERA_BACK.changeColor()
            SFERA_BACK.draw()

        if SFERA_SPIEGAZIONE.rect.collidepoint(MOUSE_POS):

            SFERA_SPIEGAZIONE.changeColor()
            SFERA_SPIEGAZIONE.draw()
        
        #sferascuscu=Sfera(screen, (240,50),(342,443))
        
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         sys.exit()
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         if SFERA_BACK.checkForInput(SFERA_MOUSE_POS):
        #             start = False
        #             sfera = False
        #             spiega= False
        #             spiego= False
        #         if SFERA_SPIEGAZIONE.checkForInput(SFERA_MOUSE_POS):
        #             spiega= True
        #             start = False
        #             sfera = False
        #             spiego= False

        #         if sferascuscu.checkForInput(MOUSE_POS):
        #            #sferascuscu.scrivi()
        #            scritta= True
        
        
        sferascuscu.draw()
        
        if scritta== True:
            screen.fill((0 ,0 ,0))
            screen.blit (background, (0,0))
            sferascuscu.scrivi()
        
        if SFERA_BACK.rect.collidepoint(MOUSE_POS):
            SFERA_BACK.changeColor()
            SFERA_BACK.draw()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if sferascuscu.checkForInput(SFERA_MOUSE_POS):
                   #sferascuscu.scrivi()
                   scritta= True

                if SFERA_BACK.checkForInput(SFERA_MOUSE_POS):
                    start = False
                    sfera = False
                    spiega= False
                    spiego= False

                if SFERA_SPIEGAZIONE.checkForInput(SFERA_MOUSE_POS):
                    spiega= True
                    start = False
                    sfera = False
                    spiego= False
                    scritta= True 

        if scritta== True:
            screen.fill((0 ,0 ,0))
            screen.blit (background, (0,0))
            sferascuscu.scrivi()



        pygame.display.update()


        

    while spiego == True:

        pygame.display.set_caption('spiegazione tarocchi')
        sfondone= pygame.image.load('immagini/cielonottespiegazione.png')
        sfondone = pygame.transform.scale(sfondone,window_size)

        screen.fill((0 ,0 ,0))
        screen.blit (sfondone, (0,0))
        
        SPIEGO_MOUSE_POS= pygame.mouse.get_pos()

        SPIEGO_BACK = Button((700, 50), (50, 50), screen, "<--")
        SPIEGO_BACK.draw()

        if SPIEGO_BACK.rect.collidepoint(SPIEGO_MOUSE_POS):

            SPIEGO_BACK.changeColor()
            SPIEGO_BACK.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if SPIEGO_BACK.checkForInput(SPIEGO_MOUSE_POS):
                    start = True
                    sfera = False
                    spiego= False
                    spiega= False
        
        pygame.display.update()

    

    while spiega == True:

        pygame.display.set_caption('spiegazione sfera')
        sfondino= pygame.image.load('immagini/cielonottespiegazionesfera.png')
        sfondino = pygame.transform.scale(sfondino,window_size)

        screen.fill((0 ,0 ,0))
        screen.blit (sfondino, (0,0))
        
        SPIEGA_MOUSE_POS= pygame.mouse.get_pos()

        SPIEGA_BACK = Button((700, 50), (50, 50), screen, "<--")
        SPIEGA_BACK.draw()

        if SPIEGA_BACK.rect.collidepoint(SPIEGA_MOUSE_POS):

            SPIEGA_BACK.changeColor()
            SPIEGA_BACK.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if SPIEGA_BACK.checkForInput(SPIEGA_MOUSE_POS):
                    start = True
                    sfera = True
                    spiego= False
                    spiega= False
                    scritta= True
        
        pygame.display.update()



    if not start:                                           #main menu
        pygame.display.set_caption('Scelte')
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