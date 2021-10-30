import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce

# This file will be the data getter and washer

file2017 = 'Datas/VEHICULOS_PARQUE_MOVIL_2017.csv'
file2018 = 'Datas/VEHICULOS_PARQUE_MOVIL_2018.csv'
file2019 = 'Datas/VEHICULOS_PARQUE_MOVIL_2019.csv'
file2020 = 'Datas/VEHICULOS_PARQUE_MOVIL_2020.csv'
file2021 = 'Datas/VEHICULOS_PARQUE_MOVIL_2021.csv'


# convertir les données 2017-18-19 pour mettre a jour noms ----------------------
def updatedataBefore2020(datas):
    dataTab = datas.rename(columns={'ENERG�A/COMBUSTIBLE': 'ENERGÍA/COMBUSTIBLE', 'N� MPAL': 'Nº MPAL'})
    return dataTab


def updateValuesBefore2020(datas):
    dataValues = datas['ENERGÍA/COMBUSTIBLE'].replace(['EL�CTRICO', 'GASOLINA / HIBRIDO', 'EL�CTRICO / H�BRIDO'],
                                                      ['ELÉCTRICO', 'GASOLINA/HIBRIDO', 'ELÉCTRICO / HÍBRIDO'])
    return dataValues


def updateValuesStart2020(datas):
    dataValues = datas['ENERGÍA/COMBUSTIBLE'].replace(['DIESEL'], ['DIESEL'])
    return dataValues


def TotalConsoByTypo():
    #totalconsobytipo = pd.concat([d17Group, d18Group, d19Group, d20Group, d21Group], axis=1)
    dfrr = [d17Group, d18Group, d19Group, d20Group, d21Group]
    totalconsobytipo = reduce(lambda left,right: pd.merge(left,right,on='Type'), dfrr)
    #totalconsobytipo = pd.merge(dfrr, on='Type', how='right')
    #print(totalconsobytipo)
    return totalconsobytipo


# Variables
d17 = pd.read_csv(file2017, delimiter=';')
d18 = pd.read_csv(file2018, delimiter=';')
d19 = pd.read_csv(file2019, delimiter=';')
d20 = pd.read_csv(file2020, delimiter=';')
d21 = pd.read_csv(file2021, delimiter=';')

d17step = d17.drop_duplicates()
d18step = d18.drop_duplicates()
d19step = d19.drop_duplicates()
d20step = d20.drop_duplicates()
d21step = d21.drop_duplicates()

d17Tab = updatedataBefore2020(d17step)
d17Clean = updateValuesBefore2020(d17Tab)
d17Group = updateValuesBefore2020(d17Tab).value_counts().rename_axis('Type').reset_index(name='2017')

d18Tab = updatedataBefore2020(d18step)
d18Clean = updateValuesBefore2020(d18Tab)
d18Group = updateValuesBefore2020(d18Tab).value_counts().rename_axis('Type').reset_index(name='2018')

d19Tab = updatedataBefore2020(d19step)
d19Clean = updateValuesBefore2020(d19Tab)
d19Group = updateValuesBefore2020(d19Tab).value_counts().rename_axis('Type').reset_index(name='2019')

d20Clean = updateValuesBefore2020(d20step)
d20Group = updateValuesBefore2020(d20step).value_counts().rename_axis('Type').reset_index(name='2020')

d21Clean = updateValuesBefore2020(d21step)
d21Group = updateValuesBefore2020(d21step).value_counts().rename_axis('Type').reset_index(name='2021')




#d17Group1 = d17Group.join(d21Group["2021"],d20Group["2020"])
TotalConsoByTypo()