import plotly.graph_objects as go
import pandas as pd

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
        colorbar_title = 'Probability',
    ))

    fig.update_layout(
        title_text='Probability That a Country Matches You',
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ),
        annotations = [dict(
            x=0.55,
            y=0.1,
            showarrow = False
        )]
    )
    print("reached")
    fig.write_image("static/fig.png")
    print("Fig")