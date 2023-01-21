# -*- coding: utf-8 -*-


def sucesion_fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=',')
        a, b = b, a+b
    print()

sucesion_fibonacci(18)




lista=[]
for i in range(2000, 3201):
    if (i%7==0):    	 	
        lista.append(str(i))
print (','.join(lista))
