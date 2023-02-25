# DO NOT RUN THIS FILE, IT IS USED FOR MAKING DATASETS

import pandas as pd

df = pd.read_csv("out.csv")
df['Urban Pop %'] = df['Urban Pop %'].str.rstrip('%').astype('float') / 100.0
df['Yearly Change'] = df['Yearly Change'].str.rstrip('%').astype('float') / 100.0

df = df[['Country','Ladder','Positive affect','Negative affect','Social support','Freedom','Corruption','Generosity','Log of GDP per capita','Healthy life expectancy','CO2 Emissions','Population','Yearly Change','Net Change','Density','Land Area','Urban Pop %']]

#df.to_csv('out.csv')