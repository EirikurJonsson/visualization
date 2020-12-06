import pandas as pd
import plotly.express as px

data = pd.read_csv("owid-covid-data.csv")
data = data.fillna(0)
data = data[data["location"] != "World"]
data = data[data["location"] != "International"]

fig = px.scatter_mapbox(
        lat = "lat",
        lon = "long",
        hover_data = ["human_development_index"],
        hover_name = "location",
        zoom = 1,
        height = 600,
        size = "total_cases_per_million",
        color = "continent"
        )
fig.update_layout(mapbox_style = 'carto-darkmatter')
fig.show()
