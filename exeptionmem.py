# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:54:24 2020

@author: Juan Carlos
"""

string = 'x'
try:
    while True:
        string = string + string
        print(len(string))
except MemoryError:
    print('¡Esto no es gracioso!')