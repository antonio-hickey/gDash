"""
Handler.py : Concatenate individual datsets into one dataset
"""

import os
import pathlib

import pandas as pd

df = pd.read_csv('../../data/events/geoConflicts.csv')
df2 = pd.read_csv('../../data/events/usEvents.csv')
df3 = pd.read_csv('../../data/events/GND.csv')

sets = [df, df2, df3]
merged = pd.concat(sets)

APP_PATH = str(pathlib.Path(__file__).parent.resolve())
filename = (os.path.join(APP_PATH, "../../data/events/dataset.csv"))
merged.to_csv(filename, index=False)
