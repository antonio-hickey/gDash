import pandas as pd

from app.util.links import OWID_COVID

url = OWID_COVID
c19_df = pd.read_csv(url)
world_c19_df = c19_df[c19_df['location'] == 'World']
world_c19_df = world_c19_df[['location', 'date', 'total_cases', 'new_cases',
                             'total_deaths', 'new_deaths']]

world_c19_df.to_csv('app/data/covid/world_c19.csv')
