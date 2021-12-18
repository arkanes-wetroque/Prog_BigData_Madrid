

#TODO - Work out on the new way of process used with Data vehicules

import pandas as pd
from dash import dcc
from dash import html
import plotly.express as px
from dash import dash_table

from datasConsYCrea import getConsoT, getGeneT, getConsoAmbitioT, getGeneAmbitioT, getYearT, getYearTs, graphPieGen

#Init
rYear = getYearT(2018, 2020)
sYear = getYearTs(2018, 2020)
rConsoT = getConsoT(2018, 2020)
rGeneT = getGeneT(2018, 2020)
rConsoAmbitioT = getConsoAmbitioT(2018, 2020)
rGeneAmbitioT = getGeneAmbitioT(2018, 2020)
rGraphPie = graphPieGen()


d = {'Year': rYear, 'Consomation': rConsoT, 'Creation': rGeneT}
DataTableConsoGen = pd.DataFrame(data=d)


#par de consomation et creation par année
lineChartResum = px.line(DataTableConsoGen,x= "Year", y=["Consomation","Creation"], title="Test")

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
    Select date range
    '''),
        #--- Modif il faut récup la value voir avec un @app.callback ??????
        html.Div([
            dcc.RangeSlider(
                min=2018,
                max=2020,
                value=[2018, 2020],
                tooltip={"placement": "bottom", "always_visible": True}
            )
        ]),


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
