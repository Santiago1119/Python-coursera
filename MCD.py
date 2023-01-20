# -*- coding: utf-8 -*-

def maximo_comun_divisor(n1:int, n2:int)->int:
	n= min(n1, n2)
	encontro = False
	while(encontro == False):
		if(n1%n == 0 and n2%n == 0):
			encontro = True
		else:
			n = n-1
	return n