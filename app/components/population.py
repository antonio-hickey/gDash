import plotly.express as px
from typing import TypeVar
import pandas as pd


px_Figure = TypeVar('plotly.graph_objs._figure.Figure')

def Figure(link_2_data: str) -> px_Figure:
    data = pd.read_csv(link_2_data)
    
    fig = px.pie(data, values='Net Change', names='Country (or dependency)')
    fig["layout"][
        "uirevision"
    ] = "The User is always right"
    fig["layout"]["height"] = 590

    return fig
