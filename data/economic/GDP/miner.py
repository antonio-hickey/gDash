# Using the World Bank API for sourcing global economic data
#----------------------------
# Importing Modules
import wbgapi as wb
import pandas as pd
#----------------------------

# Null lists of target output data
nations = []
value = []

# Fetching most recent GDP data for top 20 nations
for row in wb.data.fetch('NY.GDP.MKTP.CD',economy=['USA','CHN','JPN','DEU','GBR','IND',
    'FRA','ITA','CAN','KOR','RUS','AUS','BRA','ESP','MEX','IDN','NLD','CHE','SAU','TUR'],mrv=1):
    
    # Cleaning datai
    for x in row: # Dict Structure {value: x, series: x, economy: x, aggergate: x, time: x}
        if x == 'value':
            value.append(row[x])
        if x == 'economy':
            if row[x] == 'USA':
                nations.append('United States')
            if row[x] == 'CHN':
                nations.append('China')
            if row[x] == 'JPN':
                nations.append('Japan')
            if row[x] == 'DEU':
                nations.append('Germany')
            if row[x] == 'GBR':
                nations.append('United Kingdom')
            if row[x] == 'IND':
                nations.append('India')
            if row[x] == 'FRA':
                nations.append('France')
            if row[x] == 'ITA':
                nations.append('Italy')
            if row[x] == 'CAN':
                nations.append('Canada')
            if row[x] == 'KOR':
                nations.append('South Korea')
            if row[x] == 'RUS':
                nations.append('Russia')
            if row[x] == 'AUS':
                nations.append('Australia')
            if row[x] == 'BRA':
                nations.append('Brazil')
            if row[x] == 'ESP':
                nations.append('Spain')
            if row[x] == 'MEX':
                nations.append('Mexico')
            if row[x] == 'IDN':
                nations.append('Indonesia')
            if row[x] == 'NLD':
                nations.append('Netherlands')
            if row[x] == 'CHE':
                nations.append('Switzerland')
            if row[x] == 'SAU':
                nations.append('Saudi Arabia')
            if row[x] == 'TUR':
                nations.append('Turkey')

# Creating output dataset
df = pd.DataFrame({
    'Economy': nations,
    'value': value
})
print(df.head())

# Outputting dataset to csv file
os.chdir(os.path.dirname(__file__))
df.to_csv('dataset.csv')
