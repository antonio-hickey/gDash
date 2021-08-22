import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

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

ce_df = pd.read_csv(CE_DF)
c19_df = pd.read_csv(C19_DF)
gdp_df = pd.read_csv(GDP_DF)
pop_df = pd.read_csv(POP_DF)

px.set_mapbox_access_token(MAPBOX_TOKEN)
fig = px.scatter_mapbox(
        ce_df,
        lat=ce_df['Lat'],
        lon=ce_df['Lon'],
        hover_name=ce_df['Title'],
        color=ce_df['Condition'],
        color_continuous_scale=px.colors.diverging.RdYlGn,
        size=ce_df['Impact'],
        size_max=15,
        zoom=1,
        mapbox_style="satellite-streets",
    )
fig["layout"]["height"] = 780
fig["layout"].update(paper_bgcolor="#d9d9d9", plot_bgcolor="#d9d9d9")
fig.update_layout(title_text='Earth\'s Current Events', title_x=0.5, title_font_color='#353535',
                  yaxis=dict(color='#353535'), xaxis=dict(color='#353535'))


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
