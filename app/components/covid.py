import plotly.express as px
from typing import TypeVar
import pandas as pd


px_Figure = TypeVar('plotly.graph_objs._figure.Figure')

def Figure(link_2_data: str) -> px_Figure:
    data = pd.read_csv(link_2_data)
    
    fig = px.area(data, x="date", y="deaths weekly change", color_discrete_sequence=['#3c6e71'])

    fig.add_scatter(
     x=data["date"],
     y=data["+2 Sigma"],
     mode='lines',
     line=dict(color='#d40f33'),
     name='+4 Sigma',
    )

    fig.add_scatter(
     x=data["date"],
     y=data["-2 Sigma"],
     mode='lines',
     line=dict(color='#edac15'),
     name='+2 Sigma',
    )

    fig["layout"][
         "uirevision"
    ] = "The User is always right"
    fig["layout"]["height"] = 590
    fig["layout"]["yaxis"]["title"] = 'Change in Deaths'
    fig["layout"]["xaxis"]["title"] = 'Dates'
    fig["layout"]["yaxis"]["gridcolor"] = "#ffffff"
    fig["layout"]["xaxis"]["gridcolor"] = "#ffffff"
    fig.update_layout(legend=dict(font=dict(color="#353535")))
    fig["layout"].update(paper_bgcolor="#ffffff", plot_bgcolor="#d9d9d9")
    fig.update_yaxes(title_font=dict(color='#353535'))
    fig.update_xaxes(title_font=dict(color='#353535'))
    fig.update_layout(title_text='COVID-19 Change in Deaths', title_x=0.5,
                         title_font_color='#353535', yaxis=dict(color='#353535'),
                         xaxis=dict(color='#353535'))
    return fig
