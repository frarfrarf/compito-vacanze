
import pygame
import sys
from pygame.locals import *
import random


#text_font = pygame.font.SysFont("Spectral" , 30)


class Button():
    def __init__(self, pos, size, screen, text):
        self.pos = pos
        self.size = size
        self.screen = screen
        self.colore1 = (255, 255, 255)
        self.colore2 = (191, 0, 255) #viola
        self.colore= self.colore1
        self.text = text
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.image = pygame.Surface(size)
        self.image.fill(self.colore)
      
    
    def draw(self):
        # pygame.draw.rect(self.image, colore, (4, 4, bordo_width, bordo_height), spessore_bordo)
        self.image.fill(self.colore)
        font = pygame.font.SysFont("Spectral" , 30)
        scritta = font.render(f"{self.text}", True, (0, 0, 0))
        posx = self.size[0] // 2 - scritta.get_width() // 2
        posy = self.size[1] // 2 - scritta.get_height() // 2
        self.image.blit(scritta, (posx, posy))
        self.screen.blit(self.image, self.rect)
        
    
    def checkForInput(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def changeColor(self):
        if self.colore == self.colore1:
             self.colore = self.colore2
        elif self.colore== self.colore2:
            self.colore = self.colore1
        
class Carta:    
    def __init__(self, screen, pos, size) -> None:
        self.screen = screen
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1]) #questi dati andranno cabiati ma per ora fingeremo che andranno bene
        self.image = pygame.image.load('immagini/dietro.png')
        self.image = pygame.transform.scale(self.image, size)

    def draw_text (self, text, font, text_col, x, y):
        font=pygame.font.SysFont("Spectral" , 50)
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x,y))
    
    def draw(self):
        self.screen.blit(self.image, self.rect)

    def genera(self,size):
        n= random.randint(0,22)   
                 #tutte le dimensioni e posizioni sono messe momentaneamente a caso
        if n== 0:
            self.image = pygame.image.load('immagini/matto.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("intraprenderai un nuovo viaggio, un nuovo inizio, guidato dai tuoi soli istinti che ti condurranno attraverso nuove strade che si possono rivelare sia positive che negative.", self.draw_text, (0,0,0), 220,150)

        elif n==1:
            self.image = pygame.image.load('immagini/mago.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("La tua grande volontà farà si che seguendo la ragione riuscirai a portare a termine tutti i tuoi progetti e riuscirai a raggiungere i tuoi più grandi obbiettivi.", self.draw_text, (0,0,0), 220,150)
       
        elif n==2:
            self.image = pygame.image.load('immagini/pretessa.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("Il periodo difficile che stai affrontando non durerà per sempre, è necessario che tu porti pazienza e faccia affidamento alla tua intuizione.", self.draw_text, (0,0,0), 220,150)
       
        elif n==3:
            self.image = pygame.image.load('immagini/imperatrice.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("La ricchezza non è l'unico tipo di abbndanza esistente, e tu stai attraendo proprio uno di questi, si consapevole delle tue doti e delle tue capacità perchè gli altri lo sono.", self.draw_text, (0,0,0), 220,150)
       
        elif n==4:
            self.image = pygame.image.load('immagini/imperatore.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("Ti si pareranno davanti agli occhi scelte difficili,ma il tuo autocontrollo e la predominanza dell'influenza della mente ti renderanno semplice affrontare queste situazioni.", self.draw_text, (0,0,0), 220,150)
       
        elif n==5:
            self.image = pygame.image.load('immagini/ierofante.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("FIdati di te stesso, non lasciarti influenzare ne dalle scelte degli altri ne da tutto ciò che ti circonda, qualsiasi sia il probelma che ti sta frenando sappi che hai le risposte a tutto dentro di te.", self.draw_text, (0,0,0), 220,150)
       
        elif n==6:
            self.image = pygame.image.load('immagini/amanti.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("La carta della dualità non solo interiore, ma anche come confronto con un altra persona, questa carta indica la nscità di una relazione amorosa o non.", self.draw_text, (0,0,0), 220,150)
       
        elif n==7:
            self.image = pygame.image.load('immagini/carro.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("Una forte energia prenderà posseso di questo periodo, e determinazione è la parola chiave, quest'energia sarà in grando di farti aprire gli occhi e i tuoi sogni smetteranno di sembrare irrealizzabili.", self.draw_text, (0,0,0), 220,150)
        
        elif n==8:
            self.image = pygame.image.load('immagini/forza.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("La tua forza è necesssaria a raggiugere la felicità non solo la tua ma anche quella altrui, quindi spezza i vincoli e affronta le tue paure perchè questo è il momento adatto.", self.draw_text, (0,0,0), 220,150)

        elif n==9:
            self.image = pygame.image.load('immagini/eremita.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("La vertità che stai cercando è troppo grande per essere trovata grazie alle tue sole forze, è necessario che tu ti rivolga all'aiuto di qualcuno da te fidato, solo grazie a questo potrai trovarla.", self.draw_text, (0,0,0), 220,150)

        elif n==10:
            self.image = pygame.image.load('immagini/ruota.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("Improvvisi cambiamenti caaratterizzano questo momento; positivi o negativi che essi siano ogni attimo è destinato a passare e così le stituazioni che ti si presenteranno, è importante ricordare che tutto è temporaneo e quindi di vivere nel presente.", self.draw_text, (0,0,0), 220,150)

        elif n==11:
            self.image = pygame.image.load('immagini/giustizia.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("Il karma sarà il concetto predominate di questo momento, prendi ogni decisioe ricordandoti di manternere un'equilibrio, le scelte potrebbero rivelarsi difficili, ma non devi permettere che questo possa influenzare il tuo giudizio.", self.draw_text, (0,0,0), 220,150)
        
        elif n==12:
            self.image = pygame.image.load('immagini/appeso.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("La vita ti sta ponendo davanti ad un bivio ed una delle due scelte implicherà un sacrificio che può riguardare l'allontanamento da persone,ideali o ricordi.", self.draw_text, (0,0,0), 220,150)

        elif n==13:
            self.image = pygame.image.load('immagini/morte.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("Non potrai più pensare di fare affidamento su determinate persone o ideali; il tuò sarà un periodo di cambiamento doloroso e difficile, ma necessario.", self.draw_text, (0,0,0), 220,150)
        
        elif n==14:
            self.image = pygame.image.load('immagini/angelo.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("E' il momento di concentrarsi sulle relazioni che siano famigliari, amichevoli o amorose; spesso queste andranno bene, ma  in caso contrario dovrai provare diversi approcci prima di raggiungere una stabilità.", self.draw_text, (0,0,0), 220,150)

        elif n==15:
            self.image = pygame.image.load('immagini/diavolo.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("In questo momento potresti sentirti prigioniero di te stesso, ma non è così. non fermarti alle apparenze perchè quello che si presenta come vicolo cieco potrebbe in realtà essere un bivio: c'è sempre una scelta.", self.draw_text, (0,0,0), 220,150)
        
        elif n==16:
            self.image = pygame.image.load('immagini/torre.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("Un cambiamento drastico ti si presenterà davanti agli occhi. Non solo ci potranno essere persone che smetteranno di far parte della tua vita, ma anche le tue ambizioni potranno sgretolarsi davanti ai tuoi occhi.", self.draw_text, (0,0,0), 220,150)

        elif n==17:
            self.image = pygame.image.load('immagini/stelle.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("Un periodo positivo ti attende, la fiducia in te stesso caratterizzerà questo momento e la tua senzazione non sarà fittizia poichè porterai a termine molti obbiettivi.", self.draw_text, (0,0,0), 220,150)
        
        elif n==18:
            self.image = pygame.image.load('immagini/luna.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("Indecisione,confusione e un'apparente interminabile attesa caratterizzano questi giorni, è necessario quindi che tu non perda la fiducia in te stesso e sopratutto che ti fidi della tua mente e del tuo intelletto.", self.draw_text, (0,0,0), 220,150)

        elif n==19:
            self.image = pygame.image.load('immagini/sole.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("Attimi di gioia,libertà e spensieratezza saranno frequenti in questo periodo, ricorda però di rimanere comunque concentrato sui tuoi obbiettivi.", self.draw_text, (0,0,0), 220,150)

        elif n==20:
            self.image = pygame.image.load('immagini/giudizio.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("Nelle tue decsione ultimamente stai contando troppo sul tuo istinto senza fermarti a ragionare e a contemplare le scelte possibili, è necessario quindi che tu rallenti e analizzi al meglio le situazioni.", self.draw_text, (0,0,0), 220,150)

        elif n==21:
            self.image = pygame.image.load('immagini/mondo.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("Il periodo complesso che satvi affrontando si sta concludendo per questo senti il peso del mondo su di te, se necessario chiedi aiuto, ricorda però che dopo aver concluso un percoso se ne aprirà uno nuovo subito dopo.", self.draw_text, (0,0,0), 220,150)

    def checkForInput(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    

class Sfera():
    def __init__(self,screen,pos,size):
        self.screen = screen
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1]) 
        self.image = pygame.image.load('immagini/sferascuscu.png')
        self.image = pygame.transform.scale(self.image, size)

    def draw_text (self, text, font, text_col, x, y):
        font=pygame.font.SysFont("Spectral" , 50)
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x,y))
    
    def draw(self):
        self.screen.blit(self.image, self.rect)

    def scrivi(self):
        lista=['Si', 'No', 'Forse', 'Non sperare che vada tutto per il meglio', 'Solo tu sai la risposta','Aspetta e spera',
               'Io questo non posso saperlo', 'Hai già la risposta a questa domanda','Guarda le stelle, ti stanno dicendo di no',
               'Il mondo gira a tuo favore','Mi dispiace','Sarà per la prossima volta','50/50']
        l= random.choice(lista)  
        self.draw_text(l) 

    
    def checkForInput(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False