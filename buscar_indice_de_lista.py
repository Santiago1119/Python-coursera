# -*- coding: utf-8 -*-

def buscar_elemento (entrada: list, buscado: int)-> int:
    posicion = 0

    for num in range(0, len(entrada)):
        if buscado == entrada[num]:
            posicion = num
            break;

    if posicion == 0:
        posicion = -1    
    
    return posicion

