import os
import pathlib

import pandas as pd

from app.util.links import OWID_COVID

url = OWID_COVID

c19_df = pd.read_csv(url)
world_c19_df = c19_df[c19_df['location'] == 'World']
world_c19_df = world_c19_df[['location', 'date', 'total_cases', 'new_cases',
                             'total_deaths', 'new_deaths']]


APP_PATH = str(pathlib.Path(__file__).parent.resolve())
world_c19_df.to_csv(os.path.join(APP_PATH, '../../data/covid/world_c19.csv'))
