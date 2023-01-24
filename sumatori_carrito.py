# -*- coding: utf-8 -*-

def valor_carrito_compras (carrito_compras:dict)->float:
    """
    Recibe un diccionario como parametro y retorna el valor total del carrito

    Parameters
    ----------
    carrito_compras : dict
        Diccionario con los productos como llaves y los precios como valores

    Returns
    -------
    float
        El precio total de todos los productos que se desean comprar.

    """
    sumatoria = 0

    for valor in carrito_compras:
        sumatoria += carrito_compras[valor]

    return sumatoria
