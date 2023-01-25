# -*- coding: utf-8 -*-

import random

def calcular_suma_matriz(matriz:list)->int:
    """
    Calcula la suma de todos los elementos de una matriz

    Parameters
    ----------
    matriz : list
        La matriz de la cual queremos saber la suma de todos sus elementos.

    Returns
    -------
    int
        Sumatoria de todos los elementos de la matriz.

    """
    suma = 0
    
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[0])):
            suma += matriz[i][j]
            
    return suma


def calcular_fila_suma(matriz:list, fila:list)->int:
    """
    Calcula la suma de una una fila de la matriz dada por parametro

    Parameters
    ----------
    matriz : list
        Matriz con una fila de la que queremos saber la sumatoria.
    fila : list
        La fila de la matriz de la cual queremos saber la sumatoria.

    Returns
    -------
    int
        Sumatoria de la fila de la matriz pasada por parametro.

    """
    suma = 0
    
    for num_col in range(0, len(matriz[0])):
        suma += matriz[fila][num_col]
        
    return suma

def calcular_columna_suma(matriz:list, columna:int)->int:
    """
    Calcula la suma de una columna de la matriz pasada por parametro

    Parameters
    ----------
    matriz : list
        Matriz con una columna de la que queremos saber la sumatoria.
    columna : int
        Numero de columna de la que queremos saber la sumatoria.

    Returns
    -------
    int
        Sumatoria de una columna de la matriz.

    """
    suma = 0
    
    for fila in matriz:
        suma += fila[columna]
        
    return suma

def calcular_valor_negativo(matriz:list)->bool:
    """
    Calcula si existe algún valor negativo en la matriz

    Parameters
    ----------
    matriz : list
        Matriz de la cual queremos saber si existe algun valor negativo.

    Returns
    -------
    bool
        True si hay valores negativos False si no.

    """
    
    encontrado = False
    
    i = 0
    j = 0
    
    while i < len(matriz) and not encontrado:
        while j < len(matriz[0]) and not encontrado:
            if matriz[i][j] < 0:
                encontrado = True
        
            j += 1
        i += 1
    
    return encontrado 


def fila_mas_ceros(matriz:list)->int:
    """
    

    Parameters
    ----------
    matriz : list
        DESCRIPTION.

    Returns
    -------
    int
        DESCRIPTION.

    """
    fila_mas = 0
    max_ceros = 0
    
    for i in range(0, len(matriz)):
        cant_ceros = 0
        for j in range(0, len(matriz[0])):
            if matriz[i][j] == 0:
                cant_ceros += 1
            
        if cant_ceros > max_ceros:
            max_ceros = cant_ceros 
            fila_mas = i
            
    return fila_mas



M = []

for i in range(5):
    fila = []
    for j in range(5):
        numero = random.randint(-2, 5)
        fila.append(numero)
    M.append(fila)
    
print("Matriz: ")
for fila in M:
    print(fila)
    
print("\nResultados:\n")

print("Suma matriz: ", calcular_suma_matriz(M))
print("Suma fila: ", calcular_fila_suma(M, 1))
print("Suma columna: ", calcular_columna_suma(M, 4))
print("Existe negativos: ", calcular_valor_negativo(M))
print("Fila mas ceros: ", fila_mas_ceros(M))


    
        
    
        

            












