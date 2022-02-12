# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:55:58 2020

@author: Juan Carlos
"""

from math import exp
ex = 1
try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('El número es demasiado grande.')