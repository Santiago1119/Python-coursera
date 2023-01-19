# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 15:47:18 2023

@author: Usuario
"""


nueva_hora = 24

duracion_peli = 200

horas_peli, minutos_peli = divmod(duracion_peli, 60)

if minutos_peli == 0:
    minutos_peli = '00'

formato_horas_minutos_peli = str(horas_peli) + str(minutos_peli)

formato_horas_minutos_peli = int(formato_horas_minutos_peli)

termino_pelicula = nueva_hora + formato_horas_minutos_peli

if termino_pelicula > 2359:
    termino_pelicula -= 2400
   
if termino_pelicula < 99:
    termino_pelicula = str(termino_pelicula)
    termino_pelicula = '0' + termino_pelicula
