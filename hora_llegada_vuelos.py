# -*- coding: utf-8 -*-

def calcular_hora_llegada(hora_salida:int, minutos_salida:int,
                           seg_salida:int, horas_duracion: int,
                           minutos_duracion:int, seg_duracion:int)->str:
   
    """
    calcula la hora de llegada del vuelo
    
    Parameters
    ----------
    hora_salida : int
        Entero con la hora salida en formato HH:MM:SS
    minutos_salida : int
        Entero con los minutos de salida en formato HH:MM:SS
    seg_salida : int
        Entero con los segundos de salida en formato HH:MM:SS
    hora_duracion: int
        Entero con las horas de duración del vuelo
    minutos_duracion: int
        Entero con los minutos de duración del vuelo
    seg_duracion : int
        Entero con los segundos de duración del vuelo
    Returns
    -------
    str
        Un string con la hora de llegada del vuelo

    """
    
    minutos, segundos = divmod(seg_salida + seg_duracion, 60)
    horas, minutos = divmod(minutos + (minutos_salida + minutos_duracion), 60)
    horas += hora_salida + horas_duracion
    
    return f'{horas:0>2d}:{minutos:0>2d}:{segundos:0>2d}'


def hora_llegada_vuelos(info_vuelos:list)->list:
    """
    calcula la hora de llegada de todos los vuelos dentro de la lista
    
    Parameters
    ----------
    info_vuelos : list
        Una lista con todos los vuelos dentro de diccionarios

    Returns
    -------
    list
        Una lista con la hora de llegada de todos los vuelos.

    """
    
    llegadas = []
    
    for vuelo in info_vuelos:
        salida = vuelo['tiempo_salida']
        duracion = vuelo['duracion']
        
        partes_salida = salida.split(':')
        hora_salida = int(partes_salida[0])
        minutos_salida = int(partes_salida[1])
        segundos_salida = int(partes_salida[2])
        
        partes_duracion = duracion.split(':')
        hora_duracion = int(partes_duracion[0])
        minutos_duracion = int(partes_duracion[1])
        segundos_duracion = int(partes_duracion[2])
        
        tiempo_llegada = calcular_hora_llegada(hora_salida, minutos_salida, segundos_salida, hora_duracion, minutos_duracion, segundos_duracion)
        
        dict_llegada = {"tiempo_llegada":tiempo_llegada}
        llegadas.append(dict_llegada)
        
    return llegadas

vuelos = [{'tiempo_salida': '08:11:45', 'duracion': '2:54:20'},
          {'tiempo_salida': '11:48:10', 'duracion': '2:11:58'},
          {'tiempo_salida': '12:00:10', 'duracion': '0:55:15'},
          {'tiempo_salida': '14:55:10', 'duracion': '3:20:00'},
          {'tiempo_salida': '17:15:20', 'duracion': '4:05:11'},]
    
print(hora_llegada_vuelos(vuelos))
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    