# -*- coding: utf-8 -*-

def calcular_factorial(n:int)->int:
    terminar = False
    factorial = 1
    
    while terminar == False:
        if n == 0:
            terminar = True
        else:
            factorial *= n
            n -= 1
            
    return factorial

numero = int(input("Ingrese un número entero positivo: "))

while numero < 0:
    print("No se permiten números negativos")
    numero = int(input("Ingrese un número entero positivo: "))
    
print(f"{numero}! es igual a {calcular_factorial(numero)}")