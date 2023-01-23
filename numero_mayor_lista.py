# -*- coding: utf-8 -*-

def encontrar_mayor (entrada: list)-> int:
    numero = 0

    for i in range(0, len(entrada)):
        if entrada[i] > numero:
            numero = entrada[i]
    
    if entrada == []:
        numero = -1

    return numero


