"""
Handler.py : Concatenate individual datsets into one dataset
"""


# Import Modules
import pandas as pd

# Import datasets
df = pd.read_csv('geoEvents.csv')
df2 = pd.read_csv('usEvents.csv')
df3 = pd.read_csv('GND.csv')


# Manipulate datasets
sets = [df, df2, df3]
merged = pd.concat(sets)


# Export to new csv dataset
merged.to_csv('dataset.csv', index=False)
