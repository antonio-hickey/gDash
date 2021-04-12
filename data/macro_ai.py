import pandas as pd
import pathlib
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Covid Data
url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
print(bcolors.OKCYAN+'Handling dataset... May take a couple minutes...' + bcolors.ENDC)
c19_df = pd.read_csv(url)
world_c19_df = c19_df[c19_df['location']=='World']
world_c19_df = world_c19_df[['location','date','total_cases','new_cases','total_deaths','new_deaths']]

# Export to csv
APP_PATH = str(pathlib.Path(__file__).parent.resolve())
world_c19_df.to_csv(os.path.join(APP_PATH, 'world_c19.csv'))

print(bcolors.OKGREEN + 'worked!' +bcolors.ENDC)

