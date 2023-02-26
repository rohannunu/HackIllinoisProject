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
        colorbar_tickprefix = '$',
        colorbar_title = 'Probability',
    ))

    fig.update_layout(
        title_text='2014 Global GDP',
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ),
        annotations = [dict(
            x=0.55,
            y=0.1,
            xref='paper',
            yref='paper',
            text='Source: <a href="https://www.cia.gov/library/publications/the-world-factbook/fields/2195.html">\
                CIA World Factbook</a>',
            showarrow = False
        )]
    )

    fig.show()

