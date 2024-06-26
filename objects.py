
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
        
class Carta():    
    def __init__(self, screen, pos, size) -> None:
        self.screen = screen
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1]) 
        self.image = pygame.image.load('immagini/dietro.png')
        self.image = pygame.transform.scale(self.image, size)

    def draw_text (self, text, font, text_col, x, y):
        font=pygame.font.SysFont("Spectral" , 25)
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x,y))
    
    def draw(self):
        self.screen.blit(self.image, self.rect)
    
    # def drawgiro(self,size):
        # self.image = pygame.image.load('immagini/dietro.png')
        # self.image = pygame.transform.scale(self.image, size)
        # self.screen.blit(self.image, self.rect)

    def genera(self,size):
        n= random.randint(0,22)   
                 
        if n== 0:
            self.image = pygame.image.load('immagini/mattoveroo.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("intraprenderai un nuovo viaggio, un nuovo inizio,guidato dai tuoi soli istinti che ", self.draw_text, (255,255,255), 50,510)
            self.draw_text("ti condurranno attraverso nuove strade che si possono rivelare sia positive che negative.", self.draw_text, (255,255,255), 50,525)
        
        elif n==1:
            self.image = pygame.image.load('immagini/magovero.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("La tua grande volontà farà si che seguendo la ragione riuscirai a portare a termine ", self.draw_text, (255,255,255), 50,510)
            self.draw_text("tutti i tuoi progetti e riuscirai a raggiungere i tuoi più grandi obbiettivi.", self.draw_text, (255,255,255), 50,525)
        
        elif n==2:
            self.image = pygame.image.load('immagini/pretessa.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("Il periodo difficile che stai affrontando non durerà per sempre, ", self.draw_text, (255,255,255), 50,510)
            self.draw_text("è necessario che tu porti pazienza e faccia affidamento alla tua intuizione.", self.draw_text, (255,255,255), 50,525)
        
        elif n==3:
            self.image = pygame.image.load('immagini/imperatrice.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("La ricchezza non è l'unico tipo di abbndanza esistente, e tu stai attraendo proprio ", self.draw_text, (255,255,255), 50,510)
            self.draw_text("uno di questi, si consapevole delle tue doti e delle tue capacità perchè gli altri lo sono.", self.draw_text, (255,255,255), 50,525)
       
        elif n==4:
            self.image = pygame.image.load('immagini/imperatore.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("Ti si pareranno davanti agli occhi scelte difficili,ma il tuo autocontrollo e la predominanza", self.draw_text, (255,255,255), 50,510)
            self.draw_text("dell'influenza della mente ti renderanno semplice affrontare queste situazioni.", self.draw_text, (255,255,255), 50,525)
        
        elif n==5:
            self.image = pygame.image.load('immagini/ierofante.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("Fidati di te stesso, non lasciarti influenzare ne dalle scelte degli altri ne ", self.draw_text, (255,255,255), 50,510)
            self.draw_text("da tutto ciò che ti circonda,qualsiasi sia il probelma che ti sta frenando", self.draw_text, (255,255,255), 50,525)
            self.draw_text("sappi che hai le risposte a tutto dentro di te.", self.draw_text, (255,255,255), 50,540)
        
        elif n==6:
            self.image = pygame.image.load('immagini/amanti.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("La carta della dualità non solo interiore, ma anche come confronto con un'altra persona,", self.draw_text, (255,255,255), 50,510)
            self.draw_text("questa carta indica la nascità di una relazione amorosa o non.", self.draw_text, (255,255,255), 50,525)
        
        elif n==7:
            self.image = pygame.image.load('immagini/carro.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("Una forte energia prenderà posseso di questo periodo,", self.draw_text, (255,255,255), 50,510)
            self.draw_text("determinazione è la parola chiave,quest'energia sarà in grando di farti aprire gli occhi ", self.draw_text, (255,255,255), 50,525)
            self.draw_text("e i tuoi sogni smetteranno di sembrare irrealizzabili.", self.draw_text, (255,255,255), 50,540)
        
        elif n==8:
            self.image = pygame.image.load('immagini/forza.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("La tua forza è necesssaria a raggiugere la felicità non solo la tua ma anche quella altrui,", self.draw_text, (255,255,255), 50,510)
            self.draw_text("quindi spezza i vincoli e affronta le tue paure perchè questo è il momento adatto.", self.draw_text, (255,255,255), 50,525)
        
        elif n==9:
            self.image = pygame.image.load('immagini/eremita.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("La vertità che stai cercando non può essere trovata grazie alle tue sole forze,", self.draw_text, (255,255,255), 50,510)
            self.draw_text("è necessario che tu ti rivolga all'aiuto di qualcuno da te fidato, ", self.draw_text, (255,255,255), 50,525)
            self.draw_text("solo grazie a questo potrai trovarla.", self.draw_text, (255,255,255), 50,540)
        
        elif n==10:
            self.image = pygame.image.load('immagini/ruota.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("Improvvisi cambiamenti caratterizzano questo momento;positivi o negativi che essi  ", self.draw_text, (255,255,255), 50,510)
            self.draw_text("siano ogni attimo è destinato a passare e così anche le stituazioni che ti si presenteranno, ", self.draw_text, (255,255,255), 50,525)  
            self.draw_text("è importante ricordare che tutto è temporaneo e quindi di vivere nel presente.", self.draw_text, (255,255,255), 50,540)  
        
        elif n==11:
            self.image = pygame.image.load('immagini/giustizia.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("Il karma sarà il concetto predominate di questo momento, prendi ogni decisione ", self.draw_text, (255,255,255), 50,510)
            self.draw_text("ricordandoti di manternere un'equilibrio,le scelte potrebbero rivelarsi difficili,", self.draw_text, (255,255,255), 50,525)
            self.draw_text("ma non devi permettere che questo possa influenzare il tuo giudizio.", self.draw_text, (255,255,255), 50,540)
        
        elif n==12:
            self.image = pygame.image.load('immagini/appeso.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("La vita ti sta ponendo davanti ad un bivio ed una delle due scelte implicherà un sacrificio", self.draw_text, (255,255,255), 50,510)
            self.draw_text("che può riguardare l'allontanamento da persone,ideali o ricordi.", self.draw_text, (255,255,255), 50,525)

        elif n==13:
            self.image = pygame.image.load('immagini/morte.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("Non potrai più pensare di fare affidamento su determinate persone o ideali;", self.draw_text, (255,255,255), 50,510)
            self.draw_text("il tuò sarà un periodo di cambiamento doloroso e difficile, ma necessario.", self.draw_text, (255,255,255), 50,525)
        
        elif n==14:
            self.image = pygame.image.load('immagini/angelo.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("E' il momento di concentrarsi sulle relazioni che siano famigliari, ", self.draw_text, (255,255,255), 50,510)
            self.draw_text("amichevoli o amorose;spesso queste andranno bene, ma in caso contrario ", self.draw_text, (255,255,255), 50,525)
            self.draw_text("dovrai provare diversi approcci prima di raggiungere una stabilità.", self.draw_text, (255,255,255), 50,540)

        elif n==15:
            self.image = pygame.image.load('immagini/diavolo.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("In questo momento potresti sentirti prigioniero di te stesso, ma non è così.", self.draw_text, (255,255,255), 50,510)
            self.draw_text("Non fermarti alle apparenze perchè quello che si presenta come vicolo cieco ", self.draw_text, (255,255,255), 50,525)
            self.draw_text("potrebbe in realtà essere un bivio: c'è sempre una scelta.", self.draw_text, (255,255,255), 50,540)
        
        elif n==16:
            self.image = pygame.image.load('immagini/torre.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("Un cambiamento drastico ti si presenterà davanti agli occhi.", self.draw_text, (255,255,255), 50,510)
            self.draw_text("Non solo ci potranno essere persone che smetteranno di far parte della tua vita,", self.draw_text,(255,255,255), 50,525)
            self.draw_text("ma anche le tue ambizioni potranno sgretolarsi davanti ai tuoi occhi.", self.draw_text,(255,255,255), 55,540)

        elif n==17:
            self.image = pygame.image.load('immagini/stelle.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("Un periodo positivo ti attende, la fiducia in te stesso caratterizzerà questo momento", self.draw_text, (255,255,255), 50,510)
            self.draw_text("e la tua senzazione non sarà fittizia poichè porterai a termine molti obbiettivi.", self.draw_text, (255,255,255), 50,525)
        
        elif n==18:
            self.image = pygame.image.load('immagini/luna.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("Indecisione,confusione e un'apparente interminabile attesa caratterizzano questi giorni,", self.draw_text, (255,255,255), 50,510)
            self.draw_text("è necessario quindi che tu non perda la fiducia in te stesso e sopratutto ", self.draw_text, (255,255,255), 50,525)
            self.draw_text("che ti fidi della tua mente e del tuo intelletto.", self.draw_text, (255,255,255), 50,540)

        elif n==19:
            self.image = pygame.image.load('immagini/sole.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("Attimi di gioia,libertà e spensieratezza saranno frequenti in questo periodo,", self.draw_text, (255,255,255), 50,510)
            self.draw_text("ricorda però di rimanere comunque concentrato sui tuoi obbiettivi.", self.draw_text, (255,255,255), 50,525)

        elif n==20:
            self.image = pygame.image.load('immagini/giudizio.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("Nelle tue decsioni ultimamente stai contando troppo sul tuo istinto senza fermarti ", self.draw_text, (255,255,255), 50,510)
            self.draw_text("a ragionare e a contemplare le scelte possibili,è necessario quindi ", self.draw_text,(255,255,255), 50,525)
            self.draw_text("che tu rallenti e analizzi al meglio le situazioni.", self.draw_text, (255,255,255), 50,540)

        elif n==21:
            self.image = pygame.image.load('immagini/mondo.png')
            self.image = pygame.transform.scale(self.image, size)
            self.draw_text("Il periodo complesso che satvi affrontando si sta concludendo per questo ", self.draw_text, (255,255,255), 50,510)
            self.draw_text("senti il peso del mondo su di te,se necessario chiedi aiuto, ricorda però ", self.draw_text, (255,255,255), 50,525)
            self.draw_text("che dopo aver concluso un percoso se ne aprirà uno nuovo subito dopo.", self.draw_text, (255,255,255), 50,540)
        

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
               'Il mondo gira a tuo favore','Mi dispiace','Sarà per la prossima volta','Fifty fifty','Ho chiesto in giro e mi hanno detto di no',
               'Si,corri', 'Se è il cuore a dirtelo allora è la cosa giusta','non farlo, andrà male']
        l= random.choice(lista)  
        self.draw_text(l,'Spectral',(255,255,255), 50,525) 

    
    def checkForInput(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False