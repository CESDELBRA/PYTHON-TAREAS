# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 18:11:31 2022

@author: Usuario
"""

try:
    x=int(input("Igrece un numero: "))
    y=1/x
    print(y)
except ZeroDivisionError:
    print("No se puede dividir para 0, lo siento")
except ValueError:
        print("Ingresa un valor entero")
except:
    print("Hemos tenido problemas")
    print("Finalizo")   