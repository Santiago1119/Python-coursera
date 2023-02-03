# -*- coding: utf-8 -*-

import pandas as pd

def calcular_habitantes_por_puesto(df_poblacion, df_universidades):
    df_universidades = df_universidades.groupby('country').sum()
    df_universidades = df_universidades.reset_index()
    df_poblacion = df_poblacion.merge(df_universidades, left_on='Pais', right_on='country')
    df_poblacion['habitantes_por_puesto'] = df_poblacion['Poblacion'] / df_poblacion['num_students']
    df_poblacion = df_poblacion.sort_values(by='habitantes_por_puesto')
    df_poblacion = df_poblacion[['Pais', 'habitantes_por_puesto']]
    df_poblacion['habitantes_por_puesto'] = df_poblacion['habitantes_por_puesto'].round(1)
    return df_poblacion

