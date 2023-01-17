# -*- coding: utf-8 -*-

def quienes_en_riesgo (est1: dict, est2: dict, est3: dict, est4: dict)->dict:
    en_riesgo = {}
    
    if est1['promedio'] < 3.4:
        en_riesgo[est1['codigo']] = est1['promedio']
    
    if est2['promedio'] < 3.4:
        en_riesgo[est2['codigo']] = est2['promedio']
    
    if est3['promedio'] < 3.4:
        en_riesgo[est3['codigo']] = est3['promedio']
    
    if est4['promedio'] < 3.4:
        en_riesgo[est4['codigo']] = est4['promedio']
        
    return en_riesgo

e_1 = {'nombre': 'Lina', 'codigo': '2020101234', 'genero': 'femenino',
       'carrera': 'Sistemas', 'promedio': 4.78, 'ssc': 2}
e_2 = {'nombre': 'Laura', 'codigo': '2020105678', 'genero': 'femenino',
       'carrera': 'Civil', 'promedio': 3.29, 'ssc': 2}
e_3 = {'nombre': 'Felipe', 'codigo': '2020109012', 'genero': 'masculino',
       'carrera': 'Sistemas', 'promedio': 4.9, 'ssc': 2}
e_4 = {'nombre': 'Carlos', 'codigo': '2020103456', 'genero': 'masculino',
       'carrera': 'Economia', 'promedio': 3.2, 'ssc': 2}

riesgo = quienes_en_riesgo(e_1, e_2, e_3, e_4)

print(riesgo)
    
