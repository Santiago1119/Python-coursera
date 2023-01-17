# -*- coding: utf-8 -*-

def mejor_del_salon (estudiante1: dict, estudiante2: dict, estudiante3: dict, estudiante4: dict, estudiante5: dict)->str:
    
    promedio1 = (estudiante1["matematicas"] + estudiante1["español"] + estudiante1["ciencias"] + estudiante1["literatura"] + estudiante1["arte"]) / 5
    promedio2 = (estudiante2["matematicas"] + estudiante2["español"] + estudiante2["ciencias"] + estudiante2["literatura"] + estudiante2["arte"]) / 5
    promedio3 = (estudiante3["matematicas"] + estudiante3["español"] + estudiante3["ciencias"] + estudiante3["literatura"] + estudiante3["arte"]) / 5
    promedio4 = (estudiante4["matematicas"] + estudiante4["español"] + estudiante4["ciencias"] + estudiante4["literatura"] + estudiante4["arte"]) / 5
    promedio5 = (estudiante5["matematicas"] + estudiante5["español"] + estudiante5["ciencias"] + estudiante5["literatura"] + estudiante5["arte"]) / 5

    promedios = {promedio1, promedio2, promedio3, promedio4, promedio5}

    mejor_promedio = max(promedios)
    
    mejor_estudiante = ''

    if mejor_promedio == promedio1:
        mejor_estudiante = estudiante1['nombre']
    elif mejor_promedio == promedio2:
        mejor_estudiante = estudiante2['nombre']
    elif mejor_promedio == promedio3:
        mejor_estudiante = estudiante3['nombre']
    elif mejor_promedio == promedio4:
        mejor_estudiante = estudiante4['nombre']
    elif mejor_promedio == promedio5:
        mejor_estudiante = estudiante5['nombre']    

    return mejor_estudiante