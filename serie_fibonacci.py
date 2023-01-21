# -*- coding: utf-8 -*-


def sucesion_fibonacci(cantidad_numeros:int)->str:

    lista = []
    numero_uno = 0
    numero_dos = 1

    if cantidad_numeros > 1:
        lista.append(str(numero_uno))
        lista.append(str(numero_dos))

        while len(lista) < cantidad_numeros:
            numero_tres = numero_uno + numero_dos
            lista.append(str(numero_tres))
            numero_uno = numero_dos
            numero_dos = numero_tres
            
        cadena = ",".join(lista)
    elif cantidad_numeros > 0:
        lista.append(str(numero_uno))
        cadena = ",".join(lista)

    return cadena

