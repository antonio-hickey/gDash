#-----------------------
# Free Access Token from https://www.mapbox.com/
#-----------------------
token = "*YOUR ACCESSS TOKEN*"
#-----------------------

#-----------------------
# Importing Modules
#-----------------------
import os
import pathlib
import re
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output, State
import cufflinks as cf
#-----------------------

#-----------------------
# Initialize App
#-----------------------
app = dash.Dash(
    __name__,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)
server = app.server
#-----------------------

#-----------------------
# Data
#-----------------------
# Current Path
APP_PATH = str(pathlib.Path(__file__).parent.resolve())

# Current Event's
ce_df = pd.read_csv(os.path.join(APP_PATH, os.path.join("data/events", "dataset.csv")))

#Covid Data
c19_df = pd.read_csv(os.path.join(APP_PATH, os.path.join("data/covid", "world_c19.csv")))
#-----------------------

#-----------------------
# Mapping
#-----------------------
px.set_mapbox_access_token(token)
fig = px.scatter_mapbox(
        ce_df,
        lat = ce_df['Lat'],
        lon = ce_df['Lon'],
        hover_name=ce_df["Description"],
        color=ce_df['Scale'],
        color_continuous_scale=px.colors.diverging.RdYlGn,
        size = ce_df['Size'],
        size_max=15,
        zoom=1,
        mapbox_style= "satellite-streets",
    )
fig["layout"]["height"] = 780
fig["layout"].update(paper_bgcolor="#d9d9d9", plot_bgcolor="#d9d9d9")
fig.update_layout(title_text='Earth\'s Current Events',title_x=0.5,title_font_color='#353535',
            yaxis=dict(color='#353535'),xaxis=dict(color='#353535'))
#-----------------------

#-----------------------
# Covid 19 Graphing
#-----------------------
c19fig = px.area(c19_df,x="date",y="total_deaths",color_discrete_sequence=['#3c6e71'])
c19fig["layout"][
    "uirevision"
] = "The User is always right"
c19fig["layout"]["height"] = 590
c19fig["layout"]["yaxis"]["title"] = 'Deaths'
c19fig["layout"]["xaxis"]["title"] = 'Dates'
c19fig["layout"]["yaxis"]["gridcolor"] = "#ffffff"
c19fig["layout"]["xaxis"]["gridcolor"] = "#ffffff"
c19fig.update_layout(legend=dict(font=dict(color="#353535")))
c19fig["layout"].update(paper_bgcolor="#ffffff", plot_bgcolor="#d9d9d9")
c19fig.update_yaxes(title_font=dict(color='#353535'))
c19fig.update_xaxes(title_font=dict(color='#353535'))
c19fig.update_layout(title_text='COVID-19 Death\'s Global',title_x=0.5,title_font_color='#353535',
            yaxis=dict(color='#353535'),xaxis=dict(color='#353535'))
#-----------------------

#-----------------------
# App layout
#-----------------------
app.layout = html.Div(
    id="root",
    children=[
        # Header
        html.Div(
            id="header",
            children=[
                html.Img(id="logo", src=app.get_asset_url("dash-logo.png")),
                html.H4(children="Observing Global Event's"),
                html.P(
                    id="description",
                    children="Leveraging Open Source Intelligence for keeping up with current event's around the world before they become history.",
                ),
            ],
        ),
        # Body
        html.Div(
            id="app-container",
            children=[
                html.Div(
                    id="left-column",
                    children=[
                        # Map
                        html.Div(
                            id="map_",
                            children=[
                                dcc.Graph(
                                    id="map",
                                    figure = fig
                                )   
                            ],
                        ),
                    ],
                ),
                # Graph
                html.Div(
                    id="graph-container",
                    children=[
                        # Dropdown menu
                        dcc.Dropdown(
                            options=[
                                {
                                    "label": "COVID-19", 
                                    "value": "covid",
                                },
                                {
                                    "label": "Economics",
                                    "value": "econ",
                                },
                                {
                                    "label": "Relationship's",
                                    "value": "relation",
                                },
                                {
                                    "label": "Recent Major Events",
                                    "value": "rme",
                                },
                            ],
                            value="covid",
                            id="chart-dropdown",
                        ),
                        html.Div(
                            id="data_graph",
                            children=[
                                dcc.Graph(
                                    id="data-graph",
                                    figure= c19fig
                                )
                            ]
                        )
                    ]
                )
            ],
        ),
    ],
)
#-----------------------

#-----------------------
# Run Server
#-----------------------
if __name__ == "__main__":
    app.run_server(debug=True)
#-----------------------
