import pandas as pd



file = 'Datas/inventario_instalaciones_fotovoltaicas_2021.csv'
df = pd.read_csv(file, delimiter=';',
                 usecols = ['Centro','Latitud','Longitud','Uso del edificio', 'Potencia KWp', 'Empresa instaladora', 'Puesta en servicio'])


def dfFotoAll():
    dc = df.rename(columns={'Uso del edificio': 'Uso', 'Potencia KWp': 'Potencia', 'Empresa instaladora': 'Empresa',
                            'Puesta en servicio': 'DateInst'})
    dc['Latitud'] = pd.to_numeric(dc['Latitud'])
    dc['Longitud'] = pd.to_numeric(dc['Longitud'])
    return dc