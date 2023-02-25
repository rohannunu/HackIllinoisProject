# DO NOT RUN THIS FILE, IT IS USED FOR MAKING DATASETS

import pandas as pd

df = pd.read_csv("out.csv")
print(df.head())

target = pd.read_csv("population_by_country_2020.csv")


target = target[target['Country'].isin(df['Country'])]
print(target)

target = target[['Country', 'Population', 'Yearly Change', 'Net Change', 'Density', 'Land Area', 'Urban Pop %']]

df3 = pd.merge(df, target, on="Country")

print(df3)

#df3.to_csv("out.csv")