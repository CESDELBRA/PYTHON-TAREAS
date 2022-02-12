# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 08:14:43 2019

@author: CEC
"""

seq = ['data','salt' ,'dairy','cat', 'dog']

print(list(filter(lambda word: word[1]=='a',seq)))
