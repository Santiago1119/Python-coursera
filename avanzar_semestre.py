# -*- coding: utf-8 -*-

def avanzar_semestre (est_1: dict, est_2: dict, est_3: dict, est_4: dict)->None:
    est_1['ssc'] += 1
    est_2['ssc'] += 1
    est_3['ssc'] += 1
    est_4['ssc'] += 1
    

e_1 = {'nombre': 'Lina', 'codigo': '2020101234', 'genero': 'femenino',
       'carrera': 'Sistemas', 'promedio': 4.78, 'ssc': 2}
e_2 = {'nombre': 'Laura', 'codigo': '2020105678', 'genero': 'femenino',
       'carrera': 'Civil', 'promedio': 4.21, 'ssc': 2}
e_3 = {'nombre': 'Felipe', 'codigo': '2020109012', 'genero': 'masculino',
       'carrera': 'Sistemas', 'promedio': 4.9, 'ssc': 2}
e_4 = {'nombre': 'Carlos', 'codigo': '2020103456', 'genero': 'masculino',
       'carrera': 'Economia', 'promedio': 3.89, 'ssc': 2}

print(f"Semestre estudiante: 1: {e_1['ssc']}")
print(f"Semestre estudiante: 2: {e_2['ssc']}")
print(f"Semestre estudiante: 3: {e_3['ssc']}")
print(f"Semestre estudiante: 4: {e_4['ssc']}")

avanzar_semestre(e_1, e_2, e_3, e_4)

print(f"Nuevo semestre estudiante 1: {e_1['ssc']}")
print(f"Nuevo semestre estudiante 2: {e_2['ssc']}")
print(f"Nuevo semestre estudiante 3: {e_3['ssc']}")
print(f"Nuevo semestre estudiante 4: {e_4['ssc']}")

