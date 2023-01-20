# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 18:48:07 2023

@author: Usuario
"""

def revisar_horas_peliculas(peli:dict, nueva_hora: int, nuevo_dia: str, p_revisar: dict)->bool:
    
    valor_retorno = False
    
    hpv, mpv = divmod(p_revisar['duracion'], 60)
    if mpv == 0:
        mpv = '00'
        
    fhm_peliv = int(str(hpv) + str(mpv))
    tpv = p_revisar['hora'] + fhm_peliv
    
    print(f'inicio pelicula vieja: {p_revisar["hora"]}')
    print(f'termino pelicula vieja {tpv}')
    
    
    hpn, mpn = divmod(peli['duracion'], 60)
    if mpn == 0:
        mpn = '00' 
        
    fhm_pelin = int(str(hpn) + str(mpn))
    
    tpn = nueva_hora + fhm_pelin
    
    print(f'inicio pelicula nueva: {nueva_hora}')
    print(f'termino pelicula nueva {tpn} \n')
    
    if (nueva_hora < p_revisar['hora'] and tpn < p_revisar['hora']) and (nuevo_dia == p_revisar['dia'] or nuevo_dia != p_revisar['dia']):
        valor_retorno = True
    
    if (nueva_hora > tpv) and (nuevo_dia == p_revisar['dia'] or nuevo_dia != p_revisar['dia']):
        valor_retorno = True
        
    return valor_retorno


pelicula_reagendar = {"nombre": "Inception","genero": "Acción, Drama", "duracion": 148, "anio": 2010, "clasificacion": '13+', "hora": 1300, "dia": "Lunes"}

pelicula1 = {"nombre": "Shrek","genero": "Familiar, Comedia", "duracion": 92, "anio": 2001, "clasificacion": 'Todos', "hora": 1700, "dia": "Viernes"}
pelicula2 = {"nombre": "Get Out","genero": "Suspenso, Terror", "duracion": 104, "anio": 2017, "clasificacion": '18+', "hora": 2330, "dia": "Sábado"}
pelicula3 = {"nombre": "Icarus","genero": "Documental, Suspenso", "duracion": 122, "anio": 2017, "clasificacion": '18+', "hora": 800, "dia": "Domingo"}
pelicula4 = {"nombre": "Inception","genero": "Acción, Drama", "duracion": 148, "anio": 2010, "clasificacion": '13+', "hora": 1300, "dia": "Lunes"}
pelicula5 = {"nombre": "The Empire Strikes Back","genero": "Familiar, Ciencia-Ficción", "duracion": 124, "anio": 1980, "clasificacion": '7+', "hora": 1415, "dia": "Miércoles"}

valor_imprimir = revisar_horas_peliculas(pelicula_reagendar, 2200, 'Sábado', pelicula1)
if valor_imprimir == False:
        print("False")
valor_imprimir = revisar_horas_peliculas(pelicula_reagendar, 2200, 'Sábado', pelicula2)
if valor_imprimir == False:
        print("False")
valor_imprimir = revisar_horas_peliculas(pelicula_reagendar, 2200, 'Sábado', pelicula3)
if valor_imprimir == False:
        print("False")
valor_imprimir = revisar_horas_peliculas(pelicula_reagendar, 2200, 'Sábado', pelicula4)
if valor_imprimir == False:
        print("False")
valor_imprimir = revisar_horas_peliculas(pelicula_reagendar, 2200, 'Sábado', pelicula5)
if valor_imprimir == False:
        print("False")



