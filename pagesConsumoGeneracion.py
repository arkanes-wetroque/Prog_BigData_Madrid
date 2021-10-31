
import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_table
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

from datasConsYCrea import getConso, getGenere, getDataByAmbito, getDataFrameByAmbito

c2018 = getConso(2018)
c2019 = getConso(2019)
c2020 = getConso(2020)
g2018 = getGenere(2018)
g2019 = getGenere(2019)
g2020 = getGenere(2020)

#For ambito analyse (variables


Conso2018Ambitio = getDataFrameByAmbito(2018, "Consumida")
Conso2019Ambitio = getDataFrameByAmbito(2019, "Consumida")
Conso2020Ambitio = getDataFrameByAmbito(2020, "Consumida")



ConsoAmbitioPerYear = pd.concat([Conso2018Ambitio,Conso2019Ambitio['count'],Conso2020Ambitio['count']], axis=1)
ConsoAmbitioPerYear.columns.values[1]= "2018"
ConsoAmbitioPerYear.columns.values[2]= "2019"
ConsoAmbitioPerYear.columns.values[3]= "2020"


print(ConsoAmbitioPerYear)

pie2018 = px.pie(ConsoAmbitioPerYear, values='2018', names='Ambito', title="Pie 2018 Consomacion per Ambito")



d = { 'Year': [2018, 2019, 2020], 'Consomation': [c2018, c2019, c2020],'Creation': [g2018, g2019, g2020]}
DataTableConsoGen = pd.DataFrame(data=d)


#par de consomation et creation par année
lineChartResum = px.line(DataTableConsoGen,x= "Year", y=["Consomation","Creation"], title="Test")

#par de consomation et creation par année
barChartAmbiConsum = px.bar(ConsoAmbitioPerYear,x= "Ambito", y=["2018","2019","2020"], barmode="group", title="Consomation de los Ambitos per year")

#trace1 = go.Bar(x=pv.index, y=pv[('Quantity', 'declined')], name='Declined')
diff = DataTableConsoGen["Consomation"] - DataTableConsoGen["Creation"]
DataTableConsoGen["difference"] = diff


def pageConsumoGeneracion():
    return html.Div(children=[
    html.H1(children='Type Consomation véhicule Madrid'),
    html.Div(children='''
    Message de tes
    '''),

    html.Div(children=[
        dcc.Graph(
        id='line-Resume',
        figure=lineChartResum
        ),
        html.Label("Table resumen en KWH"),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in DataTableConsoGen.columns],
            data=DataTableConsoGen.to_dict('records'),

        )
    ]),

        html.Div([
            html.Div([
                html.H3('Consomation 2018 per Ambitio'),
                dash_table.DataTable(
                    id='table2',
                    columns=[{"name": i, "id": i} for i in ConsoAmbitioPerYear.columns],
                    data=ConsoAmbitioPerYear.to_dict('records'),
                )
            ], className="six columns"),

            # A TRANSOFMER EN GENERADA
            html.Div([
                html.H3('Consomation 2018 per Ambitio'),
                dash_table.DataTable(
                    id='table2',
                    columns=[{"name": i, "id": i} for i in ConsoAmbitioPerYear.columns],
                    data=ConsoAmbitioPerYear.to_dict('records'),
                )
            ], className="six columns"),
        ], className="row"),



        html.Div(children=[
            dcc.Graph(
            id='test-graph2',
            figure=barChartAmbiConsum
            ),
        ]),

        html.Div(children=[
            dcc.Graph(
                id='test-graph22',
                figure=pie2018
            ),
        ]),

        html.Div([
            html.Div([
                html.H3('Column 1'),
                dcc.Graph(id='g1', figure={'data': [{'y': [1, 2, 3]}]})
            ], className="six columns"),

            html.Div([
                html.H3('Column 2'),
                dcc.Graph(id='g2', figure={'data': [{'y': [1, 2, 3]}]})
            ], className="six columns"),
        ], className="row")




    ])


