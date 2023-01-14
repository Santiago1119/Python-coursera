# -*- coding: utf-8 -*-

def calcular_IMC(peso: float, altura: float)->float:
    
    return round(peso / altura**2, 2)

def calcular_porcentaje_grasa(peso:float, altura:float, edad:int, valor_genero:float)->float:
    
    imc = calcular_IMC(peso, altura)
    return round(1.2 * imc + 0.23 * edad - 5.4 - valor_genero, 2)
    

def calcular_calorias_reposo(peso:float, altura:float, edad:int, valor_genero:int)->float:
    
    return (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero


def calcular_calorias_en_actividad(peso:float, altura:float, edad:int, valor_genero:float, valor_actividad:float)->float:
    
    tmba = calcular_calorias_reposo(peso, altura, edad, valor_genero) * valor_actividad
    return round(tmba, 2)
    

def consumo_calorias_recomendado_para_adelgazar(peso:float, altura:float, edad:int, valor_genero:float)->str:

    calMin = round(calcular_calorias_reposo(peso, altura, edad, valor_genero) * 0.80,2)
    calMax = round(calcular_calorias_reposo(peso, altura, edad, valor_genero) * 0.85,2)
    
    return f"Para adelgazar es recomendado que consumas entre: {calMin} y {calMax} calorías al día."

