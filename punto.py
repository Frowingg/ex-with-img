# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Punto:
    def __init__(self, x, y):
        #if (type(x) == float or type(x) == int) and (type(y) == float or type(y) == int):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self.x = x
            self.y = y
        else:
            raise TypeError ('Errore! x e y devono essere float o int')
#        self.x = float(x)
#        self.y = float(y)
        
        
    def __str__(self):
        return f'p({self.x},{self.y})'
    # return 'punto(x={},y={})'.format(self.x, self.y)

        
    def __repr__(self):
        return f'punto(x={self.x},y={self.y})'

    
    def distanza(self, p):
        if isinstance(p, Punto):
            return ((self.x - p.x)**2 + (self.y - p.y)**2)**0.5
        else:
            raise ValueError ('La distanza si calcola fra due punti')
        
        