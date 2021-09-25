import pandas as pd
import plotly.express as px


class Model:
    def __init__(self, link: str) -> None:
        self.data = pd.read_csv(link)

    def Figure(self) -> px.pie:
        fig = px.pie(self.data, values='Net Change', names='Country (or dependency)')
        fig["layout"][
            "uirevision"
        ] = "The User is always right"
        fig["layout"]["height"] = 590

        return fig
