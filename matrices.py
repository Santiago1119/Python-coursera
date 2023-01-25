# -*- coding: utf-8 -*-

M = [ [1,0,0], [0,1,0], [0,0,1] ]

#Imprimir elementos individuales
print(M[-1][0])
print(M[-1][-1])
#Recorrer e imprimir filas enteras
for i in range(0, 3):
    print(M[i])
    
#Recorrer e imprimir todos los elementos de la matriz
for j in range(0, 3):
    for i in range(0, 3):
        print(M[j][i])




