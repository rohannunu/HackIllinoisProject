from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn import preprocessing


df = pd.read_csv("out.csv")
X = df[["Ladder", "Positive affect","Social support", "Freedom", "Corruption", "Generosity", "Log of GDP per capita", "Healthy life expectancy", "CO2 Emissions", "Population", "Yearly Change", "Density", "Land Area", "Urban Pop %"]]
y  = df['Country']

scaler = preprocessing.RobustScaler().fit(X)
X_scaled = scaler.transform(X)

clf = RandomForestClassifier(max_depth = 4)
clf.fit(X_scaled, y)

input = [[9,18.0,20.0,9.0,11.0,14.0,19.0,8.0,0.069134,5542237,0.0015,18,303890,0.86]]
inp_scaled = scaler.transform(input)
#print(clf.predict(inp_scaled))
#print(clf.predict_proba(inp_scaled))

#Testing
X_s = df[['Density']]
scaler2 = preprocessing.RobustScaler().fit(X_s)
X_scaled2 = scaler2.transform(X_s)
print(X_scaled2)

# Need to move this somewhere else, but will keep this for now
def main():
    input = [[9,18.0,20.0,9.0,11.0,14.0,19.0,8.0,0.069134,5542237,0.0015,18,303890,0.86]]
    inp_scaled = scaler.transform(input)
    print(clf.predict(inp_scaled))
    print(clf.predict_proba(inp_scaled))

def pred_country(model_input):
    #"Ladder", "Positive affect","Social support", "Freedom", "Corruption", "Generosity", "Log of GDP per capita", "Healthy life expectancy", "CO2 Emissions", "Population", "Yearly Change", "Density", "Land Area", "Urban Pop %"
    model_input = pd.Series(model_input)
    model_input = model_input/100
    #inp_scaled = scaler.transform([model_input])
    res = clf.predict([model_input])
    print(X_scaled)
    print(model_input)
    print(res)
    return res[0]


if __name__ == "__main__":
    main()






