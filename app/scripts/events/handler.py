"""Handler.py : Concatenate individual datsets into one dataset"""

import pandas as pd

df = pd.read_csv('app/data/events/geoConflicts.csv')
df2 = pd.read_csv('app/data/events/usEvents.csv')
df3 = pd.read_csv('app/data/events/GND.csv')

pre_merge = [df, df2, df3]
merged = pd.concat(pre_merge)

filename = "app/data/events/dataset.csv"
merged.to_csv(filename, mode='w', index=False)
