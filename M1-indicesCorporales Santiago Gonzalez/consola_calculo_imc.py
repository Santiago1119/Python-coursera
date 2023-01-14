# -*- coding: utf-8 -*-

import calculadora_indices as calc

def ejecutar_calcular_IMC (peso: float, altura: float)->None:
    imc = calc.calcular_IMC(peso, altura)
    print(f'Su IMC es de: {imc}')
    

def iniciar_aplicacion ()->None:
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    ejecutar_calcular_IMC(peso, altura)
    
iniciar_aplicacion()