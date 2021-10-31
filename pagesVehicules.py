import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_table
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

from datasVehicules import VDataFClassA, VDataFClassB, Value_Counts, Value_Counts1

"""Valiables Page 1 Tipo   recrerrr un DF en ajoutant les données pour pivot """
fileV2017 = 'Datas/VEHICULOS_PARQUE_MOVIL_2017.csv'
fileV2018 = 'Datas/VEHICULOS_PARQUE_MOVIL_2018.csv'
fileV2019 = 'Datas/VEHICULOS_PARQUE_MOVIL_2019.csv'
fileV2020 = 'Datas/VEHICULOS_PARQUE_MOVIL_2020.csv'
fileV2021 = 'Datas/VEHICULOS_PARQUE_MOVIL_2021.csv'

dfV17 = VDataFClassA(fileV2017)
dfV18 = VDataFClassA(fileV2018)
dfV19 = VDataFClassA(fileV2019)
dfV20 = VDataFClassB(fileV2020)
dfV21 = VDataFClassB(fileV2021)


countTipo17 = Value_Counts(dfV17,'ENERGÍA/COMBUSTIBLE', 'Tipo','count' )
countTipo18 = Value_Counts(dfV18,'ENERGÍA/COMBUSTIBLE', 'Tipo','count' )
countTipo19 = Value_Counts(dfV19,'ENERGÍA/COMBUSTIBLE', 'Tipo','count' )
countTipo20 = Value_Counts(dfV20,'ENERGÍA/COMBUSTIBLE', 'Tipo','count' )
countTipo21 = Value_Counts(dfV21,'ENERGÍA/COMBUSTIBLE', 'Tipo','count' )



# Not used cuz in test , Blocked by concat atm need to concat without losing row values
#dfTotalCountTipo = pd.concat([dfV17, dfV18, dfV19, dfV20, dfV21, ]).value_counts()

#dfTotalCountTipo






figureConsoTotal2021 = px.bar(countTipo21,x= "Tipo", y="count", barmode="group")
figureConsoTotal2017 = px.bar(countTipo17,x= "Tipo", y="count", barmode="group")






def pageTypeConso():
    return html.Div(children=[
    html.H1(children='Type Consomation véhicule Madrid'),
    html.Div(children='''
    Message de tes
    '''),

    html.Div(children=[
        dcc.Graph(
        id='test-graph',
        figure=figureConsoTotal2017
        ),





    ])])



