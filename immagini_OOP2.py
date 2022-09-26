# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 17:03:24 2022

@author: edbin
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:38:15 2020

@author: andrea
"""
import images, math

class ImmagineError(Exception):
    pass

class Colore:
    """Rappresentiamo ciascun pixel con un oggetto che permette
        - matematica dei colori
        - conversione in triple RGB
    """
    
    def __init__(self, R, G, B):
        "inizializzazione: memorizza nell'istanza i valori di luminositÃ "
        self._R = R
        self._G = G
        self._B = B

    def __repr__(self):
        "Torna la stringa da usare nelle stampe per visualizzare il coolore"
        return f"Colore({self._R}, {self._G}, {self._B})"
    
    def __mul__(self, k):
        "crea il colore moltiplicando tutte le componenti di questo per un numero"
        return Colore(self._R*k, self._G*k, self._B*k)

    def __add__(self, other):
        "crea il colore come somma componente per componente di due colori"
        return Colore(self._R+other._R, self._G+other._G, self._B+other._B)

    def __sub__(self, other):
        "crea il colore come differenza componente per componente di due colori"
        return Colore(self._R-other._R, self._G-other._G, self._B-other._B)

    def __lt__(self, other):
        "Permette di ordinare liste di colori in base alla luminositÃ "
        return self.luminosita() < other.luminosita()

    def __eq__(self, other):
        "permette di controllare se due colori sono uguali"
        return self._R == other._R and self._G == other._G and self._B == other._B

    def luminosita(self):
        "Calcola la luminositÃ  media del pixel"
        return (self._R + self._G + self._B)//3
    
    def grigio(self):
        "crea il colore grigio con la stessa luminositÃ "
        media = self.luminosita()
        return Colore(media, media, media)
    
    def asTriple(self):
        "torna la terna di valori interi tra 0 e 255 per le immagini PNG"
        def bound(C):
            return min(255, max(0, round(C)))
        return bound(self._R), bound(self._G), bound(self._B)

    def contrasto(self, k):
        "crea il colore in cui si aumenta/diminuisce il contrasto di un fattore k"
        return ((self-Colore.grigio)*k)+Colore.grigio

    def negativo(self):
        "crea il colore negativo di questo"
        return Colore.white - self

    def illumina(self, k):
        "crea il colore in cui si aumenta/diminuisce la luminositÃ  di un fattore k"
        return self*k

# TODO: definire dei colori standard come variabili di classe
# non posso usare Colore senza aver completato la definizione della classe
# quindi definisco solo dopo gli attributi della classe, comuni a tutte le istanze
Colore.white = Colore(255, 255, 255)
Colore.black = Colore(0, 0, 0)
Colore.red   = Colore(255, 0, 0)
Colore.green = Colore(0, 255, 0)
Colore.blue  = Colore(0, 0, 255)
Colore.grey  = Colore(128, 128, 128)
Colore.cyan    = Colore(0, 255, 255)
Colore.purple  = Colore(255, 0, 255)
Colore.magenta = Colore(255, 255, 0)


class Immagine:
    """Immagine rappresentata come lista di liste di Colore.
        - filtri
        - lettura e salvataggio
        - filtri che dipendono dalle coordinate
        - altri effetti
    """

    def __init__(self, w=0, h=0, c=Colore(0,0,0), img=None):
        "crea una immagine larga w e alta h con colore di sfondo c"
        self._w   = w
        self._h   = h
        if img == None:
            self._img = [ [  c  for x in range(w)  ] for y in range(h) ]
        else:
            self._img = img
            self._w   = len(img[0])
            self._h   = len(img)            

    def __repr__(self):
        return f"Immagine( {self._w}, {self._h}, {self._img[0][0]} )"    
    
    def width(self):  return self._w
    def height(self): return self._h

    def inside(self, x, y):
        return 0 <= x < self._w and 0 <= y < self._h
    
    def get_pixel(self, x, y): 
        x = round(x)
        y = round(y)
        if self.inside(x,y):
            return self._img[y][x]
        else:
            return Colore.black
    
    def set_pixel(self, x, y, c):
        if type(c) != Colore:
            raise (f"i parametri di set_pixel devono essere int, int, Colore invece che {x} {y} {c}")        
        if self.inside(x,y):
            x = round(x)
            y = round(y)
            self._img[y][x] = c
#        if x >=0 and y>=0:
#            try:
#                self._img[y][x] = c
#            except:
#                pass
    
    # FIXME: non piÃ¹ necessaria ora che abbiamo i filtri
    '''
    def bw(self):
        "crea una immagine in bianco e nero da quella originale"
        nuova = Immagine(self._w, self._h)
        for y, linea in enumerate(self._img):
            for x, pixel in enumerate(linea):
                nuova._img[y][x] = pixel.grigio()
        return nuova
    '''

    def asTriples(self):
        "torna l'immagine come triple RGB"
        return [ [ pixel.asTriple() for pixel in line ] for line in self._img ]

    @classmethod
    def load(cls, filename):
        "costruttore che torna l'immagine caricata dal file"
        img = images.load(filename)
        return cls(img=[ [ Colore(*pixel) for pixel in line ] 
                                for line in img ])

    def save(self, filename):
        "salva l'immagine nel file PNG filename"
        images.save(self.asTriples(), filename)

    def display(self):
        "mostra l'immagine nella console iPython"
        return images.Image(self.asTriples())

    def filter(self, filtro):
        "crea una nuova immagina applicando un filtro a tutti i pixel"
        if type(filtro) != type(lambda x: x): # FIXME
            raise ImmagineError("Il filtro deve essere una funzione")
        return Immagine(img=[ [ filtro(pixel)  
                            for x,pixel in enumerate(line) ] 
                            for y,line  in enumerate(self._img) ])

    def filter_xy(self, filtro):
        """crea una nuova immagina applicando un filtro che riceve come argomenti:
            - pixel: il colore del pixel
            - x, y: le coordinate del pixel
            - img: la matrice di pixel
        """
        if type(filtro) != type(lambda x: x): # FIXME
            raise ImmagineError("Il filtro deve essere una funzione")
        # TODO: passare solo img w e h
        return Immagine(img=[ [ filtro(pixel,x,y,self.width(), self.height(), self)  
                            for x,pixel in enumerate(line) ] 
                            for y,line  in enumerate(self._img) ])

    def draw_lineH(self, x1, x2, y, c ):
        "disegna una linea orizzontale"
        for x in range(x1, x2+1):
            self.set_pixel(x, y, c)
            
    def draw_lineV(self, y1, y2, x, c ):
        "disegna una linea verticale"
        for y in range(y1, y2+1):
            self.set_pixel(x, y, c)
            
    # TODO: disegnare una qualsiasi linea
    # TODO - iterando sul lato piÃ¹ lungo
    # - interpolando la posizione del pixel
    def draw_line(self, x1, y1, x2, y2, c):
        if x1 > x2:
            x1, x2, y1, y2 = x2, x1, y2, y1        
        dx = x2-x1
        dy = y2-y1
        try:
            m = dy/dx
        except:
            return
        for X in range(0,dx+1):
            Y = X*m
            self.set_pixel(X+x1, Y+y1, c)    

    def draw_rectangle(self, x1, y1, x2, y2, c):
        "disegna un rettangolo"
        self.draw_lineV(y1, y2, x1, c)
        self.draw_lineV(y1, y2, x2, c)
        self.draw_lineH(x1, x2, y1, c)
        self.draw_lineH(x1, x2, y2, c)

    def draw_circle(self, x, y, r, c):
        "disegna un cerchio usando Pitagora"
        for dx in range(-r, r+1):
            dy = int(math.sqrt(r**2-dx**2))
            self.set_pixel(x+dx, y+dy, c)
            self.set_pixel(x+dx, y-dy, c)

    def draw_circle2(self, x, y, r, c):
        "disegna un cerchio usando coordinate polari"
        oldx = x+r
        oldy = y
        for angle in range(360):
            theta = math.radians(angle)
            dx = int(r*math.cos(theta))     # ascissa relativamente al centro
            dy = int(r*math.sin(theta))     # ordinata relativamente al centro
            self.draw_line(x+dx, y+dy, oldx, oldy, c)
            oldx = x+dx
            oldy = y+dy

'''
A proposito di errori e loro cattura

try:
    # codice che puÃ² generare ValueError o IndexError o altri
except ValueError as ve:
    # codice da eseguire se Ã¨ avvenuto un ValueError
    print(ve)
except IndexError as ie:
    # codice da eseguire se Ã¨ avvenuto un IndexError
    print(ie)
    raise ie         # rilancio l'errore in modo che continui a propagarsi
except Exception as e:
    # codice da eseguire per tutti gli errori che non giÃ  catturato (altri)
    print(e)
finally:
    # codice da eseguire in ogni caso dopo il test E dopo il codice degli except
# codice da eseguire dopo il try-except MA SOLO se non ci sono errori che non gestisco

'''


import random
def punto_a_caso(pixel,x,y,w, h, immagine):
    "filtro che torna un pixel a caso nella zona larga 11 intorno al pixel"
    # FIXME: realizzarne una versione che usa try/except
    X = random.randint(max(0, x-5),min(w-1,x+5))
    Y = random.randint(max(0, y-5),min(h-1,y+5))
    return immagine.get_pixel(X, Y)
