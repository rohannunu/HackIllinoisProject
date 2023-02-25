from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn import preprocessing

df = pd.read_csv("out.csv")
X = df[["Ladder", "Positive affect","Social support", "Freedom", "Corruption", "Generosity", "Log of GDP per capita", "Healthy life expectancy", "CO2 Emissions"]]
y  = df['Country']

scaler = preprocessing.StandardScaler().fit(X)

X_scaled = scaler.transform(X)

clf = RandomForestClassifier(max_depth = 6)
clf.fit(X_scaled, y)
input = [[9,18.0,20.0,9.0,11.0,14.0,19.0,8.0,0.069134]]
inp_scaled = scaler.transform(input)

print(clf.predict(inp_scaled))
print(clf.predict_proba(inp_scaled))
