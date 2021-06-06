<<<<<<< HEAD
=======
#!/bin/usr/python
import pandas as pd
import datetime as dt
import pathlib
>>>>>>> 0aa399242d597fe2aca3be70396a3d072e4a80a4
import os
import pathlib

import pandas as pd

# Url of dataset
url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'


# Render DataFrame
c19_df = pd.read_csv(url)


# Filter data to world data
world_c19_df = c19_df[c19_df['location'] == 'World']


# Cleaning dataset to targeted data
world_c19_df = world_c19_df[['location', 'date', 'total_cases', 'new_cases',
                             'total_deaths', 'new_deaths']]


# Export to csv
os.chdir(os.path.dirname(__file__))
APP_PATH = str(pathlib.Path(__file__).parent.resolve())
world_c19_df.to_csv(os.path.join(APP_PATH, 'world_c19.csv'))
<<<<<<< HEAD
=======
#-----------------------------
>>>>>>> 0aa399242d597fe2aca3be70396a3d072e4a80a4
