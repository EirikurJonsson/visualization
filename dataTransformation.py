#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

data = pd.read_csv(url)

df = data.transpose()

df.columns = df.iloc[1]
df = df.reset_index()
df = df.drop([0,1,2,3])
df = df.reset_index(drop = True)

df["date"] = pd.to_datetime(df["index"])
print(df.head())
fig = px.scatter(df, x = "date", y = "Iceland")
fig.show()
