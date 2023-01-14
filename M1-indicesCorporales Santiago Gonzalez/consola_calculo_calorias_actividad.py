# -*- coding: utf-8 -*-

import calculadora_indices as calc

def ejecutar_calcular_calorias_en_actividad(peso: float, altura: float, edad:int, valor_genero:int, valor_actividad:float)->None:
    
    calorias_en_actividad = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
    print(f"Su TMBA es: {calorias_en_actividad}")

def iniciar_aplicacion()->None:
    
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en centimetros: "))
    edad = int(input("Ingrese su edad en años: "))
    valor_genero = int(input("Ingrese el valor de su genero: "))
    valor_actividad = float(input("Ingrese el valor de la actividad fisica: "))
    ejecutar_calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
    
iniciar_aplicacion()
    