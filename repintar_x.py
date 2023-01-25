# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 18:45:17 2023

@author: Usuario
"""

def pintar_x(matriz, operacion):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j or i + j == len(matriz) - 1:
                if operacion == '+':
                    matriz[i][j] += matriz[i][j]
                elif operacion == '-':
                    matriz[i][j] -= matriz[i][j]
                elif operacion == '*':
                    matriz[i][j] *= matriz[i][j]
                elif operacion == '/':
                    matriz[i][j] /= matriz[i][j]
    return matriz