import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app.components import covid, economics, mapbox, population
from app.config import MAPBOX_TOKEN
from app.util.links import C19_DF, CE_DF, GDP_DF, POP_DF

application = dash.Dash(
    __name__,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"},
    ],
)
server = application.server
app = application

app.layout = html.Div(
    id="root",
    children=[
        html.Div(
            id="header",
            children=[
                html.Img(id="logo", src=app.get_asset_url("dash-logo.png")),
                html.H4(children="Observing Global Event's"),
                html.P(
                    id="description",
                    children="Leveraging Open Source Intelligence for keeping up with current event's around the world.",
                ),
            ],
        ),
        html.Div(
            id="app-container",
            children=[
                html.Div(
                    id="left-column",
                    children=[
                        html.Div(
                            id="map_",
                            children=[
                                dcc.Graph(
                                    id="map",
                                    figure=mapbox.Model(CE_DF, MAPBOX_TOKEN).Figure(),
                                ),
                            ],
                        ),
                    ],
                ),
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
                                    "label": "Population Data",
                                    "value": "pop",
                                },
                                {
                                    "label": "Upcoming Elections",
                                    "value": "elec",
                                },
                            ],
                            value="econ",
                            id="chart-dropdown",
                        ),
                        html.Div(
                            id="data_graph",
                            children=[
                                dcc.Graph(
                                    id="data-graph",
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ],
)


@app.callback(
    Output("data-graph", "figure"),
    [
        Input("chart-dropdown", "value"),
    ],
)
def data_display(chart_dropdown):
    if chart_dropdown == "covid":
        return covid.Model(C19_DF).Figure()
    elif chart_dropdown == "econ":
        return economics.Model(GDP_DF).Figure()
    elif chart_dropdown == "pop":
        return population.Model(POP_DF).Figure()
    elif chart_dropdown == "elec":
        # TODO (just a placeholder for now)
        return covid.Model(C19_DF).Figure()
