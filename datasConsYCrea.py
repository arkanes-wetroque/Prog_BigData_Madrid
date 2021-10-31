import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


File = 'Datas/CONSUMO Y GENERACIÓN_energía_Ayuntamiento de Madrid_2020.xlsx'
src_file = Path.cwd() /  'Datas/CONSUMO Y GENERACIÓN_energía_Ayuntamiento de Madrid_2020.xlsx'

df1t = pd.read_excel(src_file, header=1, usecols='B:I')

def getConso(year):
    conso = df1t.loc[(df1t['AÑO'] == year) & (df1t['CLASE'] == "Consumida"), 'CANTIDAD'].sum()
    return conso
def getGenere(year):
    geno = Gene2020 = df1t.loc[(df1t['AÑO'] == year) & (df1t['CLASE'] == "Generada"), 'CANTIDAD'].sum()
    return geno


def getDataByAmbito(year, nameAmbito, type):
    data = df1t.loc[(df1t['AÑO'] == year) & (df1t["ÁMBITO 1"] == nameAmbito) & (df1t["CLASE"] == type), 'CANTIDAD'].sum()
    return data

def getDataFrameByAmbito(year, type):
    CAmb1_18 = getDataByAmbito(year, "Parque Tecnológico de Valdemingómez", type)
    CAmb2_18 = getDataByAmbito(year, "Edificios y Centros", type)
    CAmb3_18 = getDataByAmbito(year, "Parque móvil", type)
    CAmb4_18 = getDataByAmbito(year, "Parques y viveros", type)
    CAmb5_18 = getDataByAmbito(year, "Alumbrado e instalaciones", type)
    df = {'Ambito': ["Parque Tecnológico de Valdemingómez", "Edificios y Centros", "Parque móvil", "Parques y viveros",
                      "Alumbrado e instalaciones"], 'count': [CAmb1_18, CAmb2_18, CAmb3_18, CAmb4_18, CAmb5_18]}
    AmbitioDataframe = pd.DataFrame(data=df)
    return AmbitioDataframe


def getAmbitoTypeEnergy(type, year):
    res = df1t.groupby(['ÁMBITO 2', 'AÑO', 'CLASE', 'TIPO'])['CANTIDAD'].mean().reset_index()
    res = res[(res['CLASE'] == type) & (res['AÑO'] == year)]
    return res