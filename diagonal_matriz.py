# -*- coding: utf-8 -*-

n = int(input("Ingrese el tamaño de la matriz identidad: "))

M = []
i = 0

while i < n:
    fila_nueva = [0] * n
    fila_nueva[i] = 1
    M.append(fila_nueva)
    i += 1

for fila in M:
    print(fila)


