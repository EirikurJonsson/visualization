import pandas as pd

original = pd.read_csv("owid-covid-data.csv")
locations = pd.read_csv("country.csv")

original["lat"] = 0.0
original["long"] = 0.0

for country in range(len(original)):
    for location in range(len(locations)):
        if original.loc[country, "location"] == locations.loc[location, "country"]:
            original.loc[country, 'lat'] = locations.loc[location, 'latitude']
            original.loc[country, 'long'] = locations.loc[location, 'longitude']


original.to_csv("owid-covid-data.csv")
