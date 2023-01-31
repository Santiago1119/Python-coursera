# -*- coding: utf-8 -*-

import pandas as pd

diccionario_serie_uno = {1:2, 2:4, 3:8, 4:16, 5:32}
diccionario_serie_dos = {1:1, 2:8, 3:27, 4:64, 5:125}
diccionario_serie_tres = {1:1, 2:16, 3:81, 4:256, 5:625, 6:1296}

serie_uno = pd.Series(diccionario_serie_uno)
serie_dos = pd.Series(diccionario_serie_dos)
serie_tres = pd.Series(diccionario_serie_tres)

elemento_solo = serie_uno.get(2)
# print(elemento_solo)

elementos_indices = serie_uno.loc[2:4]

# print(elementos_indices)

elementos_indices_excluido = serie_uno.iloc[0:4]

# print(elementos_indices_excluido)
elementos_lista = serie_uno.to_list()

# print(type(elementos_lista))
# print(elementos_lista)

elementos_ndarray = serie_uno.values

# print(type(elementos_ndarray))
# print(elementos_ndarray)

copia_serie_uno = serie_uno.copy()
# print(copia_serie_uno)

serie_mas_uno = serie_uno + 1
# print(serie_mas_uno)

operacion_series = serie_uno + serie_dos
# print(operacion_series)

operacion_series_dos = serie_dos + serie_tres

# print(operacion_series_dos)

suma_series_add = serie_dos.add(serie_tres, fill_value = 0)

# print(suma_series_add)

# print(serie_uno.max())