# -*- coding: utf-8 -*-

def mejor_aerolinea(vuelos:dict)->str:
    """
    Dado un diccionario que contienen como clave un código de cada vuelo
    y dentro de cada clave hay otro diccionario con la información de dicho vuelo
    calcula la aerolinea con menor retraso promedio y retorna el nombre de la misma

    Parameters
    ----------
    vuelos : dict
        Diccionario de diccionarios con la información de varios vuelos.

    Returns
    -------
    str
        Nombre de la aerolinea con menor retraso promedio.

    """
    aerolineas = {}
    for vuelo in vuelos:
        aerolinea = vuelos[vuelo]['aerolinea']
        retraso = vuelos[vuelo]['retraso']
        if aerolinea not in aerolineas:
            aerolineas[aerolinea] = {'retraso': retraso, 'vuelos': 1}
        else:
            aerolineas[aerolinea]['retraso'] += retraso
            aerolineas[aerolinea]['vuelos'] += 1
    aerolinea_mas_puntual = ''
    retraso_promedio_minimo = float('inf')

    for aerolinea in aerolineas:
        retraso_promedio = aerolineas[aerolinea]['retraso'] / aerolineas[aerolinea]['vuelos']
        if retraso_promedio < retraso_promedio_minimo:
            aerolinea_mas_puntual = aerolinea
            retraso_promedio_minimo = retraso_promedio

    return aerolinea_mas_puntual
