# -*- coding: utf-8 -*-

def verificar_materias(nombre_materia:str)->int:
    contador_materias = 0
    if nombre_materia.count('programacion') != 0:
        contador_materias += 1
    if nombre_materia.count('matematica') != 0:
        contador_materias += 1
    if nombre_materia.count('filosofia') != 0:
        contador_materias += 1   
    if nombre_materia.count('literatura') != 0:
        contador_materias += 1
    
    return contador_materias

def conteo_de_materias (nombre_materia_1:str, nombre_materia_2:str, nombre_materia_3:str)->int:
    materias_buenas = 0

    if verificar_materias(nombre_materia_1) > 0:
        materias_buenas += 1
    if verificar_materias(nombre_materia_2) > 0:
        materias_buenas += 1
    if verificar_materias(nombre_materia_3) > 0:
        materias_buenas += 1
    
    return materias_buenas