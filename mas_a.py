# -*- coding: utf-8 -*-

def mas_a(c1:str, c2:str, c3:str, c4:str)->str: 
    letra = 'a' 
    tam_1 = c1.lower().count(letra)
    tam_2 = c2.lower().count(letra)
    tam_3 = c3.lower().count(letra)
    tam_4 = c4.lower().count(letra)
    
    cadena_mas = c1
    cantidad_mas = tam_1
    
    if tam_2 > cantidad_mas:
        cadena_mas = c2
    if tam_3 > cantidad_mas:
        cadena_mas = c3
    if tam_4 > cantidad_mas:
        cadena_mas = c4
    
    return cadena_mas
    

print(mas_a('Acampar', 'fresa', 'carro', 'manzana'))