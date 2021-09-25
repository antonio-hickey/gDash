import pandas as pd
import plotly.express as px


class Model:
    def __init__(self, link: str) -> None:
        self.data = pd.read_csv(link)

    def Figure(self) -> px.bar:
        data = self.data

        fig = px.bar(data, x="Economy", y="value", color_discrete_sequence=['#3c6e71'])
        fig["layout"][
            "uirevision"
        ] = "The User is always right"
        fig["layout"]["height"] = 590
        fig["layout"]["yaxis"]["title"] = 'Dollar\'s'
        fig["layout"]["xaxis"]["title"] = 'Nation\'s'
        fig["layout"]["yaxis"]["gridcolor"] = '#ffffff'
        fig["layout"]["xaxis"]["gridcolor"] = '#ffffff'
        fig.update_layout(legend=dict(font=dict(color="#353535")))
        fig["layout"].update(paper_bgcolor="#ffffff", plot_bgcolor="#d9d9d9")
        fig.update_yaxes(title_font=dict(color='#353535'))
        fig.update_xaxes(title_font=dict(color='#353535'))
        fig.update_layout(title_text='GDP of Top 20 Nation\'s', title_x=0.5,
                          title_font_color='#353535', yaxis=dict(color='#353535'),
                          xaxis=dict(color='#353535'))
        return fig
