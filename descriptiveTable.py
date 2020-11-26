'''
This is intended to create a data table of other variables
that are static in our data-set

- Diabetes prevalence
- GDP-Per-Capita
- Median Age
- Life Expectancy
- Human development Index
'''

import plotly.express as px
import pandas as pd

external_stylesheet = 'https://codepen.io/chriddyp/pen/bWLwgP.css'

data = pd.read_csv("owid-covid-data.csv")
data["date"] = pd.to_datetime(data["date"])
data = data.sort_values(by = "date")

attributes = [
        "location",
        "population",
        "gdp_per_capita",
        "life_expectancy",
        "median_age",
        "human_development_index"
        ]

iceland = data[data["location"] == "Iceland"]

dummyData = pd.DataFrame()
countries = data["location"].unique()
result = []

df = data.drop_duplicates(subset = 'location')
df = df.loc[:,attributes].reset_index(drop = True)
print(df)
