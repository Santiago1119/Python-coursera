# -*- coding: utf-8 -*-
"""
Solicitar datos al usuario usando While
"""

from math import sqrt

x = float(input("Digite un número positivo: "))
          
while x < 0:
    print("No puede ingresar numeros negativos")
    x = float(input("Digite un número positivo: "))


print(f"La raíz cuadrada de {x} es {sqrt(x)}")
