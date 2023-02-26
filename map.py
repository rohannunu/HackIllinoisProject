import folium
import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
import branca 
import seaborn as sns
import numpy as np

ff = pd.read_csv('2015.csv')
# geojson = f'/Users/mlyg2772/Desktop/HackIllinois 2023/HackIllinoisProject/custom.geo.json' 


map = folium.Map(location=[40.116329, -88.243523],
           zoom_start=12,
           tiles='https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}',
           attr='My Data Attribution')

geojson_url = 'https://raw.githubusercontent.com/python-visualization/folium/main/examples/data/world-countries.json'
response = requests.get(geojson_url)
geojson = response.json()

folium.Choropleth(
    geo_data = geojson,
    data = ff,
    columns = ['Happiness Rank', 'Happiness Score'],
    key_on = 'feature.id'
).add_to(map)

map.save("map.html")

