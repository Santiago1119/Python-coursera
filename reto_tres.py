# -*- coding: utf-8 -*-

capital = float(input('Ingrese el capital en pesos: '))
interest = float(input('Ingrese la tasa de interes: '))
time = int(input('Ingrese el plazo de años que desea esperar: '))

result = capital*(1+ interest/100)**time

print(f'su dinero en {time} años será {round(result, 3)} pesos')

