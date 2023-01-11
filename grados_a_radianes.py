# -*- coding: utf-8 -*-

def grados_a_radianes (grados:float)->float:
    pi = 3.14159
    rad = (2*pi*grados)/360
    return rad

print(grados_a_radianes(45))
