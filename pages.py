import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_table
import dash_bootstrap_components as dbc
from datasVehicules import TotalConsoByTypo


DFConsoTypeTotal = TotalConsoByTypo()
figureConsoTotal = px.bar(DFConsoTypeTotal,x= "Type", y=["2017", "2018", "2019","2020","2021"], barmode="group")


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
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in DFConsoTypeTotal.columns],
            data=DFConsoTypeTotal.to_dict('records'),
        )
    ])
    ])

