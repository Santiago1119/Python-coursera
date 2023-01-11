# -*- coding: utf-8 -*-

def calcular_BMI (peso_lb:float, altura_inch:float )->float:
    
    peso_lb = peso_lb * 0.45
    
    altura_inch = altura_inch * 0.025
    
    bmi = peso_lb / altura_inch ** 2
    
    return round(bmi, 2)

peso_lb = float(input('ingrese su peso en libras: '))
altura_inch = float(input('ingrese su altura en pulgadas: '))

print(calcular_BMI(peso_lb, altura_inch))
