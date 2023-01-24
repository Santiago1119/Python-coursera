# -*- coding: utf-8 -*-

def producto_mas_costoso (carrito_compras:dict)->str:
    """
    Dado un diccionario retorna el producto más costoso del carro, si hay dos
    productos con el mismo precio retorna el menor alfabeticamente

    Parameters
    ----------
    carrito_compras : dict
        diccionario con los productos como llaves y los precios como valores.

    Returns
    -------
    str
        retorna un string con el producto más costoso del carro de compra y si
        el diccionario esta vacio retorna "No hay productos en el carrito".

    """
    
    producto_costoso = "No hay productos en el carrito"
    keys = carrito_compras.keys()
    key_order = sorted(keys)
    dic_order = {}

    for key in key_order:
        dic_order[key] = carrito_compras[key]

    if len(carrito_compras) > 0:
        producto_costoso = max(dic_order, key = dic_order.get)

    return producto_costoso
