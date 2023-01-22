# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 13:20:09 2023

@author: Usuario
"""

def contar_caracteres_repetidos(cadena: str)->int:
    caracteres_diferentes = {}
    numero_caracteres_diferentes = 0

    for caracter in cadena:
        if caracter in caracteres_diferentes:
            caracteres_diferentes[caracter] += 1
        else:
            caracteres_diferentes[caracter] = 1

    for caracter in caracteres_diferentes:
        if caracteres_diferentes[caracter] >= 2:
            numero_caracteres_diferentes += 1
        
    return numero_caracteres_diferentes
    
