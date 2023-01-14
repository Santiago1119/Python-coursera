# -*- coding: utf-8 -*-

def rango_numero (x:int)->int:
    
    """
    Esta función recibe como parametro un entero
    
    Si el numero es negativo retorna -1
    Si el numero es mayor a 0 y menor a 1000 retorna 0
    Si el numero es mayor o igual a 1000 y menor o igual a 10000 retorna 1
    Si es mayor a 10000 retorna 2
    
    """
    
    valor_retorno = 0
    
    if x < 0 :
        valor_retorno = -1
    elif x > 0 and x < 1000 :
        valor_retorno = 0
    elif x >= 1000 and x <= 10000:
        valor_retorno = 1
    else:
        valor_retorno = 2
    
    return valor_retorno

print(rango_numero())