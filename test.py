import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("owid-covid-data.csv")
df = df[df["location"]=='Germany']
df["date"] = pd.to_datetime(df["date"])
y= df["total_deaths_per_million"].diff().to_list()
x = df["date"].to_list()

plt.plot(x,y)
plt.show()
