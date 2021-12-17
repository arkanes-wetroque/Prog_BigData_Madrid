import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html
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

#---------------------------------------------------------------------------------------------#

def getYearT(year1, year2):
    year = []
    for yearR in range(year1, year2 + 1):
        y = yearR
        year.append(y)
        yearR = yearR+1
    return year

def getYearTs(year1, year2):
    year = []
    for yearR in range(year1, year2 + 1):
        yS = yearR
        sYear = str(yS)
        year.append(sYear)
        yearR = yearR+1
    return year

def getConsoT(year1, year2):
    conso = []
    for year in range(year1, year2 + 1):
        c = getConso(year)
        conso.append(c)
        year = year+1
    return conso

def getGeneT(year1, year2):
    gene = []
    for year in range(year1, year2 + 1):
        g = getGenere(year)
        gene.append(g)
        year = year+1
    return gene

def getConsoAmbitioT(year1, year2):
    consoAmbi = []
    for year in range(year1, year2 + 1):
        cA = getDataFrameByAmbito(year, "Consumida")
        consoAmbi.append(cA)
        year = year+1
    return consoAmbi

def getConsoAmbitioT(year1, year2):
    consoAmbi = []
    i = 1
    count = year2-year1
    print(count)
    for year in range(year1, year2 + 1):
        cA = getDataFrameByAmbito(year, "Consumida")
        consoAmbi.append(cA)
        year = year+1
    if count == 2:
        cAT = pd.concat([cA, cA['count'], cA['count']], axis=1)

    else:
        cAT = pd.concat([cA, cA['count']], axis=1)

    for year in range(year1, year2 + 1):
        sYear = str(year)
        cAT.columns.values[i] = sYear
        i = i+1
    print(cAT)
    return cAT

def getGeneAmbitioT(year1, year2):
    i = 1
    count = year2 - year1
    geneAmbi = []
    for year in range(year1, year2 + 1):
        gA = getDataFrameByAmbito(year, "Generada")
        geneAmbi.append(gA)
        year = year+1
    if count == 2:
        cAT = pd.concat([gA, gA['count'], gA['count']], axis=1)
    else:
        cAT = pd.concat([gA, gA['count']], axis=1)

    for year in range(year1, year2 + 1):
        sYear = str(year)
        cAT.columns.values[i] = sYear
        i = i + 1
    return cAT

def graphPieGen():
    i = 1
    graphPie = []
    for year in range(2018, 2021):
        gP = getAmbitoTypeEnergy("Generada", year)
        gYear = str(year) + " generation"
        gPC = px.pie(gP, values='CANTIDAD', names='ÁMBITO 2', title=gYear)
        graphPie.append(gPC)
        year = year + 1

    return graphPie