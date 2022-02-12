# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 18:39:22 2022

@author: Usuario
"""
lista=[]
file = open("C:/Users/Usuario/PythonCEC-220201/220211/devices.txt")
for a in file:
    a=a.strip("\n")
    lista.append(a)
    #print(a)
file.close()
print(lista)