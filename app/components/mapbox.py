import pandas as pd
import plotly.express as px


def figure(link_2_data: str, mapbox_token: str) -> px.scatter_mapbox:
    data = pd.read_csv(link_2_data)

    px.set_mapbox_access_token(mapbox_token)
    fig = px.scatter_mapbox(
             data,
             lat=data['Lat'],
             lon=data['Lon'],
             hover_name=data['Title'],
             color=data['Condition'],
             color_continuous_scale=px.colors.diverging.RdYlGn,
             size=data['Impact'],
             size_max=15,
             zoom=1,
             mapbox_style="satellite-streets",
          )
    fig["layout"]["height"] = 780
    fig["layout"].update(paper_bgcolor="#d9d9d9", plot_bgcolor="#d9d9d9")
    fig.update_layout(title_text='Earth\'s Current Events', title_x=0.5, title_font_color='#353535',
                      yaxis=dict(color='#353535'), xaxis=dict(color='#353535'))

    return fig
