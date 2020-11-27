import pandas as pd
import plotly.express as px
data = pd.read_csv("owid-covid-data.csv")
names = data.columns

for name in names:
    print(name)
