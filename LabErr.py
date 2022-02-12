# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 18:51:45 2022

@author: Usuario
"""

try:
    v=int(input("Igrece un numero entre -10 y 10: "))
    y=1/v
    print(y)
except ZeroDivisionError:
    print("No se puede dividir para 0, lo siento")
except ValueError:
        print("Ingresa un valor entero")
try:
    x=int(input("Igrece un numero: "))
except:
    print("Dato ingresado icorrecto")
    print("Fin")