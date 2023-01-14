# -*- coding: utf-8 -*-

def calcular_precio_pasaje(temporada_alta:bool, compania:str, edad:int, estudiante:bool)->int:
    
    precio = 5000000
    variaciones = 0
    seguro = False
    
    if compania == "ALAS":
        if temporada_alta:
            variaciones += 0.3
        else:
            if edad >= 18 and estudiante:
                variaciones -= 0.1
    elif compania == "VOLAR":
        if temporada_alta:
            variaciones += 0.2
        if edad > 60:
            seguro = True
    
    if edad < 18:
        variaciones -= 0.5
    
    precio *= (1+variaciones)

    if seguro:
        precio += 100000
        
    return round(precio)
