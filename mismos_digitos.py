# -*- coding: utf-8 -*-

def mismos_digitos(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    s = 0
    n = 0
    i = 0
    f = 0


    valor_retorno = False

    while i < len(num1):
        if num1[i] in num2:
            s += 1
        else:
            n += 1
        i += 1
    
    while f < len(num2):
        if num2[f] in num1:
            s += 1
        else:
            n += 1
        f += 1

    if n == 0:
        valor_retorno = True
    
    return valor_retorno

print(mismos_digitos(2, 8))
