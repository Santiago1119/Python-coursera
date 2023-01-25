# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 13:21:19 2023

@author: Usuario
"""


def promedio_fila (matriz:list, fila:int)->float:
    """
    Saca el promedio de una fila de una matriz, si el valor es extraño retorna -1
    cuando hay un 0 significa que no hay estudiante en esa posición, si no hay estudiantes
    retorna 0 de lo contrario retorna el promedio

    Parameters
    ----------
    matriz : list
        DESCRIPTION.
    fila : int
        DESCRIPTION.

    Returns
    -------
    float
        DESCRIPTION.

    """
    valor_retorno = 0
    sumatoria = 0
    estudiantes_fila = 0

    if fila > len(matriz) or fila < 1:
        valor_retorno = -1

    else:  
        for estudiante in range(len(matriz[fila - 1])):
            if matriz[fila-1][estudiante] != 0:
                sumatoria += matriz[fila - 1][estudiante]
                estudiantes_fila += 1
        if estudiantes_fila == 0:
            valor_retorno = 0
        else:
            valor_retorno = round(sumatoria/estudiantes_fila, 2)

    return valor_retorno


