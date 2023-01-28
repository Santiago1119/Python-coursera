# -*- coding: utf-8 -*-

def contar_votos_estado(votos:list, estado_interes:str)->tuple:
    """
    calcula la cantidad de votos para los dos candidatos

    Parameters
    ----------
    votos : list
        Lista de tuplas con la información de los votantes.
    estado_interes : str
        Estado del cual se quiere recolestar numero de votos que tuvo cada
        candidato.

    Returns
    -------
    tuple
        Tupla con la cantidad de votos de trump y la cantidad de votos de biden
        respectivamente.

    """
    votos_trump = 0
    votos_biden = 0

    for voto_actual in votos:
        id_voto, candidato, estado, condado = voto_actual
        
        if estado == estado_interes:
            if candidato == 'Donald Trump':
                votos_trump += 1
            else:
                votos_biden += 1
                
    return (votos_trump, votos_biden)

def contar_votos_por_estado(votos:list, estados:tuple)->dict:
    total_estado = {}
    
    for i in range(len(estados)):
        estado_actual = estados[i]
        votos_estado_actual = contar_votos_estado(votos, estado_actual)
        total_estado[estado_actual] = votos_estado_actual
        
    
    return total_estado

