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

#--------------------------------------All function for init -------------------------------------------------------#

def getYearT(year1, year2): #Récup toute les dates et les mets dans une list (en int )
    year = []
    for yearR in range(year1, year2 + 1):
        y = yearR
        year.append(y)
        yearR = yearR+1
    return year

def getYearTs(year1, year2): #Récup toute les dates et les mets dans une list (en str)
    year = []
    for yearR in range(year1, year2 + 1):
        yS = yearR
        sYear = str(yS)
        year.append(sYear)
        yearR = yearR+1
    return year
# Permet de récup les valeurs pour le premier graph
#---------------------------------------------\/-------------------------------------------------------
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
#---------------------------------------------/\-------------------------------------------------------

# Permet de récup les valeurs pour le deux tableau (1) et gère la taille du tableau en fonction du nombre d'année sélec (2)
# et les mets dans une list (3)
#---------------------------------------------\/-------------------------------------------------------

def getConsoAmbitioT(year1, year2):
    consoAmbi = []
    i = 1
    count = year2-year1
    print(count)

    #1
    for year in range(year1, year2 + 1):
        cA = getDataFrameByAmbito(year, "Consumida")
        consoAmbi.append(cA)
        year = year+1
        print("------1------")
        print(cA)

    if count == 2:
        a = consoAmbi[0]
        b = consoAmbi[1]
        c = consoAmbi[2]

    else:
        a = consoAmbi[0]
        b = consoAmbi[1]
    #3
    if count == 2:
        cAT = pd.concat([a, b['count'], c['count']], axis=1)
        test = cAT

    else:
        cAT = pd.concat([cA, cA['count']], axis=1)
        test = cAT
    #3
    for year in range(year1, year2 + 1):
        sYear = str(year)
        cAT.columns.values[i] = sYear
        i = i+1

    print("------2------")
    print(cAT)
    print("------3------")
    print(test)

    return cAT

def getGeneAmbitioT(year1, year2):
    i = 1
    count = year2 - year1
    geneAmbi = []

    #1
    for year in range(year1, year2 + 1):
        gA = getDataFrameByAmbito(year, "Generada")
        geneAmbi.append(gA)
        year = year+1

    if count == 2:
        a = geneAmbi[0]
        b = geneAmbi[1]
        c = geneAmbi[2]

    else:
        a = geneAmbi[0]
        b = geneAmbi[1]
    #3
    if count == 2:
        cAT = pd.concat([a, b['count'], c['count']], axis=1)
        test = cAT

    else:
        cAT = pd.concat([cA, cA['count']], axis=1)
        test = cAT

    #3
    for year in range(year1, year2 + 1):
        sYear = str(year)
        cAT.columns.values[i] = sYear
        i = i + 1
    return cAT
#---------------------------------------------/\-------------------------------------------------------

# Init les derniers graphs à la base je voulais générer le bon nombre de graphs mais j'ai un pb avoir ???

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