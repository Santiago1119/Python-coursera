# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']

temperaturas_bog = [14.3, 14.3, 15.0, 14.7, 14.7, 14.5, 14.3, 14.2, 14.3, 14.3, 14.5, 14.4]


fig = plt.figure(figsize=(7, 4))

ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(meses, temperaturas_bog, label="temperaturas")
ax.set_xlabel("Meses")
ax.set_ylabel("Temperatura")
ax.set_title("Temperatura promedio en Bogotá, por mes (1970-2000)")
ax.legend()

