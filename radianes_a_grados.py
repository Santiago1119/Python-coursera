# -*- coding: utf-8 -*-

def radianes_a_grados(radianes:float)->float:
    pi = 3.14159
    return (360*radianes)/(2*pi)

print(radianes_a_grados(20))