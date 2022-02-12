# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 18:35:46 2022

@author: Usuario
"""

file=open("C:/Users/Usuario/PythonCEC-220201/220211/devices.txt")
for a in file:
    a=a.strip("Cisco")
    print(a)
file.close()