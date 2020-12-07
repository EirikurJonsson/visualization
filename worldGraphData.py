import pandas as pd

data = pd.read_csv("owid-covid-data.csv")
locations = pd.read_csv("country.csv")
data["date"] = pd.to_datetime(data['date'])
data = data.loc[:,["location", "total_cases_per_million"]]

data = data.groupby(["location"], as_index = False).sum()

data["lat"] = 0
data["long"] = 0

for country in range(len(data)):
    for location in range(len(locations)):
        if data.loc[country, "location"] == locations.loc[location, "country"]:
            data.loc[country, 'lat'] = locations.loc[location, "latitude"]
            data.loc[country,'long'] = locations.loc[location, 'longitude']

data["total_cases_per_million"] = data["total_cases_per_million"].round(2)
data.to_csv("graphWorld.csv")


