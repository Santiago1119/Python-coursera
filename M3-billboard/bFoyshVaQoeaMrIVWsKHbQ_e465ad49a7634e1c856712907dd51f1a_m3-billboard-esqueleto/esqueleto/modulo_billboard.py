# -*- coding: utf-8 -*-

def cargar_canciones(nombre_archivo:str)->list:
    """
    Recibe como parametro un string con el nombre de un archivo .csv y retorna
    una lista con todas las caciones en diccionarios

    Parameters
    ----------
    nombre_archivo : str
        nombre del archivo.

    Returns
    -------
    list
        Una lista con diccionarios que representan cada canción.

    """
    lista_canciones = []
    archivo = open(nombre_archivo)
    archivo.readline().split(",")
    
    for linea in archivo:
        
        info_cancion = linea.split(",")
        cancion = {}
        
        cancion["posicion"] = int(info_cancion[0])
        cancion["nombre_cancion"] = info_cancion[1]
        cancion["nombre_artista"] = info_cancion[2]
        cancion["anio"] = int(info_cancion[3])
        cancion["letra"] = info_cancion[4]
        
        lista_canciones.append(cancion) 

        
    archivo.close()
    return lista_canciones


def buscar_cancion(lista_canciones:list, nombre_cancion:str, anio_rank:int)->dict:
    """
    En una lista de canciones busca una canción por el nombre y el año y retorna la información
    de dicha canción, si no la encuentra retorna None

    Parameters
    ----------
    lista_canciones : list
        Lista de canciones (diccionarios).
    nombre_cancion : str
        nombre de la cancion que se desea buscar.
    anio_rank : int
        año de lanzamiento de la canción.

    Returns
    -------
    dict
        diccionario con la información de la canción encontrada, si no la encuentra
        retorna None.

    """
    valor_retorno = None
    
    cancion_buscada = {}
    
    for cancion in range(0, len(lista_canciones)):
        if lista_canciones[cancion]["anio"] == anio_rank and lista_canciones[cancion]["nombre_cancion"] == nombre_cancion:
            cancion_buscada = lista_canciones[cancion]
            
    if len(cancion_buscada) > 0:
        valor_retorno = cancion_buscada
    
    return valor_retorno

def canciones_anio(lista_canciones:list, anio:int)->list:
    """
    En una lista de canciones busca las canciones de un año pasado como parametro, 
    si no encuentra ninguna canción en ese año retorna una lista vacia

    Parameters
    ----------
    lista_canciones : list
        Lista con todas las canciones (diccionarios).
    anio : int
        Año del que queremose extraer todas las canciones.

    Returns
    -------
    list
        Lista con la información de las canciones excepto las letras.

    """
    lista_retorno = []
    
    for cancion in range(0, len(lista_canciones)):
        if lista_canciones[cancion]["anio"] == anio:
            
            diccionario = {}
            diccionario["posicion"] = lista_canciones[cancion]["posicion"]
            diccionario["nombre_cancion"] = lista_canciones[cancion]["nombre_cancion"]
            diccionario["nombre_artista"] = lista_canciones[cancion]["nombre_artista"]
            diccionario["anio"] = lista_canciones[cancion]["anio"]
            
            lista_retorno.append(diccionario)
            
    return lista_retorno

def canciones_artista_periodo(lista_canciones:list, artista:str, anio_inic:int, anio_fin:int)->list:
    """
    Busca todas las canciones de un artista en un periodo de tiempo

    Parameters
    ----------
    lista_canciones : list
        Lista con las canciones.
    artista : str
        Nombre del artista como.
    anio_inic : int
        año de inicio de busqueda.
    anio_fin : int
        año de fin de busqueda.

    Returns
    -------
    list
        Canciones del artista en el periodo de tiempo especificado.

    """
    lista_retorno = []
    
    for cancion in range(0, len(lista_canciones)):
        if lista_canciones[cancion]["nombre_artista"] == artista and lista_canciones[cancion]["anio"] >= anio_inic and lista_canciones[cancion]["anio"] <= anio_fin:
            
            diccionario = {}
            diccionario["posicion"] = lista_canciones[cancion]["posicion"]
            diccionario["nombre_cancion"] = lista_canciones[cancion]["nombre_cancion"]
            diccionario["nombre_artista"] = lista_canciones[cancion]["nombre_artista"]
            diccionario["anio"] = lista_canciones[cancion]["anio"]
            
            lista_retorno.append(diccionario)
            
    return lista_retorno

def todas_canciones_artista(lista_canciones:list, artista:str)->list:
    """
    Busca todas las canciones de un artista en específico

    Parameters
    ----------
    lista_canciones : list
        Lista de canciones.
    artista : str
        Nombre del artista.

    Returns
    -------
    list
        Lista con todas las canciones interpretadas por el artista.

    """
    lista_retorno = []
    
    for cancion in range(0, len(lista_canciones)):
        if lista_canciones[cancion]["nombre_artista"] == artista:
            
            diccionario = {}
            diccionario["posicion"] = lista_canciones[cancion]["posicion"]
            diccionario["nombre_cancion"] = lista_canciones[cancion]["nombre_cancion"]
            diccionario["nombre_artista"] = lista_canciones[cancion]["nombre_artista"]
            diccionario["anio"] = lista_canciones[cancion]["anio"]
            
            lista_retorno.append(diccionario)
    
    
    return lista_retorno

def todos_artistas_cancion(lista_canciones:list, nom_cancion:str)->list:
    """
    Busca todos los artistas que interpreten una misma canción

    Parameters
    ----------
    lista_canciones : list
        Lista de canciones.
    nom_cancion : str
        Nombre de la canción que interpretan varios artistas.

    Returns
    -------
    list
        Lista de artistas que interpretan la misma canción.

    """
    
    lista_retorno = []
    
    for cancion in range(0, len(lista_canciones)):
        if lista_canciones[cancion]['nombre_cancion'] == nom_cancion:
            lista_retorno.append(lista_canciones[cancion]['nombre_artista'])
            
    return lista_retorno

def artistas_mas_populares(lista_canciones:list, cantidad_minima:int)->dict:
    """
    Pide como parametro la lista de canciones y una cantidad de canciones, si 
    un artista tiene más canciones de las pasadas como parametro entra a la lista
    que se retorna, de lo contrario no

    Parameters
    ----------
    lista_canciones : list
        Lista de canciones.
    cantidad_minima : int
        cantidad de evaluacion.

    Returns
    -------
    dict
        artistas que tienes mas canciones del numero especificado.

    """
    diccionario_retorno = {}
    diccionario_auxiliar = {}
    
    for cancion in range(0, len(lista_canciones)):
        artista = lista_canciones[cancion]['nombre_artista']
        if lista_canciones[cancion]['nombre_artista'] not in diccionario_auxiliar:
            diccionario_auxiliar[artista] = 1
        else:
            diccionario_auxiliar[artista] += 1
        
    
    for artista in diccionario_auxiliar:
        if diccionario_auxiliar[artista] > cantidad_minima:
            diccionario_retorno[artista] = diccionario_auxiliar[artista]

    
    return diccionario_retorno
            
def artista_estrella(lista_canciones:list)->dict:
    
    diccionario_auxiliar = {}
    
    diccionario_retorno = {}
    
    for cancion in range(0, len(lista_canciones)):
        artista = lista_canciones[cancion]['nombre_artista']
        if lista_canciones[cancion]['nombre_artista'] not in diccionario_auxiliar:
            diccionario_auxiliar[artista] = 1
        else:
            diccionario_auxiliar[artista] += 1 

    mejor_artista = max(diccionario_auxiliar, key=diccionario_auxiliar.get)
    
    diccionario_retorno[mejor_artista] = diccionario_auxiliar[mejor_artista]
    
    return diccionario_retorno
    
def artistas_y_sus_canciones(lista_canciones:list)->dict:
    """
    Retorna en un diccionario los artistas como claves y una lista como valor de
    cada artista con las canciones que ha escrito

    Parameters
    ----------
    lista_canciones : list
        Lista de canciones.

    Returns
    -------
    dict
        diccionario con todos los artistas y las canciones que han escrito.

    """
    
    diccionario_retorno = {}
    canciones_recorridas = []
    
    for cancion in range(0, len(lista_canciones)):
        cancion_actual = lista_canciones[cancion]['nombre_cancion']
        artista = lista_canciones[cancion]['nombre_artista']
        
        if artista not in diccionario_retorno:
            
            diccionario_retorno[artista] = []
            diccionario_retorno[artista].append(cancion_actual)
            canciones_recorridas.append(cancion_actual)
            
        if cancion_actual not in canciones_recorridas and artista in diccionario_retorno:
            diccionario_retorno[artista].append(cancion_actual)
            canciones_recorridas.append(cancion_actual)
            
    return diccionario_retorno
            

def promedio_canciones_por_artista(canciones:list)->float:

    
    
    
    k = 0
    
    resultado_pre = {}
    
    for cancion in canciones:
        if cancion["nombre_artista"] in resultado_pre:
            if cancion["nombre_cancion"] not in resultado_pre[cancion["nombre_artista"]]:
                resultado_pre[cancion["nombre_artista"]] = resultado_pre[cancion["nombre_artista"]] + [cancion["nombre_cancion"]]
                k = k + 1
        else:
            resultado_pre[cancion["nombre_artista"]] = [cancion["nombre_cancion"]]
            k = k + 1
    
    j = list(resultado_pre.keys()) 
    
    promedio = k/len(j)    

    
    return promedio
        
















