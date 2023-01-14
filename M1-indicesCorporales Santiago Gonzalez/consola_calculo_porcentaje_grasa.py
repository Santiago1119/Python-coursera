# -*- coding: utf-8 -*-

import calculadora_indices as calc

def ejecutar_calcular_porcentaje_grasa(peso:float, altura:float, edad:int, valor_genero:float)->None:
    porcentaje_grasa = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
    print(f"Su porcentaje de grasa es: {porcentaje_grasa}")
    
def iniciar_aplicacion()->None:
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    edad = int(input("Ingrese su edad en años: "))
    valor_genero = float(input("Ingrese el valor de su genero: "))  
    ejecutar_calcular_porcentaje_grasa(peso, altura, edad, valor_genero)

iniciar_aplicacion()

