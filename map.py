import folium
import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
import branca 
import seaborn as sns
import numpy as np
import branca.colormap as cmp

ff = pd.read_csv('2015.csv')
# geojson = f'/Users/mlyg2772/Desktop/HackIllinois 2023/HackIllinoisProject/custom.geo.json' 
# world_data_dict = ff.set_index('Happiness Rank')['Economy (GDP per Capita)']

map = folium.Map(location=[40.116329, -88.243523],
           zoom_start=12,
           tiles='https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}',
           attr='My Data Attribution')

geojson_url = 'https://raw.githubusercontent.com/python-visualization/folium/main/examples/data/world-countries.json'
response = requests.get(geojson_url)
geojson = response.json()

# step = cmp.StepColormap(
#  ['yellow', 'green', 'purple'],
#  vmin=3, vmax=10,
#  index=[3, 6, 8, 10],  #for change in the colors, not used fr linear
#  caption='Color Scale for Map'    #Caption for Color scale or Legend
# )

# folium.GeoJson(
#     geojson,
#     style_function=lambda feature: {
#         'fillColor': step(world_data_dict[feature['id']]),
#         'color': 'black',       #border color for the color fills
#         'weight': 1,            #how thick the border has to be
#         'dashArray': '5, 3'  #dashed lines length,space between them
#     }
# ).add_to(map)

folium.Choropleth(
    geo_data = geojson,
    data = ff,
    columns = ['Happiness Rank', 'Economy (GDP per Capita)'],
    key_on = 'feature.id',
    fill_color ='YlGnBu',    
    fill_opacity = 0.7,
    line_opacity = 0.2
).add_to(map)

folium.LayerControl().add_to(map)

# url = (
#     "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data"
# )
# state_geo = f"{url}/us-states.json"
# state_unemployment = f"{url}/US_Unemployment_Oct2012.csv"
# state_data = pd.read_csv(state_unemployment)

# m = folium.Map(location=[48, -102], zoom_start=3)

# folium.Choropleth(
#     geo_data=state_geo,
#     name="choropleth",
#     data=state_data,
#     columns=["State", "Unemployment"],
#     key_on="feature.id",
#     fill_color="YlGn",
#     fill_opacity=0.7,
#     line_opacity=0.2,
#     legend_name="Unemployment Rate (%)",
# ).add_to(m)

# folium.LayerControl().add_to(m)

# m.save("map.html")

