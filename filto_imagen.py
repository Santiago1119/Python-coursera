# -*- coding: utf-8 -*-

def aplicar_filtro_color(imagen:list, conservar:tuple)->list:
    nueva_imagen = []
    alto = len(imagen)
    ancho = len(imagen[0])
    
    for i in range(alto):
        fila_nueva = []
        for j in range(ancho):
            r,g,b = imagen[i][j]
            temp = [r,g,b]
            for k in range(3):
                if not conservar[k]:
                    temp[k] = 0.0
            nuevo_pixel = (temp[0], temp[1], temp[2])
            fila_nueva.append(nuevo_pixel)
            
        nueva_imagen.append(fila_nueva)
        
    return nueva_imagen