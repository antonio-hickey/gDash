# Using the World Bank API for sourcing global economic data
import pandas as pd
import wbgapi as wb

from app.util import Nations

nations = []
value = []

regions = ['USA', 'CHN', 'JPN', 'DEU', 'GBR', 'IND',
           'FRA', 'ITA', 'CAN', 'KOR', 'RUS', 'AUS', 'BRA',
           'ESP', 'MEX', 'IDN', 'NLD', 'CHE', 'SAU', 'TUR']

for row in wb.data.fetch('NY.GDP.MKTP.CD', economy=regions, mrv=1):
    value.append(row['value'])
    nations.append(
        Nations.convert_abbreviation(row['economy']),
    )

df = pd.DataFrame({
    'Economy': nations,
    'value': value,
})
df.to_csv('app/data/economic/gdp.csv')
