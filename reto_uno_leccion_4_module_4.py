# -*- coding: utf-8 -*-

import pandas as pd

def mejores_estudiantes(df):
    df['promedio'] = df.mean(axis=1)
    df = df.sort_values(by='promedio', ascending=False)
    df = df.iloc[:int(len(df)*0.25)]
    df = df[['nombre', 'promedio']]
    df['promedio'] = df['promedio'].round(2)
    return df
