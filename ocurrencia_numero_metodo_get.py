# -*- coding: utf-8 -*-

def contar(num:int, diccionario:dict)->int:
    digito = num % 10
    
    diccionario[digito] = diccionario.get(digito, 0) + 1
        
    return num // 10 

numero = int(input("Ingrese el numero de 10 cifras: "))
conteo = {}

numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)

print(conteo)


