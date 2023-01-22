# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 13:13:27 2023

@author: Usuario
"""

def es_numero_primo(numero: int)->bool:
    primo = True
    
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            
    return primo

print(es_numero_primo(9))
