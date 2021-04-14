import pandas as pd
import datetime as dt
import pathlib
import json
import os
#-----------------------------
# Covid Data
#-----------------------------
url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
c19_df = pd.read_csv(url)
world_c19_df = c19_df[c19_df['location']=='World']
world_c19_df = world_c19_df[['location','date','total_cases','new_cases','total_deaths','new_deaths']]
# Export to csv
APP_PATH = str(pathlib.Path(__file__).parent.resolve())
world_c19_df.to_csv(os.path.join(APP_PATH, 'world_c19.csv'))
#-----------------------------