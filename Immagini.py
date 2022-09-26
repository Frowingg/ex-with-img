# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 12:03:18 2020

@author: Studente
"""

from punto import Punto
from rettangolo import Rettangolo
from quadrato import Quadrato
import images 

class Immagine:
    def __init__(self, larghezza, altezza, colore_sfondo):
        self.imm = []
        for riga in range(altezza):
            self.imm.append([colore_sfondo]*larghezza)
        self.h = altezza
        self.w = larghezza
        self.filename = 'immagine.png'
        
    def set_filename(self, filename):
        self.filename = filename
        
    def save(self):
        images.save(self.imm, self.filename)
        
    def disegna_punto(self, p, colore):
        self.imm[p.y][p.x] = colore
        
    def disegna_quadrato(self, q, colore):
        if isinstance(q, Quadrato):
            for pixel in range(q.v1.x, q.v2.x+1):
                self.imm[q.v1.y][pixel] = colore
                self.imm[q.v3.y][pixel] = colore
            for riga in range(q.v3.y, q.v1.y+1):
                self.imm[riga][q.v1.x] = colore
                self.imm[riga][q.v2.x] = colore