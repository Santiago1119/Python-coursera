# -*- coding: utf-8 -*-

import calculadora_indices as calc

def ejecutar_calcular_calorias_reposo(peso: float, altura: float, edad:int, valor_genero:int)->None:
    
    calorias_reposo = calc.calcular_calorias_reposo(peso, altura, edad, valor_genero)
    print(f"Su TMB es: {calorias_reposo}")

def iniciar_aplicacion()->None:
    
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en centimetros: "))
    edad = int(input("Ingrese su edad en años: "))
    valor_genero = int(input("Ingrese el valor de su genero: "))  
    ejecutar_calcular_calorias_reposo(peso, altura, edad, valor_genero)
    
iniciar_aplicacion()
    
