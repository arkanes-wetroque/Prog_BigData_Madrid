import pandas as pd


# This file will be the data getter and washer


def processTotal(file, date):
    datas = pd.read_csv(file, delimiter=';', encoding= 'latin1')
    datas.drop_duplicates()
    datas = datas.iloc[:, 0:7]
    datas.columns = ['Num', 'Area', 'Direction', 'Uso', 'Vehicule', 'Juridique', 'Energie']
    
    #Fix Energie name
    datas['Energie'] = datas['Energie'].replace(['ELÃ\x89CTRICO', 'GASOLINA / HIBRIDO', 'ELÃ\x89CTRICO / HÃ\x8dBRIDO', 'ELÃ\x89CTRICO/GASOLINA', 'GAS NATURAL COMPRIMIDO', 'GAS LICUADO DE PETROLEO', 'DIESEL '],
                                                ['ELÉCTRICO', 'GASOLINA/HIBRIDO', 'ELÉCTRICO / HÍBRIDO', 'ELÉCTRICO/GASOLINA', 'GNC', 'GLP', 'DIESEL'])
    
    #Fix Uso name
    datas['Uso'] = datas['Uso'].replace(['incidencias', 'OPERATIVOS', 'INCIDENCIAS ', 'OPERATIVO ', 'FORMACIÃ\x93N', 'ADMINISTRATIVO ', 'AD/ REPRESENTACIÃ\x93N', 'REPRESENTACIÃ\x93N', 'EXPOSICIÃ\x93N'],
                                                ['INCIDENCIAS', 'OPERATIVO', 'INCIDENCIAS', 'OPERATIVO', 'FORMACIÓN', 'ADMINISTRATIVO', 'AD/ REPRESENTACIÓN', 'REPRESENTACIÓN', 'EXPOSICIÓN'])
    
    #Fix Vehicule name
    datas['Vehicule'] = datas['Vehicule'].replace(['FURGONETA ', 'TODO TERRENO ', 'turismo', 'CAMIÃ\x93N', 'VEHÃ\x8dCULO EMERGENCIAS', 'VEHÃ\x8dCULO ESPECIAL', 'AUTOBÃ\x9aS', 'CAMIÃ\x93N BASURA', 'AUTOBÃ\x9aS TURISTICO'],
                                                ['FURGONETA', 'TODO TERRENO', 'TURISMO', 'CAMIÓN', 'VEHÍCULO EMERGENCIAS', 'VEHÍCULO ESPECIAL', 'AUTOBUS', 'CAMIÓN BASURA', 'AUTOBUS TURISTICO'])   
    
    datas['Date'] = date
    return datas


def fusionDF(df1, df2, df3, df4, df5):
    datas = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)
    return datas