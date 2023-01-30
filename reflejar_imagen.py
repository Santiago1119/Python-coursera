# -*- coding: utf-8 -*-


def reflejar_imagen(imagen:list):
    for i in range(len(imagen)):
        for j in range(len(imagen[i])//2):
            imagen[i][j], imagen[i][len(imagen[i])-1-j] = imagen[i][len(imagen[i])-1-j], imagen[i][j]
    return imagen

