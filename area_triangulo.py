# -*- coding: utf-8 -*-

import math

def area_triangulo (s1:float, s2:float, s3:float)->float:
    
    sub = (s1 + s2 + s3) / 2
    area = math.sqrt(sub*(sub-s1) * (sub-s2) * (sub-s3))
    return round(area, 2)



s1 = float(input('Ingrese la longitud del primer lado del triangulo: '))
s2 = float(input('Ingrese la longitud del segundo lado del triangulo: '))
s3 = float(input('Ingrese la longitud del tercer lado del triandulo: '))

print(f'El area del triangulo es: {area_triangulo(s1, s2, s3)}')