


import dash_core_components as dcc
from dash import html
import plotly.express as px
from datasFotos import dfFotoAll

dfAll = dfFotoAll()
totalFoto = dfAll.shape[0]

group=dfAll.groupby(["Empresa"])
groupEmpresa = group.size().reset_index(name='counts')

usos=dfAll.groupby(["Uso"])
groupUsos = usos.size().reset_index(name='counts')


fig = px.scatter_mapbox(dfAll, lat="Latitud", lon="Longitud", hover_name="Centro", hover_data=["DateInst", "Uso"],
                        color_discrete_sequence=["fuchsia"], zoom=10, height=300)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

pieEmpresa = px.pie(groupEmpresa, values='counts', names='Empresa', title="Instalation per Empresa")
bar1 = px.bar(groupEmpresa, x="Empresa", y="counts",barmode="group")
barUsos = px.bar(groupUsos, x="Uso", y="counts",barmode="group")

def pageFotos():
    return html.Div(children=[
    html.H1(children='Inventorio de los instalaciones fotovoltaicas de Madrid'),
    html.Div(children='''
    
    '''),

    html.Div([
        html.Div([
            dcc.Graph(id='g2', figure=fig)
        ], className="row"),
    ]),
    html.Div([
        html.H3("Numbre total de instalaciones : %d " % (totalFoto))
    ]),

    html.Div([
        html.Div([
            dcc.Graph(id='test-graph22',
                      figure=pieEmpresa)
        ], className="six columns"),
        html.Div([
            dcc.Graph(id='test-graph22',
                      figure=bar1)
        ], className="six columns"),

    ], className="row"),
    html.Div([
        dcc.Graph(id='test-graph22',
                  figure=barUsos)
    ], className="six columns"),




    ])