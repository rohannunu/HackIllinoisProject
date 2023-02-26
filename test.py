import plotly.graph_objects as go
import base64
import pandas as pd
import io

def config(df): 
    fig = go.Figure(data=go.Choropleth(
        locations = df['code'],
        z = df['Prob'],
        text = df['Country'],
        colorscale = 'tropic',
        autocolorscale=False,
        reversescale=True,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_tickprefix = '%',
        colorbar_title = 'Probability'
    ))

    fig.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        )
    )
    print("reached")
    

    #fig_json = fig.to_json()

    # convert graph to PNG and encode it
    img_bytes = fig.to_image(format="png")
    encoding = base64.b64encode(img_bytes).decode()
    img_b64 = "data:image/png;base64," + encoding
    return img_b64
