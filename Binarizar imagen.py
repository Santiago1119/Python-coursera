# -*- coding: utf-8 -*-

def binarizar_imagen(matriz, umbral):
    """
    Este ejercicio consiste en llevar los valores de una matriz que  representa una imagen a dos colores: negro y blanco. En cada posición de  la matriz que representa la imagen, hay una tupla de 3 flotantes entre 0 y 1 que representan los valores R, G y B del píxel. 

    Para ello, se establece un umbral (valor entre 0 y 1) y los  píxeles con promedio de color que  son iguales o mayores al  umbral se cambian a blanco (todos los valores de la tupla en 1) y los que están por  debajo se cambian a negro (todos los valores de la tupla en 0).

    Parameters
    ----------
    matriz : TYPE
        Matriz con los valores de cada pixel.
    umbral : TYPE
        Umbral en el que se convertiran los colores a blanco.

    Returns
    -------
    matriz : TYPE
        la imagen a blanco y negro.

    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if sum(matriz[i][j])/3 >= umbral:
                matriz[i][j] = [1, 1, 1]
            else:
                matriz[i][j] = [0, 0, 0]

    return matriz

