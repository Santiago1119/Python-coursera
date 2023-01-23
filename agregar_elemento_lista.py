# -*- coding: utf-8 -*-

def insertar_ordenado (lista_ordenada:list, cadena: str)->list:
    """
    Agrega un elemento a una lista ordenada,
    y devuelve la lista ordenada con el nuevo elemento dentro
    
    Parameters
    ----------
    lista_ordenada : list
        Una lista ordenada en orden alfabetico.
    cadena : str
        Un string que será agregado a la lista.

    Returns
    -------
    list
        La lista ordenada con el nuevo elemento incluido.

    """
    i = 0
    
    while i < len(lista_ordenada) and cadena > lista_ordenada[i]:
        
        i += 1
        
    lista_ordenada.insert(i, cadena)
    
    return lista_ordenada


def ordenar_lista(lista_desordenada: list)->list:
    """
    Ordena una lista desordenada 
    
    Parameters
    ----------
    lista_ordenada : list
        Una lista ordenada en desorden.
    Returns
    -------
    list
        La lista ordenada

    """
    
    ordenada = []
    
    for cadena in lista_desordenada:
        ordenada = insertar_ordenado(ordenada, cadena)
        
    return ordenada

lista = ["tanque", "avion", "moto", "automovil", "barco", "diligencia"]

orden = ordenar_lista(lista)

print(orden)
    
    
    
