import pandas as pd

descriptiveAttributes=[
        'location',
        'population',
        'gdp_per_capita',
        'life_expectancy',
        'median_age',
        'human_development_index'
        ]

df = pd.read_csv("owid-covid-data.csv")
for i in df.columns:
    print(i)
print(df.info())
'''
def indexFinder(input_data):
    df = pd.read_csv("owid-covid-data.csv")
    df = df.drop_duplicates(subset = 'location').reset_index(drop = True)
    df = df.loc[:,descriptiveAttributes].sort_values(by = ['human_development_index']).reset_index(drop=True)
    indx = df[df['location'] == input_data].index.tolist()
    ranger = [i+2 for i in indx]
    minRanger = [i - 1 for i in indx]
    slicer = range(minRanger[0], ranger[0])
    df = df.loc[slicer,:].round(3)
    df = df.reset_index(drop = True)
    return(df["location"].to_list())

print(indexFinder("China"))
'''
