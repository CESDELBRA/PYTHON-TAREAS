# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 19:34:10 2022

@author: Usuario
"""

lista1=["Python",58,True,25.8]
print(type(lista1))
print(len(lista1))
print(lista1)
print(lista1[0])
print(lista1[1])
print(lista1[2])
print(lista1[3])
#print(lista1[4])#error porque solo tiene 4 valores que van del 0 al 3
print(lista1[-1])
print(lista1[-2])
print(lista1[-3])
print(lista1[-4])
#print(lista1[-5])#error porque solo va del rango 0 al 3
tupla1=("Python",58,True,25.8)
print(tupla1)
print(tupla1[0])
print(tupla1[1])
print(tupla1[2])
print(tupla1[3])
print(tupla1[-1])
print(tupla1[-2])
print(tupla1[-3])
print(tupla1[-4])
#print(tupla1[-5]) fuera de posicion
lista1[0]="Hola Python desde el CEC-EPN"
tupla1[0]="Hola Python desde el CEC-EPN"
del lista1[3]
del tupla1[3]