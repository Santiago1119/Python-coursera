# -*- coding: utf-8 -*-

import pandas as pd

peajes = pd.read_csv("archivo.csv", sep=";")

#Peajes cundinamarca o Tolima
cundinamarca_tolima = peajes[ (peajes['DEP'] == 'Cundinamarca') | (peajes['DEP'] == 'Tolima')]
cundinamarca_tolima = [['NOMBRE', 'DEP']]

#Peajes con tarifa de categoria 6 y 7 superior a 50000
peajes_cat6y7_costosa = peajes[(peajes['CAT6'] > 50000) & (peajes['CAT7'] > 50000)]
peajes_cat6y7_costosa[['NOMBRE', 'CAT6', 'CAT7']]

#Peajes de Atlántico o Valle del Cauca
valle_atlantico = peajes[peajes['DEP'].isin(['Atlántico', 'Valle del Cauca'])]
valle_atlantico = [['NOMBRES', 'DEP']]


