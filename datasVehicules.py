import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce

# This file will be the data getter and washer



def VDataFClassB(file):
    df = pd.read_csv(file, delimiter=';')
    df = df.drop_duplicates()
    #df = df.drop(df.columns[[1, 3,5,7,8,9,10]], axis=1)
    df = df[['Nº MPAL','DIRECCIÓN GENERAL O SERVICIO DE ADSCRIPCIÓN','TIPO VEHICULO','ENERGÍA/COMBUSTIBLE']]
    df['ENERGÍA/COMBUSTIBLE'] = df['ENERGÍA/COMBUSTIBLE'].replace(['DIESEL '],['DIESEL'])
    indexToSupp = df[ df['ENERGÍA/COMBUSTIBLE'] == 'No precisa' ].index
    df.drop(indexToSupp, inplace=True)
    return df


def VDataFClassA(file):
    df = pd.read_csv(file, delimiter=';')
    df = df.drop_duplicates()
    df = df.drop(df.columns[[1, 3,5]], axis=1)
    df = df.rename(columns={df.columns[0]: 'Nº MPAL', df.columns[1]: 'DIRECCIÓN GENERAL O SERVICIO DE ADSCRIPCIÓN', df.columns[3]:'ENERGÍA/COMBUSTIBLE' })
    df['DIRECCIÓN GENERAL O SERVICIO DE ADSCRIPCIÓN'] = df['DIRECCIÓN GENERAL O SERVICIO DE ADSCRIPCIÓN'].replace(['D.G. EMERGENCIAS Y PROTECCI�N CIVIL','D.G. DE GESTI�N Y VIGILANCIA DE LA CIRCULACI�N','D.G. GESTI�N DEL AGUA Y ZONAS VERDES'],['D.G. EMERGENCIAS Y PROTECCION CIVIL','D.G. GESTION Y VIGILANCIA DE LA CIRCULACION','D.G. GESTION DEL AGUA Y ZONAS VERDES'])
    df = df[['Nº MPAL','DIRECCIÓN GENERAL O SERVICIO DE ADSCRIPCIÓN','TIPO VEHICULO','ENERGÍA/COMBUSTIBLE']]
    df['TIPO VEHICULO'] = df['TIPO VEHICULO'].replace(['CAMI�N','VEH�CULO ESPECIAL'],['CAMIÓN','VEHICULO ESPECIAL'])
    df['ENERGÍA/COMBUSTIBLE'] = df['ENERGÍA/COMBUSTIBLE'].replace(['EL�CTRICO'],['ELÉCTRICO'])
    df['ENERGÍA/COMBUSTIBLE'] = df['ENERGÍA/COMBUSTIBLE'].replace(['DIESEL '],['DIESEL'])
    return df


def Value_Counts(dataframe, byColumn, name1, name2):
    dc = dataframe[byColumn].value_counts().rename_axis(name1).reset_index(name=name2)
    return dc

def Value_Counts1(dataframe, byColumn):
    dc = dataframe[byColumn].value_counts()
    return dc
