# -*- coding: utf-8 -*-

'''
Sumatoria de i = 1 hasta 1000 de i
'''

sumatoria = 0
i = 1
iteraciones = 0

while i <= 1000:
    iteraciones += 1
    sumatoria += i
    i += 1
    
print("El resultado de la sumatoria es: ", sumatoria)
print("El numero de iteraciones fue: ", iteraciones)
print("El valor de i es: ", i)



