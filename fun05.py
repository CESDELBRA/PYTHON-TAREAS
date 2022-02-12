# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 19:27:09 2022

@author: Usuario
"""

def direction(ciudad, calle, barrio):
    print("La direccion de envio e: ")
    print("Sector ", barrio)
    print("En la calle ", calle)
    print("En la ciudad de:  ", ciudad)
    
cl=input("Ingrese la calle: ")
ba=input("Ingrese el bario: ")
ci=input("Ingrese la ciudad: ")
direccion(cl, ba, ci)