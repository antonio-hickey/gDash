# Importing Modules
import pathlib

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# Free Access Token from https://www.mapbox.com/
token = 'pk.eyJ1IjoiYWZoaWNrZXkiLCJhIjoiY2tuaG9xbXcwMHA4ZDJubDc0NGZ3dmVpYSJ9.dgDkc3Jyu19_DWd5qZq-TQ'


# Initialize App
app = dash.Dash(
    __name__,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"},
    ],
)
server = app.server


# Defining datasets
APP_PATH = str(pathlib.Path(__file__).parent.resolve())
ce_df = pd.read_csv('https://raw.githubusercontent.com/antonio-hickey/gDash/main/data/events/dataset.csv')
c19_df = pd.read_csv('https://raw.githubusercontent.com/antonio-hickey/gDash/main/data/covid/world_c19.csv')
gdp_df = pd.read_csv('https://raw.githubusercontent.com/antonio-hickey/gDash/main/data/economic/GDP/dataset.csv')
pop_df_link = "https://raw.githubusercontent.com/antonio-hickey/gDash/main/data/demographics/population_by_country_2020.csv"
pop_df = pd.read_csv(pop_df_link)


# Mapping
px.set_mapbox_access_token(token)
fig = px.scatter_mapbox(
        ce_df,
        lat=ce_df['Lat'],
        lon=ce_df['Lon'],
        hover_name=ce_df["Description"],
        color=ce_df['Scale'],
        color_continuous_scale=px.colors.diverging.RdYlGn,
        size=ce_df['Size'],
        size_max=15,
        zoom=1,
        mapbox_style="satellite-streets",
    )
fig["layout"]["height"] = 780
fig["layout"].update(paper_bgcolor="#d9d9d9", plot_bgcolor="#d9d9d9")
fig.update_layout(title_text='Earth\'s Current Events', title_x=0.5, title_font_color='#353535',
                  yaxis=dict(color='#353535'), xaxis=dict(color='#353535'))


# Covid 19 Graphing
c19fig = px.area(c19_df, x="date", y="total_deaths", color_discrete_sequence=['#3c6e71'])
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
c19fig.update_layout(title_text='COVID-19 Death\'s Global', title_x=0.5, title_font_color='#353535',
                     yaxis=dict(color='#353535'), xaxis=dict(color='#353535'))


# App layout
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
                                    figure=fig,
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
                                    "label": "Recent Major Events",
                                    "value": "rme",
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


# Callbacks


# Dropdown callback
@app.callback(
    Output("data-graph", "figure"),
    [
        Input("chart-dropdown", "value"),
    ],
)
def data_display(chart_dropdown):
    if chart_dropdown == "covid":
        c19fig = px.area(c19_df, x="date", y="total_deaths", color_discrete_sequence=['#3c6e71'])
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
        c19fig.update_layout(title_text='COVID-19 Death\'s Global', title_x=0.5,
                             title_font_color='#353535', yaxis=dict(color='#353535'),
                             xaxis=dict(color='#353535'))
        return c19fig

    if chart_dropdown == "econ":
        econFig = px.bar(gdp_df, x="Economy", y="value", color_discrete_sequence=['#3c6e71'])
        econFig["layout"][
            "uirevision"
        ] = "The User is always right"
        econFig["layout"]["height"] = 590
        econFig["layout"]["yaxis"]["title"] = 'Dollar\'s'
        econFig["layout"]["xaxis"]["title"] = 'Nation\'s'
        econFig["layout"]["yaxis"]["gridcolor"] = '#ffffff'
        econFig["layout"]["xaxis"]["gridcolor"] = '#ffffff'
        econFig.update_layout(legend=dict(font=dict(color="#353535")))
        econFig["layout"].update(paper_bgcolor="#ffffff", plot_bgcolor="#d9d9d9")
        econFig.update_yaxes(title_font=dict(color='#353535'))
        econFig.update_xaxes(title_font=dict(color='#353535'))
        econFig.update_layout(title_text='GDP of Top 20 Nation\'s', title_x=0.5,
                              title_font_color='#353535', yaxis=dict(color='#353535'),
                              xaxis=dict(color='#353535'))
        return econFig

    if chart_dropdown == "pop":
        relFig = px.pie(pop_df, values='Net Change', names='Country (or dependency)')
        relFig["layout"][
            "uirevision"
        ] = "The User is always right"
        relFig["layout"]["height"] = 590

        return relFig

    if chart_dropdown == "rme":
        rmeFig = px.area(c19_df, x="date", y="total_deaths", color_discrete_sequence=['#3c6e71'])
        rmeFig["layout"][
            "uirevision"
        ] = "The User is always right"
        rmeFig["layout"]["height"] = 590
        rmeFig["layout"]["yaxis"]["title"] = 'Deaths'
        rmeFig["layout"]["xaxis"]["title"] = 'Dates'
        rmeFig["layout"]["yaxis"]["gridcolor"] = '#ffffff'
        rmeFig["layout"]["xaxis"]["gridcolor"] = '#ffffff'
        rmeFig.update_layout(legend=dict(font=dict(color="#353535")))
        rmeFig["layout"].update(paper_bgcolor="#ffffff", plot_bgcolor="#d9d9d9")
        rmeFig.update_yaxes(title_font=dict(color='#353535'))
        rmeFig.update_xaxes(title_font=dict(color='#353535'))
        rmeFig.update_layout(title_text='Recent Major Events', title_x=0.5,
                             title_font_color='#353535', yaxis=dict(color='#353535'),
                             xaxis=dict(color='#353535'))
        return rmeFig


# Run Server
if __name__ == "__main__":
    app.run_server(debug=True)
