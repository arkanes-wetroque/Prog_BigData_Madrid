import dash
import pandas as pd
import dash_core_components as dcc
from dash import html
import plotly.express as px
import dash_table
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

from datasVehicules import processTotal, fusionDF

"""Valiables Page 1 Tipo   recrerrr un DF en ajoutant les données pour pivot """
fileV2017 = 'Datas/VEHICULOS_PARQUE_MOVIL_2017.csv'
fileV2018 = 'Datas/VEHICULOS_PARQUE_MOVIL_2018.csv'
fileV2019 = 'Datas/VEHICULOS_PARQUE_MOVIL_2019.csv'
fileV2020 = 'Datas/VEHICULOS_PARQUE_MOVIL_2020.csv'
fileV2021 = 'Datas/VEHICULOS_PARQUE_MOVIL_2021.csv'

dfV17 = processTotal(fileV2017,"2017")
dfV18 = processTotal(fileV2018,"2018")
dfV19 = processTotal(fileV2019,"2019")
dfV20 = processTotal(fileV2020,"2020")
dfV21 = processTotal(fileV2021,"2021")

dataframeTotal = fusionDF(dfV17, dfV18, dfV19, dfV20, dfV21)
print(dataframeTotal)


# Not used cuz in test , Blocked by concat atm need to concat without losing row values
groupEnergie=dataframeTotal.groupby(["Energie", "Date"])['Num']
dataEnergie = groupEnergie.size().reset_index(name='counts')
#






figureConsoTotal = px.bar(dataEnergie,x= "Energie", y= "counts", color="Date", barmode="group")
#figureConsoTotal2017 = px.bar(countTipo17,x= "Tipo", y="count", barmode="group")






def pageTypeConso():
    return html.Div(children=[
    html.H1(children='Type Consomation véhicule Madrid'),
    html.Div(children='''
    Message de tes
    '''),

    html.Div(children=[
        dcc.Graph(
        id='test-graph',
        figure=figureConsoTotal
        ),
    ])
    ])



