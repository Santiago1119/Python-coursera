# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']

temperaturas_bog = [14.3, 14.3, 15.0, 14.7, 14.7, 14.5, 14.3, 14.2, 14.3, 14.3, 14.5, 14.4]

#Creamos la figura arriba
plt.figure(figsize=(7,4))

plt.plot(meses, temperaturas_bog, label="temperatura")

plt.xlabel("Meses")
plt.ylabel("temperatura")
plt.title("Temperatura promedio en Bogotá, por mes (1970-2000)")
#Permite que se vea la figura
plt.legend()

