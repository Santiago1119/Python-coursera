# -*- coding: utf-8 -*-

def picas_y_fijas (numero_secreto:int, intento:int)->dict:
    picas = 0
    fijas = 0
    salida = {"PICAS": 0, "FIJAS": 0}

    numero_secreto = str(numero_secreto)
    intento = str(intento)

    if numero_secreto[0] == intento[0]:
        salida["FIJAS"] += 1
    elif numero_secreto[0] in intento:
        salida["PICAS"] += 1

    if numero_secreto[1] == intento[1]:
        salida["FIJAS"] += 1
    elif numero_secreto[1] in intento:
        salida["PICAS"] += 1

    if numero_secreto[2] == intento[2]:
        salida["FIJAS"] += 1
    elif numero_secreto[2] in intento:
        salida["PICAS"] += 1

    if numero_secreto[3] == intento[3]:
        salida["FIJAS"] += 1
    elif numero_secreto[3] in intento:
        salida["PICAS"] += 1
    
    return salida

