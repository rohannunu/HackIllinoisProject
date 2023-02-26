# DO NOT RUN THIS FILE, IT IS USED FOR MAKING DATASETS

import pandas as pd

df = pd.read_csv("out.csv")
print(df.head())
df2 = pd.read_csv("test.csv")
print(df2.head())

df2['Country'] = df2['COUNTRY']

df2 = df2[df2['Country'].isin(df['Country'])]

df2 = df2[['Country', 'CODE']]

df3 = pd.merge(df, df2, on="Country")

print(df3)
#df3.to_csv("out.csv")