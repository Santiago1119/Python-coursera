# -*- coding: utf-8 -*-

def redondear_nota(nota: float)->float:
    """
    Redondea la nota final

    Parameters
    ----------
    nota : float
        Recibe número flotante como parametro el cual redondea.

    Returns
    -------
    float
        Retorna el número redondeado.

    """
    nota_retorno = 1.5
    if nota >= 4.5:
        nota_retorno = 5.0
    elif nota >= 3.5 and nota < 4.5:
        nota_retorno = 4.0
    elif nota >= 2.5 and nota < 3.5:
        nota_retorno = 3.0
    
    return nota_retorno

def calcular_definitivas(estudiantes: list)->list:
    """
    Redondea todas las notas definitivas que se le pasan como parametro
    dentro de una lista en diccionarios, cada diccionario tiene "nombre" y "definitiva"

    Parameters
    ----------
    estudiantes : list
        La lista con todos los nombre y notas de los estudiantes.

    Returns
    -------
    list
        La lista con la nota final redondeada.

    """
    l_retorno = []

    for i in range(0, len(estudiantes)):
        nota_r = redondear_nota(estudiantes[i]["nota"])
        estudiantes[i]["nota"] = nota_r
        l_retorno.append(estudiantes[i])

    return l_retorno