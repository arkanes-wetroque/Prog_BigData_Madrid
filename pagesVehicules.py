import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_table
import dash_bootstrap_components as dbc

from datasVehicules import VDataFClassA, VDataFClassB, Value_Counts, Value_Counts1

"""Valiables Page 1 Tipo """
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

dfV17['Year'] = '2017'
dfV18['Year'] = '2018'
dfV19['Year'] = '2019'
dfV20['Year'] = '2020'
dfV21['Year'] = '2021'




# Not used cuz in test , Blocked by concat atm need to concat without losing row values
dfTotalCountTipo = pd.concat([dfV17,
                              dfV18,
                              dfV19,
                              dfV20,
                              dfV21,
                              ])





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


        html.Div(children=[
            dcc.Graph(
                id='test-graph',
                figure=figureConsoTotal2021
            ),
        ]),

        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in dfTotalCountTipo.columns],
            data=dfTotalCountTipo.to_dict('records'),
        ),
    ])])



