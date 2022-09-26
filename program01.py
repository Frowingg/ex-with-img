# -*- coding: utf-8 -*-
'''
I Caponians, una specie aliena proviente da un non ben specificato
pianeta della galassia, stanno pianificando da un bel po' l'invasione
del pianeta Terra. Per farlo, hanno creato e installato in vari punti
del pianeta varie *mind bending machine*, macchine che riducono
l'intelligenza degli umani attraverso la rete telefonica [1].

Terminata la fase di riduzione dell'intelligenza umana, il prossimo
passo verso la conquista della Terra sara' lo sbarco sul nostro
pianeta, che avverra' non appena i Caponians avranno trovato dei punti
sufficientemente spaziosi per far atterrare le loro astronavi.

Un'astronave vista dall'alto puo' essere rappresentata come un
rettangolo di dimensioni W (larghezza) e H (altezza). Nel considerare
lo spazio necessario ad un'astronave per atterrare vanno pero' aggiunti
sui 4 lati del rettangolo 4 aree in piu'. Le aree in piu' sono una una
per lato.
Le aree sporgono tutte di una stessa quantita' D, per permettere di
aprire su ogni lato un portellone di sbarco. Ogni portellone e' quindi
largo quanto il lato dell'astronave su cui si trova e lungo D, su
qualunque lato si trovi.

I Caponians vorrebbero sbarcare con le loro astronavi in alcune nostre
citta', di cui hanno scaricato le rispettive mappe. Una citta' puo'
essere rappresentata come un'immagine rettangolare nera, in cui ogni
palazzo e' rappresentato come un rettangolo colorato (ogni palazzo ha
un colore che lo identifica univocamente).

Per definire gli ultimi dettagli del piano di sbarco, i Caponians
hanno bisogno di un algoritmo che, data la mappa di una citta' e un
elenco di astronavi definite come sopra, confermi oppure no se
ciascuna astronave ha abbastanza spazio per atterrare in quella citta',
aprire i suoi 4 portelloni e sbarcare il suo contenuto. Le astronavi
non atterrano contemporaneamente nella citta', quindi vanno valutate
separatamente le une rispetto alle altre.

(1) Quindi, data un'immagine nera (citta') con dei rettangoli colorati
pieni (palazzi) disegnati sopra, con ogni rettangolo di un colore
diverso da tutti gli altri, bisognera':

- determinare posizione, dimensioni e colore di ogni rettangolo
- salvare in un file di testo un rettangolo per riga
- nel file, ogni rettangolo e' rappresentato con una sequenza di 7 valori:
     x, y, w, h, r, g, b
  separati da virgole, in ordine di coordinata y (numero di riga)
  decrescente e, a parimerito, di x (pixel della riga) crescente.





(2) Successivamente, e' dato un file di testo contente N terne di
interi.  Ogni terna separata internamente e dalle altre terne da un
qualunque numero di spazi, tabulazioni o ritorni a capo.
Ogni terna
rappresenta larghezza W, altezza H e distanza minima D (vedere sotto)
di un rettangolo (astronave) che si vorrebbe aggiungere all'immagine
al punto (1):

- restituire una lista di N valori booleani, l'i-esimo valore nella
lista e' True se nell'immagine c'e' abbastanza spazio per inserire
l'i-esimo rettangolo

- un rettangolo puo' essere inserito nell'immagine se esiste almeno una
posizione nell'immagine in cui c'e' abbastanza spazio (cioe' un'area
costituita interamente da pixel neri) per contenere il rettangolo
stesso, piu' le 4 "estensioni" del rettangolo, ossia i 4 portelloni
dell'astronave.

Ad esempio, se un'astronave da inserire ha 2 pixel di
larghezza e 3 di altezza e D = 2, bisognera' cercare uno spazio
nell'immagine adatto a contenere la seguente figura:

                              **
                              **
                            **++**
                            **++**
                            **++**
                              **
                              **

in cui i simboli + sono i pixel del rettangolo/astronave 2x3 e i *
sono i pixel delle 4 estensioni/portelloni

Esempio:
Data la seguente immagine rappresentata con un carattere per ogni
pixel, dove "." e' un pixel nero mentre caratteri diversi da "." sono
pixel colorati (*=rosso, +=verde):

**....
**....
......
......
....++
....++

Il file con i rettangoli trovati da voi salvato deve contenere le
righe:
4,4,2,2,0,255,0
0,0,2,2,255,0,0

e dati le seguenti astronavi:

(3, 3, 0)
(2, 2, 4)
(1, 1, 3)
(4, 2, 1)
(2, 4, 1)
ex
verra' restituita la lista: [True, False, False, False, False]
infatti solo la prima astronave puo' atterrare ad esempio nella
zona marcata da 'X' (non ha sportelloni, infatti D = 0)

**.XXX
**.XXX
...XXX
......
....++
....++

mentre le altre non entrano nella mappa perche', pur avendo un punto
in cui possono atterrare, non possono aprire tutti i portelloni


[1] https://en.wikipedia.org/wiki/Zak_McKracken_and_the_Alien_Mindbenders)
'''

from pngmatrix import load_png8

def ex(file_png, file_txt, file_out):
    navi = []
    contenuto = ""
    lista = []
    palazzi = {}
    h = 0
    img = load_png8(file_png)
    for y, line in enumerate(img):
        for x, pixel in enumerate(line):
            if pixel != (0, 0, 0) and pixel not in palazzi:
                for linea in img:
                    if pixel in linea:
                        h += 1
                    else: 
                        continue
                palazzi[pixel] = (x, y, img[y].count(pixel), h, pixel[0], pixel[1], pixel[2])
                h = 0
    a = sorted(palazzi.values(), key = lambda x: (-x[1], x[0]))
    for x in range(len(a)):        
        contenuto += f"{a[x][0]},{a[x][1]},{a[x][2]},{a[x][3]},{a[x][4]},{a[x][5]},{a[x][6]}\n"
    with open(file_out, 'w') as f:
            f.write(contenuto) 
    with open(file_txt, 'r') as f:
         terne = f.read()
    terne = terne.split()
    n = 0
    for i in range(0, len(terne), 3):
        n+= 1
        navi.append((terne[i], terne[i+1], terne[i+2], n))        
    x = 0
    y = 0
    for navicella in navi:
        ok = None
        W = int(navicella[0])
        H = int(navicella[1])
        D = int(navicella[2])
        for y, line in enumerate(img):
            if len(lista) == navicella[3]:                 
                 break
            for x, pixel in enumerate(line):
                if ok:
                    lista.append(ok)
                    break        
                if D != 0:
                    if y < D:
                        break
                    elif x < D:
                        continue        
                ok = True
                if y+1 == len(img) and x+1 == len(img[0]) and W !=0 and H !=0:
                        ok = False
                        lista.append(ok)
                        break
                elif pixel != (0,0,0):
                    ok = False
                    pass                    
                else:
                    if W == 1 and H == 1:
                        break
                    else:
                      for X in range(x-D, x+W+D):
                        if not ok:
                            break
                        for y_ in range(y, y+H):
                            if X == len(img[0]) or y_ == len(img) or img[y_][X] != (0,0,0):
                                    ok = False
                                    break
                      if ok and D != 0:   
                        for Y in range(y-D, y+H+D):   
                            if not ok:
                              break
                            for x_ in range(x, x+W):
                                if x_ == len(img[0]) or Y == len(img) or img[Y][x_] != (0,0,0):
                                        ok = False
                                        break
    return lista

#ex('image6.png', 'rectangles6.txt', 'test__')                

if __name__ == "__main__":
    pass

