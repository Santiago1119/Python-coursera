# -*- coding: utf-8 -*-
import calculadora_indices as calc

def ejecutar_consumo_calorias_recomendado_para_adelgazar(peso: float, altura: float, edad:int, valor_genero:float)->None:
    
    mensaje_consumo_calorias = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
    print(mensaje_consumo_calorias)

def iniciar_aplicacion()->None:
    
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en centimetros: "))
    edad = int(input("Ingrese su edad en años: "))
    valor_genero = float(input("Ingrese el valor de su genero: "))
    ejecutar_consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
    
iniciar_aplicacion()

