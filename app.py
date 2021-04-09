# Importing Modules
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

# Initialize App
app = dash.Dash(
    __name__,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)
server = app.server

# Load data
APP_PATH = str(pathlib.Path(__file__).parent.resolve())
df = pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "dataset.csv")))
# Mapping
fig = px.scatter_mapbox(
        df,
        lat = df['lat'],
        lon = df['lon'],
        hover_name="description",
        zoom=1,
        mapbox_style="open-street-map",
    )
fig["layout"]["height"] = 780
fig["layout"].update(paper_bgcolor="#252e3f", plot_bgcolor="#252e3f")

# App layout
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
                    ]
                )
            ],
        ),
    ],
)
# Run Server
if __name__ == "__main__":
    app.run_server(debug=True)
