# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 17:39:52 2022

@author: Usuario
"""

nombre=input("Ingrese Nombre: ")
apellido=input("Ingrese Apellido: ")
direccion=input("Ingrese su direccion: ")
edad=int(input("Ingresa tu edad: "))
space=""
print("Su nombre es",nombre,space,apellido,"vive en la calle",direccion,space,"y suedad es de ",edad,"anos")
if edad<13:
    print(nombre, "Eres un nino")
elif edad>=13 and edad<18:
    print(nombre, "Eres un adolecente")
elif edad>=18 and edad<33:
    print(nombre, "Eres un joven")
elif edad>=33 and edad<65:
    print(nombre, "Eres un adulto") 
else:
    print(nombre, "Eres un adulto mayor")         