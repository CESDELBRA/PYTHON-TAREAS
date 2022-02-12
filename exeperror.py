# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:58:07 2020

@author: Juan Carlos
"""

dict = { 'a' : 'b', 'b' : 'c', 'c' : 'd' }
ch = 'a'
try:
    while True:
        ch = dict[ch]
        print(ch)
except KeyError:
    print('No existe tal clave:', ch)