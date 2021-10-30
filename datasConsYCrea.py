import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


File = 'Datas/CONSUMO Y GENERACIÓN_energía_Ayuntamiento de Madrid_2020.xlsx'
src_file = Path.cwd() /  'Datas/CONSUMO Y GENERACIÓN_energía_Ayuntamiento de Madrid_2020.xlsx'

df1t = pd.read_excel(src_file, header=1, usecols='B:I')

Con2018 = df1t.loc[(df1t['AÑO'] == 2018) & (df1t['CLASE'] == "Consumida"), 'CANTIDAD'].sum()
Con2019 = df1t.loc[(df1t['AÑO'] == 2019) & (df1t['CLASE'] == "Consumida"), 'CANTIDAD'].sum()
Con2020 = df1t.loc[(df1t['AÑO'] == 2020) & (df1t['CLASE'] == "Consumida"), 'CANTIDAD'].sum()

Gene2018 = df1t.loc[(df1t['AÑO'] == 2018) & (df1t['CLASE'] == "Generada"), 'CANTIDAD'].sum()
Gene2019 = df1t.loc[(df1t['AÑO'] == 2019) & (df1t['CLASE'] == "Generada"), 'CANTIDAD'].sum()
Gene2020 = df1t.loc[(df1t['AÑO'] == 2020) & (df1t['CLASE'] == "Generada"), 'CANTIDAD'].sum()

d = {'Consomation': [Con2018, Con2019, Con2020], 'Creation': [Gene2018, Gene2019, Gene2020], 'Year': [2018, 2019, 2020]}
DataConsoTotal = pd.DataFrame(data=d)