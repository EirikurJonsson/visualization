#!/usr/bin/env python3

import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
data = pd.read_csv("owid-covid-data.csv")
data["dates"] = pd.to_datetime(data["date"])
data = data.sort_values(by = ["dates"])
names = data.columns
location = data["location"].unique()
for name in names:
    print(name)

names = names[4:]
for name in names:
    for country in location:
        if name == "total_cases":
            df = data[data["location"] == country]
            df["total_cases"] = df["total_cases"].diff()
            plt.plot(df["dates"], df[name])
            plt.title(name +" "+ country)
            plt.show()
        else:
            df = data[data["location"] == country]
            plt.plot(df["dates"], df[name])
            plt.show()
