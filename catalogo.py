# -*- coding: utf-8 -*-

def producto_mas_barato(catalogo:dict)->str:
    """
    Retorna el producto más barato exceptuando algunas condiciones

    Parameters
    ----------
    catalogo : dict
        diccionario que contiene los productos, las llaves poseen el nombre 
        del producto y el valor posee el precio.

    Returns
    -------
    str
        String con el nombre del producto más economico del diccionario.

    """

    producto_barato = None
    llaves = catalogo.keys()
    llaves_ordenadas = sorted(llaves)
    diccionario_ordenado = {}

    for llave in llaves_ordenadas:
        diccionario_ordenado[llave] = catalogo[llave]

    if len(catalogo) > 0:
        producto_barato = min(diccionario_ordenado, key=diccionario_ordenado.get)
    
    if len(catalogo) == 0:
        producto_barato = "No hay productos para escoger"

    if len(catalogo) > 0:
        if diccionario_ordenado[producto_barato] > 10000:
            producto_barato = None


    return producto_barato

