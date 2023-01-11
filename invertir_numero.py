# -*- coding: utf-8 -*-
def invertir_numero(numero:float)->float:
    unidades = numero%10
    numero //= 10
    decenas = numero%10
    numero //= 10
    centenas = numero%10
    numero //= 10
    millares = numero%10
    numero //= 10
    
    inversion = (unidades*1000)+(decenas*100)+(centenas*10)+(millares)
    
    return inversion

print(invertir_numero(4586))
