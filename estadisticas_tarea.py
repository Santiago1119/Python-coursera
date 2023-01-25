# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 19:23:23 2023

@author: Usuario
"""
def calcular_estadisticas_tarea(estudiantes_tareas:dict, nombre_tarea:str)->dict:
    diccionario_retorno = {"mayor":0, "mejor":'', "menor":100, "peor":'', "promedio":0, "cantidad":0, "total":0}
    estudiantes = 0
    
    print()
    
    for estudiante in estudiantes_tareas:
        if nombre_tarea in estudiantes_tareas[estudiante]:
            if estudiantes_tareas[estudiante][nombre_tarea] > diccionario_retorno["mayor"]:
                diccionario_retorno["mayor"] = estudiantes_tareas[estudiante][nombre_tarea]
                diccionario_retorno["mejor"] = estudiante
            if estudiantes_tareas[estudiante][nombre_tarea] < diccionario_retorno["menor"]:
                diccionario_retorno["menor"] = estudiantes_tareas[estudiante][nombre_tarea]
                diccionario_retorno["peor"] = estudiante
            if nombre_tarea in estudiantes_tareas[estudiante]:
                diccionario_retorno["cantidad"] += 1
                diccionario_retorno["total"] += estudiantes_tareas[estudiante][nombre_tarea]
    
            diccionario_retorno['promedio'] += estudiantes_tareas[estudiante][nombre_tarea]
            estudiantes += 1

    diccionario_retorno["promedio"] /= estudiantes

        
    return diccionario_retorno

diccionario = {
    "Roberto": {"Tarea 1": 80, "Tarea 2" : 90},
    "Juan": {"Tarea 1": 70, "Tarea 2" : 80},
    "Pedro": {"Tarea 1": 60, "Tarea 2" : 70},
    "Maria": {"Tarea 1": 50, "Tarea 2" : 60},
    "Jose": {"Tarea 1": 40, "Tarea 2" : 50},
    "Luis": {"Tarea 1": 30, "Tarea 2" : 40},
    "Ana": {"Tarea 1": 20, "Tarea 2" : 30},
    "Sofia": {"Tarea 1": 10, "Tarea 2" : 20},
    "Sara": {"Tarea 1": 0, "Tarea 2" : 10},
    "Lucia": {"Tarea 1": 100}
}

print(calcular_estadisticas_tarea(diccionario, "Tarea 1"))
print(calcular_estadisticas_tarea(diccionario, "Tarea 2"))