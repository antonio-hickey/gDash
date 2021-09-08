"""
Handler.py : Concatenate individual datsets into one dataset
"""

import os
import pathlib

import pandas as pd

df = pd.read_csv('app/data/events/geoConflicts.csv')
df2 = pd.read_csv('app/data/events/usEvents.csv')
df3 = pd.read_csv('app/data/events/GND.csv')

merged = pd.concat([
    df,
    df2.values,
    df3.values,
])

APP_PATH = str(pathlib.Path(__file__).parent.resolve())
filename = (os.path.join(APP_PATH, "../../data/events/dataset.csv"))
merged.to_csv(filename, mode='w', index=False)
