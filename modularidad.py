# -*- coding: utf-8 -*-
def es_divisible (n: int, d: int)->int:
    valor_retorno = 0
    if d == 0:
        valor_retorno = 0
    elif n % (2 * d) == 0:
        valor_retorno = 2
    elif n % d == 0 and n % (2*d) != 0:
        valor_retorno = 1
    else:
        valor_retorno = 0
        
    return valor_retorno
