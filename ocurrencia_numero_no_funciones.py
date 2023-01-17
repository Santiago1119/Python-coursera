# -*- coding: utf-8 -*-

numero = int(input("Digite el número de 10 cifras: "))

conteo = {}

digito = numero % 10

if digito in conteo:
    conteo[digito] += 1
else:
    conteo[digito] = 1
    
numero = numero // 10

digito = numero % 10

if digito in conteo:
    conteo[digito] += 1
else:
    conteo[digito] = 1
    
numero = numero // 10

digito = numero % 10

if digito in conteo:
    conteo[digito] += 1
else:
    conteo[digito] = 1
    
numero = numero // 10

digito = numero % 10

if digito in conteo:
    conteo[digito] += 1
else:
    conteo[digito] = 1
    
numero = numero // 10

digito = numero % 10

if digito in conteo:
    conteo[digito] += 1
else:
    conteo[digito] = 1
    
numero = numero // 10

digito = numero % 10

if digito in conteo:
    conteo[digito] += 1
else:
    conteo[digito] = 1
    
numero = numero // 10

digito = numero % 10

if digito in conteo:
    conteo[digito] += 1
else:
    conteo[digito] = 1
    
numero = numero // 10

digito = numero % 10

if digito in conteo:
    conteo[digito] += 1
else:
    conteo[digito] = 1
    
numero = numero // 10

digito = numero % 10

if digito in conteo:
    conteo[digito] += 1
else:
    conteo[digito] = 1
    
numero = numero // 10

digito = numero % 10

if digito in conteo:
    conteo[digito] += 1
else:
    conteo[digito] = 1
    
numero = numero // 10

print(conteo)
