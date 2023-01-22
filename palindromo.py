# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 12:27:41 2023

@author: Usuario
"""


def es_palindromo(cadena: str)->bool:
    palindromo = False
    sin_espacios = cadena.replace(" ", "")
    en_minus = sin_espacios.lower()

    i = 0
    j = len(en_minus) - 1
    
    while i < j and en_minus[i] == en_minus[j]:
        i += 1
        j -= 1
    
    if i == j:
        palindromo = True
    
    return palindromo

print(es_palindromo("Isaac no ronca asi"))
print(es_palindromo("Sometamos o matemos"))
print(es_palindromo("Hola mundo"))