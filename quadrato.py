# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 11:28:50 2020

@author: Studente
"""

from punto import Punto

class Quadrato:
    def __init__(self, vertice, lato):
        if not (type(vertice) == Punto and isinstance(lato, (int,float))):
            raise TypeError('Quadrato richiede un Punto e un int/float')
        self.v1 = vertice
        self.v2 = Punto(vertice.x+lato, vertice.y)
        self.v3 = Punto(self.v2.x, vertice.y-lato)
        self.v4 = Punto(self.v1.x, self.v3.y)
        self.lato = lato
        
    def __str__(self):
        return f'q({self.v1},{self.v2},{self.v3},{self.v4})'
    # return 'punto(x={},y={})'.format(self.x, self.y)

        
    def __repr__(self):
        return f'quadrato(p={self.v1},lato={self.lato})'
    
    
    def area(self):
        return self.lato**2
    
    
    def perimetro(self):
        return self.lato*4
                    