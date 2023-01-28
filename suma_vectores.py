# -*- coding: utf-8 -*-


def suma_vectorial(vector_1:tuple, vector_2:tuple)->tuple:
    """
    Suma de dos vectores

    Parameters
    ----------
    vector_1 : tuple
        tupla con los 3 valores del vector uno.
    vector_2 : tuple
        tupla con los 3 valores del vector dos.

    Returns
    -------
    tuple
        tupla con la suma de los vectores.

    """
    
    suma_1 = vector_1[0] + vector_2[0]
    suma_2 = vector_1[1] + vector_2[1]
    suma_3 = vector_1[2] + vector_2[2]

    tupla_retorno = (suma_1, suma_2, suma_3)

    return  tupla_retorno