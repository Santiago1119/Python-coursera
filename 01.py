# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 12:56:46 2023

@author: Usuario
"""

def convertir_a_tupla(lista:list)->tuple:
    
    tupla_retorno = tuple(lista)
    
    return tupla_retorno

lista = [1, 2, 3]
print(convertir_a_tupla(lista))

    
diccionario_retorno = {}

texto = "Seis suecos sosos secan sesos sin sal, Secan seis sesos los suecos, Salan seis sesos con sal, secan y salan los sesos, que sacan del secadal."

texto = texto.split(' ')

caracteres_permitidos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'á', 'é', 'í', 'ó', 'ú', 'ñ']


for palabra in texto:
    aprobada = True
    for letra in palabra:
        if letra not in caracteres_permitidos:
            aprobada = False
            break
    
    if aprobada == True:
        diccionario_retorno[palabra] = 
        
            
    
    



