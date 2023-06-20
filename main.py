import pygame
import sys
from pygame.locals import *
import random


pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

pygame.display.set_caption('predizioni')

clock = pygame.time.Clock()

fps=60
background = pygame.image.load('cielonotte3.png')
background = pygame.transform.scale(background,window_size)

text_font = pygame.font.SysFont("Spectral" , 30)

def draw_text (text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

class Button():

    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image= image
        self.x_pos=pos[0]
        self.y_pos=pos[1]
        self.font=font
        self.base_color, self.hovering_color = base_color, self.hovering_color
        self.text_input=text_input
        self.text=self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image=self.text
        self.rect=self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.test_rect= self.text.get_rect(center=(self.x_pos, self.y_pos))
    
    def update(self,screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
    
    def checkForInput(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.botton):
            return True
        return False
    
    def changeColor(self,position):
         if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.botton):
             self.text= self.font.render(self.text_input, True, self.hovering_color)
         else:
             self.text= self.font.render(self.text_input, True, self.base_color)

class carta ():
    def __init__(self, screen, pos, size) -> None:
        self.screen = screen
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1]) #questi dati andranno cabiati ma per ora fingeremo che andranno bene
        self.image = pygame.image.load('dietro.png')
        self.image = pygame.transform.scale(self.image, size)

    def genera(self,size):
        n= random.randint(0,22)   
                 #tutte le dimensioni e posizioni sono messe momentaneamente a caso
        if n== 0:
            self.image = pygame.image.load('matto.png')
            self.image = pygame.transform.scale(self.image, size)
            draw_text("intraprenderai un nuovo viaggio, un nuovo inizio, guidato dai tuoi soli istinti che ti condurranno attraverso nuove strade che si possono rivelare sia positive che negative.", text_font, (0,0,0), 220,150)

        elif n==1:
            self.image = pygame.image.load('mago.png')
            self.image = pygame.transform.scale(self.image, size)
            draw_text("La tua grande volontà farà si che seguendo la ragione riuscirai a portare a termine tutti i tuoi progetti e riuscirai a raggiungere i tuoi più grandi obbiettivi.", text_font, (0,0,0), 220,150)
       
        elif n==2:
            self.image = pygame.image.load('pretessa.png')
            self.image = pygame.transform.scale(self.image, size)
            draw_text("Il periodo difficile che stai affrontando non durerà per sempre, è necessario che tu porti pazienza e faccia affidamento alla tua intuizione.", text_font, (0,0,0), 220,150)
       
        elif n==3:
            self.image = pygame.image.load('imperatrice.png')
            self.image = pygame.transform.scale(self.image, size)
            draw_text("La ricchezza non è l'unico tipo di abbndanza esistente, e tu stai attraendo proprio uno di questi, si consapevole delle tue doti e delle tue capacità perchè gli altri lo sono.", text_font, (0,0,0), 220,150)
       
        elif n==4:
            self.image = pygame.image.load('imperatore.png')
            self.image = pygame.transform.scale(self.image, size)
            draw_text("Ti si pareranno davanti agli occhi scelte difficili,ma il tuo autocontrollo e la predominanza dell'influenza della mente ti renderanno semplice affrontare queste situazioni.", text_font, (0,0,0), 220,150)
       
        elif n==5:
            self.image = pygame.image.load('ierofante.png')
            self.image = pygame.transform.scale(self.image, size)
            draw_text("FIdati di te stesso, non lasciarti influenzare ne dalle scelte degli altri ne da tutto ciò che ti circonda, qualsiasi sia il probelma che ti sta frenando sappi che hai le risposte a tutto dentro di te.", text_font, (0,0,0), 220,150)
       
        elif n==6:
            self.image = pygame.image.load('amanti.png')
            self.image = pygame.transform.scale(self.image, size)
            draw_text("La carta della dualità non solo interiore, ma anche come confronto con un altra persona, questa carta indica la nscità di una relazione amorosa o non.", text_font, (0,0,0), 220,150)
       
        elif n==7:
            self.image = pygame.image.load('carro.png')
            self.image = pygame.transform.scale(self.image, size)
            draw_text("Una forte energia prenderà posseso di questo periodo, e determinazione è la parola chiave, quest'energia sarà in grando di farti aprire gli occhi e i tuoi sogni smetteranno di sembrare irrealizzabili.", text_font, (0,0,0), 220,150)
        
        elif n==8:
            self.image = pygame.image.load('forza.png')
            self.image = pygame.transform.scale(self.image, size)
            draw_text("La tua forza è necesssaria a raggiugere la felicità non solo la tua ma anche quella altrui, quindi spezza i vincoli e affronta le tue paure perchè questo è il momento adatto.", text_font, (0,0,0), 220,150)

        elif n==9:
            self.image = pygame.image.load('eremita.png')
            self.image = pygame.transform.scale(self.image, size)
            draw_text("La vertità che stai cercando è troppo grande per essere trovata grazie alle tue sole forze, è necessario che tu ti rivolga all'aiuto di qualcuno da te fidato, solo grazie a questo potrai trovarla.", text_font, (0,0,0), 220,150)

        elif n==10:
            self.image = pygame.image.load('ruota.png')
            self.image = pygame.transform.scale(self.image, size)
            draw_text("Improvvisi cambiamenti caaratterizzano questo momento; positivi o negativi che essi siano ogni attimo è destinato a passare e  così le stituazioni che ti si presenteranno, è importante ricordare che tutto è temporaneo e quindi di vivere nel presente.", text_font, (0,0,0), 220,150)

        elif n==11:
            self.image = pygame.image.load('giustizia.png')
            self.image = pygame.transform.scale(self.image, size)
            draw_text("Il karma sarà il concetto predominate di questo momento, prendi ogni decisioe ricordandoti di manterner eun'equilibrio, le scelte potrebbero riversi difficili, ma non devi permettere che questo possa influenzare il tuo giudizio.", text_font, (0,0,0), 220,150)
        
        elif n==12:
            self.image = pygame.image.load('appeso.png')
            self.image = pygame.transform.scale(self.image, size)
            draw_text("La vita ti sta ponendo davanti ad un bivio ed una delle due scelte implicherà un sacrificio che può riguardare l'allontanamento da persone,ideali o ricordi.", text_font, (0,0,0), 220,150)

        elif n==13:
            self.image = pygame.image.load('morte.png')
            self.image = pygame.transform.scale(self.image, size)
            draw_text("Non potrai più pensare di fare affidamento su determinate persone o ideali; il tuò sarà un periodo di cambiamento doloroso e difficile, ma necessario.", text_font, (0,0,0), 220,150)
        
        elif n==14:
            self.image = pygame.image.load('angelo.png')
            self.image = pygame.transform.scale(self.image, size)
            draw_text("E' il momento di concentrarsi sulle relazioni che siano famigliari, amichevoli o amorose; spesso queste andranno bene, ma  in caso contrario dovrai provare diversi approcci prima di raggiungere una stabilità.", text_font, (0,0,0), 220,150)

        elif n==15:
            self.image = pygame.image.load('diavolo.png')
            self.image = pygame.transform.scale(self.image, size)
            draw_text("In questo momento potresti sentirti prigioniero di te stesso, ma on è così. non fermarti alle apparenze perchè quello che si presenta come vicolo cieco potrebbe in realtà essere un bivio: c'è sempre una scelta.", text_font, (0,0,0), 220,150)
        
        elif n==16:
            self.image = pygame.image.load('torre.png')
            self.image = pygame.transform.scale(self.image, size)
            draw_text("Un cambiamento drastico ti si presenterà davanti agli occhi. Non solo ci potranno essere persone che smetteranno di far parte della tua vita, ma anche le tue ambizioni potranno sgretolarsi davanti ai tuoi occhi.", text_font, (0,0,0), 220,150)

        elif n==17:
            self.image = pygame.image.load('stelle.png')
            self.image = pygame.transform.scale(self.image, size)
            draw_text("Un periodo positivo ti attende, la fiducia in te stesso caratterizzerà questo momento e la tua senzazione non sarà fittizia poichè porterai a termine molti obbiettivi.", text_font, (0,0,0), 220,150)
        
        elif n==18:
            self.image = pygame.image.load('luna.png')
            self.image = pygame.transform.scale(self.image, size)
            draw_text("Indecisione,confusione e un'apparente interminabile attesa caratterizzano questi giorni, è necessario quindi che tu non perda la fiducia in te stesso e sopratutto che ti fidi della tua mente e del tuo intelletto.", text_font, (0,0,0), 220,150)

        elif n==19:
            self.image = pygame.image.load('sole.png')
            self.image = pygame.transform.scale(self.image, size)
            draw_text("Attimi di gioia,libertà e spensieratezza saranno frequenti in questo periodo, ricorda però di rimanere comunque concentrat sui tuoi obbiettivi.", text_font, (0,0,0), 220,150)

        elif n==20:
            self.image = pygame.image.load('giudizio.png')
            self.image = pygame.transform.scale(self.image, size)
            draw_text("Nelle tue decsione ultimamente stai contando troppo sul tuo istinto senza fermarti a ragionare e a contemplare le scelte possibili, è necessario quindi che tu rallenti e analizzi al meglio le situazioni.", text_font, (0,0,0), 220,150)

        elif n==21:
            self.image = pygame.image.load('mondo.png')
            self.image = pygame.transform.scale(self.image, size)
            draw_text("Il periodo complesso che satvi affrontando si sta concludendo per questo senti il peso del mondo su di te, se necessario chiedi aiuto, ricorda però che dopo aver concluso un percoso se ne aprirà uno nuovo subito dopo.", text_font, (0,0,0), 220,150)

def lettura():
    pygame.display.set_caption("lettura")

    while True:
        LETTURA_MOUSE_POS= pygame.mouse.get_pos()
        
        LETTURA_BACK = Button(image=None, pos=(640, 460),
                               text_input="TORNA INDIETRO", font= get_font(75), base_color="White", hovering_color="Green" )
        
        LETTURA_BACK.changeColor(LETTURA_MOUSE_POS)
        LETTURA_BACK.update(SCREEN)

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
           
                
    if start : pass
    


    if not start:
        LETTURA_BUTTON= Button(image=pygame.image.load("assets/lettura rect.png"), pos=(640,250),
                                text_input="LETTURA ", font=get_font(75), base_color="#d7fcd4", hovering_color="white")
    
        for button in [LETTURA_BUTTON]:
                button.changeColor(MOUSE_POS)
                button.update(SCREEN)
        
        for event in pygame.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LETTURA_BUTTON.checkForInput(MOUSE_POS):
                   strat= True
    
    if not 


    pygame.display.update()
    clock.tick(fps)