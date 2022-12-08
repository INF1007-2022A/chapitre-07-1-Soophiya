#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import turtle as t
import math as m

# TODO: Définissez vos fonction ici
def ellipsoid(volume, a, b, c, density):

    pi = 3.141592653589793

    volume = 3/4 * pi * a * b * c

    mass= density * volume

    return (volume, mass) 

#draw a tree with turtle  
def tree():

    screen = t.Screen()
    screen.bgcolor("white")
   
   



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass
