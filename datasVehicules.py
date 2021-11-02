import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce

# This file will be the data getter and washer


def processTotal(file, date):
    datas = pd.read_csv(file, delimiter=';')
    datas.drop_duplicates()
    datas = datas.iloc[:, 0:7]
    datas.columns = ['Num', 'Area', 'Direction', 'Uso', 'Vehicule', 'Juridique', 'Energie']
    datas['Energie'] = datas['Energie'].replace(['EL�CTRICO', 'GASOLINA / HIBRIDO', 'EL�CTRICO / H�BRIDO'],
                                                ['ELÉCTRICO', 'GASOLINA/HIBRIDO', 'ELÉCTRICO / HÍBRIDO'])
    datas['Energie'] = datas['Energie'].replace(['DIESEL '], ['DIESEL'])
    datas['Date'] = date
    return datas


def fusionDF(df1, df2, df3, df4, df5):
    datas = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)
    return datas