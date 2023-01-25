# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 18:26:35 2023

@author: Usuario
"""

def total_goles(tablero_goles:list)->int:
    total = 0
    
    for i in range(len(tablero_goles)):
        for j in range(len(tablero_goles[0])):
            casilla = tablero_goles[i][j]
            if casilla >= 0:
                total += casilla
                
    return total

def partidos_jugados(tablero_goles:list)->int:
    partidos = 0
    
    for i in range(len(tablero_goles)):
        for j in range(i+1, len(tablero_goles[0])):
            if tablero_goles[i][j] >= 0:
                partido += 1
                
    return partidos

def equipo_mas_goleador(tablero_goles:list, equipos:dict)->str:
    max_goles = 0
    indice_goleador = 0
    
    for i in range(len(tablero_goles)):
        goles_actual = 0
        for j in range(len(tablero_goles[0])):
            if tablero_goles[i][j] > 0:
                goles_actual += tablero_goles[i][j]
        
        if goles_actual > max_goles:
            max_goles = goles_actual
            indice_goleador = i
            
    nom_equipo = ""
    
    for eq in equipos:
        if equipos[eq] == indice_goleador:
            nom_equipo= eq
            
    return nom_equipo