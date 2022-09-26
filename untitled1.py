# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 18:12:40 2022

@author: edbin
"""

def nuova_immagine(w, h, c, D):
    return  [ [c]*(w-D)  for y in range(h) ]

def filled_rectangle(img, x, y, w, h, c):
    for Y in range(y, y+h):
        line_h(img, x, Y, w, c )
    print(img)
        
def line_h(img, x, y, l, c ):
    img[y][x:x+1] = [c]*l
    
def crea_navicella(sfondo, pixel, W, H, D):   
    H_tot = int(H + D*2)
    W_tot = int(W + D*2)
    img = nuova_immagine(W_tot, H_tot, sfondo, D)
    print(img)
    filled_rectangle(img, 0, D, W, H, pixel)
    print(img)

crea_navicella((0,0,0), (255,0,0), 4, 5, 3)