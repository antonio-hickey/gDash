import pandas as pd

df = pd.read_csv('app/data/covid/world_c19.csv')

date = df['date']
deaths = df['total_deaths']

up_sigma = deaths.rolling(7).std().rolling(28).mean() * 4
down_sigma = deaths.rolling(7).std().rolling(28).mean() * 2
deaths = deaths.diff(periods=7)

new_df = pd.DataFrame({
    'date': date,
    'deaths weekly change': deaths,
    '+2 Sigma': up_sigma,
    '-2 Sigma': down_sigma,
})

filename = "app/data/covid/dataset.csv"
new_df.to_csv(
    filename,
    mode='w',
    index=False,
)
