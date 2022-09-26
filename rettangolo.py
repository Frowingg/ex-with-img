# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 11:48:16 2020

@author: Studente
"""
from punto import Punto


class Rettangolo:
    def __init__(self, vertice_as, vertice_bd):
        if not (type(vertice_as) == Punto and type(vertice_bd) == Punto):
            raise TypeError('Rettangolo richiede due vertici di tipo Punto')
        self.v1 = vertice_as
        self.v3 = vertice_bd
        self.v2 = Punto(self.v3.x, self.v1.y)
        self.v4 = Punto(self.v1.x, self.v3.y)
        self.base = self.v3.distanza(self.v4)
        self.altezza = self.v3.distanza(self.v2)
        
    def __str__(self):
        return f'r({self.v1},{self.v2},{self.v3},{self.v4})'
    # return 'punto(x={},y={})'.format(self.x, self.y)

        
    def __repr__(self):
        return self.__str__()

    def area(self):
        return self.base * self.altezza
        
    def perimetro(self):
        return self.base*2 + self.altezza*2
    
    def diagonale(self):
        return self.v1.distanza(self.v3)