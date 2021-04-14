#----------------------------------
# Import Modules
import pandas as pd
#----------------------------------
# Import datasets
df = pd.read_csv('geoEvents.csv')
df2 = pd.read_csv('usEvents.csv')
#----------------------------------
# Manipulate datasets
sets = [df,df2]
merged = pd.concat(sets)
#----------------------------------
# Export to new csv dataset
#----------------------------------
merged.to_csv('dataset.csv',index=False)
