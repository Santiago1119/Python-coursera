# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 14:42:51 2023

@author: Usuario
"""

caracteres_permitidos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'á', 'é', 'í', 'ó', 'ú', 'ñ']
texto = "Muchos años después, frente al pelotón de fusilamiento, el coronel Aureliano Buendía había de recordar aquella tarde remota en que su padre lo llevó a conocer el hielo."

# for i in range(len(texto)):
#     print(f"indice: {i} letra: {texto[i]}")

def convertir_a_tupla(lista:list)->tuple:
    
    tupla_retorno = tuple(lista)
    
    return tupla_retorno


def primer_palabra(texto:str, palabra:str)->int:
    texto += ' '
    
    palabra += ' '
    
    return texto.index(palabra)
    
def ultima_palabra(texto:str, palabra:str)->int:
    texto += ' '

    palabra += ' '

    return texto.rindex(palabra)


def analizar_texto(texto: str, caracteres_permitidos: list) -> dict:
    diccionario = {}
    texto = texto.lower()
    
    texto = texto.replace(',', '')
    
    for letra in texto:
        if letra not in caracteres_permitidos:
            texto = texto.replace(letra, ' ')
    if len(texto) <= 0 or len(caracteres_permitidos) <= 1:
        diccionario = diccionario
    else:
        
        palabras_texto = texto.split(' ')
        
        
        for palabra in palabras_texto:
            
            
            diccionario[palabra] = [palabras_texto.count(palabra), primer_palabra(texto, palabra), ultima_palabra(texto, palabra)]
            
            diccionario[palabra] = convertir_a_tupla(diccionario[palabra])

    return diccionario

print(analizar_texto(texto, caracteres_permitidos))