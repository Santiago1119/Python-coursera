# -*- coding: utf-8 -*-

def contar(num:int, diccionario:dict)->dict:
    digito = num % 10
    
    if digito in diccionario:
        diccionario[digito] += 1
    else:
        diccionario[digito] = 1
        
    return diccionario

numero = int(input("Ingrese el numero de 10 cifras: "))
conteo = {}

conteo = contar(numero, conteo)
numero //= 10

conteo = contar(numero, conteo)
numero //= 10

conteo = contar(numero, conteo)
numero //= 10

conteo = contar(numero, conteo)
numero //= 10

conteo = contar(numero, conteo)
numero //= 10

conteo = contar(numero, conteo)
numero //= 10

conteo = contar(numero, conteo)
numero //= 10

conteo = contar(numero, conteo)
numero //= 10

conteo = contar(numero, conteo)
numero //= 10

conteo = contar(numero, conteo)
numero //= 10

print(conteo)
