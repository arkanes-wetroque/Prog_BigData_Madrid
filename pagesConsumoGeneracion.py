

#TODO - Work out on the new way of process used with Data vehicules

import pandas as pd
from dash import dcc
from dash import html
import plotly.express as px
from dash import dash_table

from datasConsYCrea import getConsoT, getGeneT, getConsoAmbitioT, getGeneAmbitioT, getYearT, getYearTs, graphPieGen, getConsoAmbitioT1

#Init
Y1 = 2018
Y2 = 2020
rYear = getYearT(Y1, Y2)
sYear = getYearTs(Y1, Y2)
rConsoT = getConsoT(Y1, Y2)
rGeneT = getGeneT(Y1, Y2)
rConsoAmbitioT = getConsoAmbitioT(Y1, Y2)
rConsoAmbitioT1 = getConsoAmbitioT1(Y1, Y2)
rGeneAmbitioT = getGeneAmbitioT(Y1, Y2)
rGraphPie = graphPieGen()


d = {'Year': rYear, 'Consomation': rConsoT, 'Creation': rGeneT}
DataTableConsoGen = pd.DataFrame(data=d)


#par de consomation et creation par année
lineChartResum = px.line(DataTableConsoGen,x= "Year", y=["Consomation","Creation"], title="Consomation y generacion per Ano per Ambitio")

#par de consomation et creation par année
barChartAmbiConsum = px.bar(rConsoAmbitioT,x= "Ambito", y=sYear, barmode="group", title="Consomation de los Ambitos per year")
barChartAmbiGene = px.bar(rGeneAmbitioT,x= "Ambito", y=sYear, barmode="group", title="Consomation de los Ambitos per year")

#trace1 = go.Bar(x=pv.index, y=pv[('Quantity', 'declined')], name='Declined')
diff = DataTableConsoGen["Consomation"] - DataTableConsoGen["Creation"]
DataTableConsoGen["difference"] = diff


def pageConsumoGeneracion():
    return html.Div(children=[
    html.H1(children='Consomation y generation energia Madrid'),
    html.Div(children='''
    Nuestro conjunto de datos procede de datos.madrid.es.
    '''),
    html.H3(children='Resumen'),
    html.Div('''
    El objetivo es analizar el consumo y la producción de energía a lo largo de 3 años para el conjunto del 
    municipio de Madrid con el fin de interpretar los cambios, destacar la "zona" que más consume y produce 
    con el tipo de producción utilizado. Gracias a este análisis, podremos destacar las diferentes tendencias 
    de cambio (hacia una producción más ecológica, por ejemplo).  
    '''),

        html.Div(children=[        # Premier Graph
        dcc.Graph(
        id='line-Resume',
        figure=lineChartResum),

        html.Label("Table resumen en KWH"),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in DataTableConsoGen.columns],
            data=DataTableConsoGen.to_dict('records'),
        )
    ]),

    html.Div([                   # Deuxieme avec 2 graph
        html.Div([
            html.H3('Consomation per Ano per Ambitio'),
            dash_table.DataTable(
                id='table2',
                columns=[{"name": i, "id": i} for i in rConsoAmbitioT.columns],
                data=rConsoAmbitioT.to_dict('records'),
            )
        ], className="six columns"),
        # A TRANSOFMER EN GENERADA
        html.Div([
            html.H3('Generacion per Ano per Ambitio'),
            dash_table.DataTable(
                id='table2',
                columns=[{"name": i, "id": i} for i in rGeneAmbitioT.columns],
                data=rGeneAmbitioT.to_dict('records'),
            )
        ], className="six columns"),
    ], className="row"),

        html.Div(children=[
            dcc.Graph(
            id='test-graph2',
            figure=barChartAmbiConsum
            ),
        ]),

        #TODO - Wait for the new way of processing then make a big graph about the kind of generation per year.
        html.H1(children='Generacion de energia per manera'),

        html.Div([
            html.Div([
                dcc.Graph(id='test-graph22',
                figure=rGraphPie[0])
            ], className="six columns"),
            html.Div([
                dcc.Graph(id='test-graph22',
                          figure=rGraphPie[1])
            ], className="six columns"),
            html.Div([
                dcc.Graph(id='test-graph22',
                          figure=rGraphPie[2])
            ], className="six columns"),
        ], className="row"),
    ])
