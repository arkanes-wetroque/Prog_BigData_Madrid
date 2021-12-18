


import dash_core_components as dcc
from dash import html
import plotly.express as px
from datasFotos import dfFotoAll

dfAll = dfFotoAll()
totalFoto = dfAll.shape[0] # get total

#Analyse by buisness
group=dfAll.groupby(["Empresa"])
groupEmpresa = group.size().reset_index(name='counts')
#Analyse by use
usos=dfAll.groupby(["Uso"])
groupUsos = usos.size().reset_index(name='counts')


fig = px.scatter_mapbox(dfAll, lat="Latitud", lon="Longitud", hover_name="Centro", hover_data=["DateInst", "Uso"],
                        color_discrete_sequence=["fuchsia"], zoom=10, height=300)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

pieEmpresa = px.pie(groupEmpresa, values='counts', names='Empresa', title="Instalaciones por empresa (Gráfico circular)")
bar1 = px.bar(groupEmpresa, x="Empresa", y="counts",barmode="group", title="Instalaciones por empresa (Gráfico de barras)")
barUsos = px.bar(groupUsos, x="Uso", y="counts",barmode="group", title="Instalaciones por uso (Gráfico de barras)")

def pageFotos():
    return html.Div(children=[
    html.H1(children='Inventario de los instalaciones fotovoltaicas de Madrid'),
    html.Div(children='''
    Datos de data.gob.es
    '''),

    html.Div([
        html.Div([
            dcc.Graph(id='g2', figure=fig)
        ], className="row"),
    ]),
    html.Div([
        html.H3("Número de instalaciones : %d " % (totalFoto))
    ]),

    html.Div([
        html.Div([
            dcc.Graph(id='EmpresaPie',
                      figure=pieEmpresa)
        ], className="six columns"),
        html.Div([
            dcc.Graph(id='bar1',
                      figure=bar1)
        ], className="six columns"),

    ], className="row"),
    html.Div([
        dcc.Graph(id='bar1Uso',
                  figure=barUsos)
    ], className="six columns"),




    ])