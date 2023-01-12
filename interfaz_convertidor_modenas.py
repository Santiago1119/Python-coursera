# -*- coding: utf-8 -*-

import libreria as lb

def ejecutar_convertir_a_dolares(trm: float)->None:
    pesos = float(input("Ingrese la cantidad de pesos: "))
    dolares = lb.convertir_a_dolares(pesos, trm)
    print(pesos, "pesos son", round(dolares,2), "dolares")

def ejecutar_convertir_a_pesos(trm: float)->None:
    dolares = float(input("Ingrese la cantidad de dolares: "))
    pesos = lb.convertir_a_pesos(dolares, trm)
    print(dolares, "dólares son", round(pesos, 0), "pesos")
    
def iniciar_aplicacion()->None:
    trm = float(input("Ingrese la TRM: "))
    ejecutar_convertir_a_dolares(trm)
    ejecutar_convertir_a_pesos(trm)

iniciar_aplicacion()
