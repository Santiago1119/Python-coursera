# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 14:42:51 2023

@author: Usuario
"""

def convertir_a_tupla(lista:list)->tuple:
    
    tupla_retorno = tuple(lista)
    
    return tupla_retorno




caracteres_permitidos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'á', 'é', 'í', 'ó', 'ú']
texto = 'Muchos años después frente al pelotón de fusilamiento el coronel Aureliano Buendía había de recordar aquella tarde remota en que su padre lo llevó a conocer el hielo'

texto = texto.lower()

for letra in texto:
    if letra not in caracteres_permitidos:
        texto = texto.replace(letra, ' ')
    
lista = texto.split(' ')

print(lista)


diccionario = {}

for palabra in lista:
    
    lista_salida = []
    comprobada = True
    
    for letra in palabra:
        if letra not in caracteres_permitidos:
            comprobada = False
            
    if comprobada == True:
        diccionario[palabra] = [lista.count(palabra), texto.find(palabra) , texto.rfind(palabra)]
    else:
        diccionario[palabra] = [lista.count(palabra), 3]
    
for palabra in diccionario:
    lista = diccionario[palabra]
    
    diccionario[palabra] = convertir_a_tupla(lista)
    

# print(diccionario)