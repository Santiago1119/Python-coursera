# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 11:18:38 2023

@author: Usuario
"""

def hacer_la_vaca (salon:list, vaca:str)->list:
    """
    Verifica si se puede hacer una vaca o no dependiendo de un str que debe 
    indicar "botella o pastel", y la posición del estudiante que más aporto a 
    la vaca

    Parameters
    ----------
    salon : list
        Matriz con los valores aportados por los estudiantes como valores.
    vaca : str
        tipo de regalo que se le dará al profesor.

    Returns
    -------
    list
        Una lista que en su primera posición diga si se puede o no hacer el regalo
        Y en sus dos siguientes posiciones las coordenadas en la matriz del estudiante
        que más aporto a la vaca.

    """
    list_return = ['No Alcanza', 0, 0]
    sumatoria = 0
    est_max = 0
    # for estudiante in salon:
    #     sumatoria += salon[estudiante]
    #     if salon[estudiante] > est_max:
    #         est_max = salon[estudiante]
        
    for i in range(0, len(salon)):
        for j in range(0,len(salon[i])):
            sumatoria += salon[i][j]

            if salon[i][j] > est_max:
                est_max = salon[i][j]
                list_return[1] = i
                list_return[2] = j
    
    if vaca == 'pastel' and sumatoria >= 35000:
        list_return[0] = 'Hay Vaca'
    
    if vaca == 'botella' and sumatoria >= 120000:
        list_return[0] = 'Hay Vaca'

    return list_return

