# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

def depurar_partidos(df):
    
    df['resultado'] = np.where(df['goles_local'] > df['goles_visitante'], df['local'], np.where(df['goles_local'] < df['goles_visitante'], df['visitante'], 'empate'))
    df['goles_local'] = df['goles_local'].fillna(0)
    df['goles_visitante'] = df['goles_visitante'].fillna(0)
    df = df[df['local'] != df['visitante']]
    
    return df
