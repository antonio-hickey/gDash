import pandas as pd
import plotly.express as px


def Figure(link_2_data: str) -> px.pie:
    data = pd.read_csv(link_2_data)

    fig = px.pie(data, values='Net Change', names='Country (or dependency)')
    fig["layout"][
        "uirevision"
    ] = "The User is always right"
    fig["layout"]["height"] = 590

    return fig
