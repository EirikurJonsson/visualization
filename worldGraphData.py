import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
from dash_table import DataTable
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

data = pd.read_csv("owid-covid-data.csv")
locations = pd.read_csv("country.csv")
data["date"] = pd.to_datetime(data['date'])
data["lat"] = 0
data["long"] = 0

for country in range(len(data)):
    for location in range(len(locations)):
        if data.loc[country, "location"] == locations.loc[location, "country"]:
            data.loc[country, 'lat'] = locations.loc[location, "latitude"]
            data.loc[country,'long'] = locations.loc[location, 'longitude']

data["total_cases"] = data["total_cases"].round(2)
data["Total Cases"] = data["total_cases"].apply("{:,}".format)
data = data.fillna(0)
data['size'] = data['total_cases']
data['deathsize']=data['total_deaths']

data['HDI_INDEX'] = 1

conditions = [
    (data['human_development_index'] <= 0.65),
    (data['human_development_index'] > 0.65) & (data['human_development_index'] <= 0.80),
    (data['human_development_index'] > 0.80) & (data['human_development_index'] <= 0.90),
    (data['human_development_index'] > 0.90) & (data['human_development_index'] <= 1.0),
    ]

values = ['Poorly Developed', 'Moderate Developed', 'Very Developed', 'Higest Developed']

data['HDI_INDEX'] = np.select(conditions,values)

data.to_csv("graphWorld.csv")

print(data.tail())


