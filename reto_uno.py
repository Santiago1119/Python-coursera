# -*- coding: utf-8 -*-

x1 = input('Por favor ingrese el valor de x1: ')
x2 = input('Por favor ingrese el valor de x2: ')
x3 = input('Por favor ingrese el valor de x3: ')

temporal = x1

x1 = x3
x3 = x2
x2 = temporal

print(f"""
el valor de x1 es: {x1}
el valor de x2 es: {x2}
el valor de x3 es: {x3} """)

