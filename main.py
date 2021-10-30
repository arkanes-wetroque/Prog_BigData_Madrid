import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

from datasVehicules import TotalConsoByTypo
from functions import generate_table

app = dash.Dash(__name__)

"""
Phase de test inportation de la conso dataframe et insertion dans un grapgique
dash
"""
testDF = TotalConsoByTypo()


figureTest = px.bar(testDF,x= "Type", y=["2017", "2018", "2019"], barmode="group")


app.layout = html.Div(children=[
    html.H1(children='test'),
    html.Div(children='''
    Dash : test app vehicule type conso
    '''),

    html.Div(children=[
        dcc.Graph(
        id='test-graph',
        figure=figureTest
    ),
    html.H4(children='Datas by types'),
    generate_table(testDF)
    ])





])

if __name__ == '__main__':
    app.run_server(debug=True)
