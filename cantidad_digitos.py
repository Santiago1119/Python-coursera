# -*- coding: utf-8 -*-


def cantidad_digitos(numero: int)->int:
    digitos = 0
    terminar = False
    
    while (terminar == False):
        if numero == 0:
            terminar = True
        else:
            digitos += 1
            numero //= 10
            
    return digitos
    
num = int(input("Ingrese un número entero: "))
digitos = cantidad_digitos(num)
print(f"La cantidad de dígitos del número es {digitos}")
