import dash
import dash_core_components as dcc
from dash import html
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

import pandas as pd




#VARIABLES
from pagesConsumoGeneracion import pageConsumoGeneracion
from pagesFotos import pageFotos
from pagesVehicules import pageTypeConso


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Pelegrino", className="display-4"),
        html.Hr(),
        html.P(
            "Projecto de Big Data UPM ", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("El parque movil", href="/", active="exact"),
                dbc.NavLink("instalaciones fotovoltaicas", href="/page-1", active="exact"),
                dbc.NavLink("Consumo y géneracion Madrid", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)





app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return pageTypeConso()
    elif pathname == "/page-1":
        return pageFotos()
    elif pathname == "/page-2":
        return pageConsumoGeneracion()
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )



if __name__ == '__main__':
    app.run_server(debug=True)
