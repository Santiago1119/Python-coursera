"""
Ejercicio nivel 2: Agenda de peliculas.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2

NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """    
    
    pelicula = {'nombre': nombre, 'genero': genero, 'duracion': duracion, 'anio': anio,
                'clasificacion': clasificacion, 'hora': hora, 'dia': dia}
    
    return pelicula

def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
        None si no se encuentra una pelicula con ese nombre.
    """
    pelicula_retorno = None
    
    if p1['nombre'] == nombre_pelicula:
        pelicula_retorno = p1

    if p2['nombre'] == nombre_pelicula:
        pelicula_retorno = p2

    if p3['nombre'] == nombre_pelicula:
        pelicula_retorno = p3
        
    if p4['nombre'] == nombre_pelicula:
        pelicula_retorno = p4
        
    if p5['nombre'] == nombre_pelicula:
        pelicula_retorno = p5
        
    return pelicula_retorno
    

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """
    mayor_duracion = p1
    
    if p2['duracion'] > p1['duracion']:
        mayor_duracion = p2

    if p3['duracion'] > p2['duracion']:
        mayor_duracion = p3
        
    if p4['duracion'] > p3['duracion']:
        mayor_duracion = p4
    
    if p5['duracion'] > p4['duracion']:
        mayor_duracion = p5
        
    return mayor_duracion
    

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
       Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """
    promedio = p1['duracion'] +  p2['duracion'] + p3['duracion'] + p4['duracion'] + p5['duracion'] / 5
    
    horas, minutos = divmod(promedio, 60)
    
    return f"La duracion promedio de las peliculas en horas y minutos es igual a {horas}:{minutos}"

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    mensaje_retorno = ''
    
    if p1['anio'] > anio:
        mensaje_retorno = p1['nombre']
    
    if p2['anio'] > anio:
        mensaje_retorno += ',' + p2['nombre'] 
        
    if p3['anio'] > anio:
        mensaje_retorno += ',' + p3['nombre']
        
    if p4['anio'] > anio:
        mensaje_retorno += ',' + p4['nombre']
        
    if p5['anio'] > anio:
        mensaje_retorno += ',' + p5['nombre']
        
    if mensaje_retorno == '':
        mensaje_retorno = 'Ninguna'
        
    return mensaje_retorno

def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """
    peliculas_mas_18 = 0
    
    if p1['clasificacion'] == '18+':
        peliculas_mas_18 += 1
    
    if p2['clasificacion'] == '18+':
        peliculas_mas_18 += 1

    if p3['clasificacion'] == '18+':
        peliculas_mas_18 += 1
        
    if p4['clasificacion'] == '18+':
        peliculas_mas_18 += 1

    if p5['clasificacion'] == '18+':
        peliculas_mas_18 += 1

    return peliculas_mas_18

def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool: 
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
    valor_retorno = False
    
    ''' 
    Respetando lo que se ha visto en el curso repeti el proceso por cada pelicula para validar si la nueva hora
    interfiere con alguna hora o dia de las demas peliculas, ya que aclaro con un ciclo se pudo haber reducido 
    una cantidad de código importante
    '''
    
    #PELICULA 1
    horas_peli1, minutos_peli1 = divmod(p1['duracion'], 60)
    
    if minutos_peli1 == 0:
        minutos_peli1 = '00'
        
    formato_horas_minutos_peli1 = str(horas_peli1) + str(minutos_peli1)
    formato_horas_minutos_peli1 = int(formato_horas_minutos_peli1)
    termino_pelicula1 = p1['hora'] + formato_horas_minutos_peli1

    if termino_pelicula1 > 2359:
        termino_pelicula1 -= 2400
       
    if termino_pelicula1 < 99:
        termino_pelicula1 = str(termino_pelicula1)
        termino_pelicula1 = '0' + termino_pelicula1
        
    if (str(nueva_hora) < str(termino_pelicula1) or str(nueva_hora) > str(p1['hora'])) and nuevo_dia == p1['dia']:
        valor_retorno = False
        
    #PELICULA 2
    
    horas_peli2, minutos_peli2 = divmod(p2['duracion'], 60)
    
    if minutos_peli2 == 0:
        minutos_peli2 = '00'
        
    formato_horas_minutos_peli2 = str(horas_peli2) + str(minutos_peli2)
    formato_horas_minutos_peli2 = int(formato_horas_minutos_peli2)
    termino_pelicula2 = p2['hora'] + formato_horas_minutos_peli2

    if termino_pelicula2 > 2359:
        termino_pelicula2 -= 2400
       
    if termino_pelicula2 < 99:
        termino_pelicula2 = str(termino_pelicula2)
        termino_pelicula2 = '0' + termino_pelicula2
        
    if (str(nueva_hora) < str(termino_pelicula2) or str(nueva_hora) > str(p2['hora'])) and nuevo_dia == p2['dia']:
        valor_retorno = False
        
    #PELICULA 3
    
    horas_peli3, minutos_peli3 = divmod(p3['duracion'], 60)
    
    if minutos_peli3 == 0:
        minutos_peli3 = '00'
        
    formato_horas_minutos_peli3 = str(horas_peli3) + str(minutos_peli3)
    formato_horas_minutos_peli3 = int(formato_horas_minutos_peli3)
    termino_pelicula3 = p3['hora'] + formato_horas_minutos_peli3

    if termino_pelicula3 > 2359:
        termino_pelicula3 -= 2400
       
    if termino_pelicula3 < 99:
        termino_pelicula3 = str(termino_pelicula3)
        termino_pelicula3 = '0' + termino_pelicula3
        
    if (str(nueva_hora) < str(termino_pelicula3) or str(nueva_hora) > str(p3['hora'])) and nuevo_dia == p3['dia']:
        valor_retorno = False
        
    #PELICULA 4
    
    horas_peli4, minutos_peli4 = divmod(p4['duracion'], 60)
    
    if minutos_peli4 == 0:
        minutos_peli4 = '00'
        
    formato_horas_minutos_peli4 = str(horas_peli4) + str(minutos_peli4)
    formato_horas_minutos_peli4 = int(formato_horas_minutos_peli4)
    termino_pelicula4 = p4['hora'] + formato_horas_minutos_peli4

    if termino_pelicula4 > 2359:
        termino_pelicula4 -= 2400
       
    if termino_pelicula4 < 99:
        termino_pelicula4 = str(termino_pelicula4)
        termino_pelicula4 = '0' + termino_pelicula4
        
    if (str(nueva_hora) < str(termino_pelicula4) or str(nueva_hora) > str(p4['hora'])) and nuevo_dia == p4['dia']:
        valor_retorno = False
    
    #PELICULA 5
    
    horas_peli5, minutos_peli5 = divmod(p5['duracion'], 60)
    
    if minutos_peli5 == 0:
        minutos_peli5 = '00'
        
    formato_horas_minutos_peli5 = str(horas_peli5) + str(minutos_peli5)
    formato_horas_minutos_peli5 = int(formato_horas_minutos_peli5)
    termino_pelicula5 = p5['hora'] + formato_horas_minutos_peli5

    if termino_pelicula5 > 2359:
        termino_pelicula5 -= 2400
       
    if termino_pelicula5 < 99:
        termino_pelicula5 = str(termino_pelicula5)
        termino_pelicula5 = '0' + termino_pelicula5
        
    if (str(nueva_hora) < str(termino_pelicula5) or str(nueva_hora) > str(p5['hora'])) and nuevo_dia == p5['dia']:
        valor_retorno = False
    
    #CONTROL HORARIO
    
    if control_horario == True:
        if peli['genero'] != 'Documental' and (peli['hora'] < 2200):
            valor_retorno = True
        if peli['dia'] != 'Viernes' and (peli['genero'] == 'Drama'):
            valor_retorno = True
        if (peli['hora'] < 2300 or peli['hora'] > 600) and (peli['dia'] == 'Sábado' or peli['dia'] == 'Domingo'):
            valor_retorno = True
        
    return valor_retorno    
        
        
    
def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool)->bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
       pelicula que entra igualmente por parametro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    
    invitacion = False
    
    restriccion_edad = peli['clasificacion']
    
    
    if edad_invitado >= 18:
        invitacion = True
    
    if edad_invitado < 15 and peli['genero'] != 'Terror':
        invitacion = True
    
    if edad_invitado < 10 and peli['genero'] == 'Familiar':
        invitacion = True
        
    if restriccion_edad == '18+' and edad_invitado < 18 and autorizacion_padres == True:
        invitacion = True
        
    if restriccion_edad == '16+' and edad_invitado < 16 and autorizacion_padres == True:
        invitacion = True
        
    if restriccion_edad == '13+' and edad_invitado < 13 and autorizacion_padres == True:
        invitacion = True
        
    if restriccion_edad == '7+' and edad_invitado < 7 and autorizacion_padres == True:
        invitacion = True
        
    if peli['genero'] == 'Documental':
        invitacion = True
        
    return invitacion
    
    









