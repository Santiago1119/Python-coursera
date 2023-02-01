# -*- coding: utf-8 -*-

import pandas as pd

a1 = {"tiempo":9.58, "atleta":"Usain Bolt", "país":"Jamaica", "fecha":"16/08/2009", "ciudad":"Berlín"}
a2 = {"tiempo":9.69, "atleta":"Usain Bolt", "país":"Jamaica", "fecha":"16/08/2008", "ciudad":"Beijing"}
a3 = {"tiempo":9.72, "atleta":"Usain Bolt", "país":"Jamaica", "fecha":"31/05/2008", "ciudad":"New York"}
a4 = {"tiempo":9.74, "atleta":"Asafa Powel", "país":"Jamaica", "fecha":"09/09/2007", "ciudad":"Rieti"}
a5 = {"tiempo":9.77, "atleta":"Asafa Powel", "país":"Jamaica", "fecha":"18/08/2006", "ciudad":"Zurich"}

records = [a1, a2, a3, a4, a5]

df_records1 = pd.DataFrame(records)

# print(df_records1)

tiempos = pd.Series([9.58, 9.69, 9.72, 9.74, 9.77])
atletas = pd.Series(["Usain Bolt", "Usain Bolt", "Usain Bolt", "Asafa Powel", "Asafa Powel"])
paises = pd.Series(["Jamaica", "Jamaica", "Jamaica", "Jamaica", "Jamaica"])
fechas = pd.Series(["16/08/2009", "16/08/2008", "31/05/2008", "09/09/2007", "18/08/2006"])
ciudades = pd.Series(["Berlín", "Beijing", "New York", "Rieti", "Zurich"])

datos = {"tiempo": tiempos, "atleta": atletas, "paises": paises, "fechas": fechas, "ciudades": ciudades}

df_records2 = pd.DataFrame(datos)

print(df_records2)