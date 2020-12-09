import pandas as pd
import locale

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
data = data.rename(columns = {'continent':'Continent'})
data = data.fillna(0)
data.to_csv("graphWorld.csv")


