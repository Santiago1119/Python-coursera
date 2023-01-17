# -*- coding: utf-8 -*-

def buscar_estudiante (est1: dict, est2: dict, est3: dict, est4: dict, nom:str)->dict:
    buscado = None
    
    if est1['nombre'] == nom:
        buscado = est1
    elif est2['nombre'] == nom:
        buscado = est2
    elif est3['nombre'] == nom:
        buscado = est3
    elif est4['nombre'] == nom:
        buscado = est4
        
    return buscado

e_1 = {'nombre': 'Lina', 'codigo': '2020101234', 'genero': 'femenino',
       'carrera': 'Sistemas', 'promedio': 4.78, 'ssc': 2}
e_2 = {'nombre': 'Laura', 'codigo': '2020105678', 'genero': 'femenino',
       'carrera': 'Civil', 'promedio': 4.21, 'ssc': 2}
e_3 = {'nombre': 'Felipe', 'codigo': '2020109012', 'genero': 'masculino',
       'carrera': 'Sistemas', 'promedio': 4.9, 'ssc': 2}
e_4 = {'nombre': 'Carlos', 'codigo': '2020103456', 'genero': 'masculino',
       'carrera': 'Economia', 'promedio': 3.89, 'ssc': 2}

nombre = input("Ingrese el nombre del estudiante a buscar: ")

est_buscado = buscar_estudiante(e_1, e_2, e_3, e_4, nombre)

if est_buscado is None:
    print('El estudiante no existe')
else:
    print(f"El estudiante existe y su código es {est_buscado['codigo']}")