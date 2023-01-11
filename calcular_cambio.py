# -*- coding: utf-8 -*-

def calcular_cambio (precio:float)->str:
    monedas_500 = precio // 500
    monedas_200 = (precio % 500) // 200
    monedas_100 = ((precio % 500) % 200) // 100
    monedas_50 = (((precio % 500) % 200 ) % 100) // 50
    
    mensaje = f'{monedas_500},{monedas_200},{monedas_100},{monedas_50}'
    
    return mensaje

