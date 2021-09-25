import pandas as pd
import plotly.express as px


class Model:
    def __init__(self, link: str) -> None:
        self.data = pd.read_csv(link)

    def render(self) -> pd.DataFrame:
        df = self.data
        date = df['date']
        deaths = df['new_deaths']
        up_sigma = deaths.rolling(7).std().rolling(28).mean() * 4
        down_sigma = deaths.rolling(7).std().rolling(28).mean() * 2
        return pd.DataFrame({
            'date': date,
            'new deaths': deaths,
            '+4 Sigma': up_sigma,
            '+2 Sigma': down_sigma,
        })

    def Figure(self) -> px.area:
        data = self.render()
        fig = px.area(data, x="date", y="new deaths", color_discrete_sequence=['#3c6e71'])

        fig.add_scatter(
         x=data["date"],
         y=data["+4 Sigma"],
         mode='lines',
         line=dict(color='#d40f33'),
         name='+4 Sigma',
        )

        fig.add_scatter(
         x=data["date"],
         y=data["+2 Sigma"],
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
