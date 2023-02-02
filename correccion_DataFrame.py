# -*- coding: utf-8 -*-

import pandas as pd

peajes = pd.read_csv('nombre_archivo.csv', sep=";")

peajes.info()

peajes['COD_VIA'] = peajes['COD_VIA'].fillna('Sin codigo')
peajes['CAT4'] = peajes['CAT4'].fillna(0)
peajes['CAT5'] = peajes['CAT5'].fillna(0)

fechas_nulas = peajes[peajes['INIC_OPER'].isna()]
fechas_nulas[['NOMBRE', 'INIC_OPER', 'GEN']]
peajes['INIC_OPER'] = peajes['INIC_OPER'].fillna('01/01/2019')

peajes.info()

peajes['FECHA_INICIO_OP'] = pd.to_datetime(peajes['INIC_OPER'],
                                           infer_datetime_format=True,
                                           errors='coerce')

peajes.info()
peajes['FECA_INICIO_OP'].head()