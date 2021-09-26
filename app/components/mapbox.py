import pandas as pd
import plotly.express as px


class Model:
    '''Mapbox Plotly Figure Model'''
    def __init__(self, link: str, token: str) -> None:
        self.data = pd.read_csv(link)
        self.token = token

    def Figure(self) -> px.scatter_mapbox:
        px.set_mapbox_access_token(self.token)
        fig = px.scatter_mapbox(
                 self.data,
                 lat=self.data['Lat'],
                 lon=self.data['Lon'],
                 hover_name=self.data['Title'],
                 color=self.data['Condition'],
                 color_continuous_scale=px.colors.diverging.RdYlGn,
                 size=self.data['Impact'],
                 size_max=15,
                 zoom=1,
                 mapbox_style="satellite-streets",
              )
        fig["layout"]["height"] = 780
        fig["layout"].update(paper_bgcolor="#d9d9d9", plot_bgcolor="#d9d9d9")
        fig.update_layout(title_text='Earth\'s Current Events', title_x=0.5, title_font_color='#353535',
                          yaxis=dict(color='#353535'), xaxis=dict(color='#353535'))

        return fig
