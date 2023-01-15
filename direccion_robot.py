# -*- coding: utf-8 -*-
def movimientos_norte (giro)->str:

    nueva_orientacion = ""

    if giro == "L":
        nueva_orientacion = "W"
    elif giro == "R":
        nueva_orientacion = "E"
    elif giro == "H":
        nueva_orientacion = "S"
    else:
        nueva_orientacion = "N"
    
    return nueva_orientacion

def movimientos_sur (giro)->str:

    nueva_orientacion = ""

    if giro == "L":
        nueva_orientacion = "E"
    elif giro == "R":
        nueva_orientacion = "W"
    elif giro == "H":
        nueva_orientacion = "N"
    else:
        nueva_orientacion = "S"

    return nueva_orientacion
    
def movimientos_este (giro)->str:

    nueva_orientacion = ""
    
    if giro == "L":
        nueva_orientacion = "N"
    elif giro == "R":
        nueva_orientacion = "S"
    elif giro == "H":
        nueva_orientacion = "W"
    else:
        nueva_orientacion = "E"

    return nueva_orientacion
    
def movimientos_oeste (giro)->str:

    nueva_orientacion = ""
    
    if giro == "L":
        nueva_orientacion = "S"
    elif giro == "R":
        nueva_orientacion = "N"
    elif giro == "H":
        nueva_orientacion = "E"
    else:
        nueva_orientacion = "W"

    return nueva_orientacion


def movimiento_robot(orientacion_actual:str, giro_1:str, giro_2:str, giro_3:str)->str:

    if orientacion_actual == "N":
        orientacion_actual = movimientos_norte(giro_1)
    elif orientacion_actual == "S":
        orientacion_actual = movimientos_sur(giro_1)
    elif orientacion_actual == "E":
        orientacion_actual = movimientos_este(giro_1)
    else:
        orientacion_actual = movimientos_oeste(giro_1)

    if orientacion_actual == "N":
        orientacion_actual = movimientos_norte(giro_2)
    elif orientacion_actual == "S":
        orientacion_actual = movimientos_sur(giro_2)
    elif orientacion_actual == "E":
        orientacion_actual = movimientos_este(giro_2)
    else:
        orientacion_actual = movimientos_oeste(giro_2)

    if orientacion_actual == "N":
        orientacion_actual = movimientos_norte(giro_3)
    elif orientacion_actual == "S":
        orientacion_actual = movimientos_sur(giro_3)
    elif orientacion_actual == "E":
        orientacion_actual = movimientos_este(giro_3)
    else:
        orientacion_actual = movimientos_oeste(giro_3)
    
    
    return orientacion_actual

print(movimiento_robot('N', 'L', 'H', 'L'))

