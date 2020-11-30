import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
data = pd.read_csv("owid-covid-data.csv")

data["date"] = pd.to_datetime(data["date"])
iceland = data[data["location"] == "Iceland"]
iceland = iceland.sort_values(by = ["date"])
iceland["totalDiff"] = iceland["total_cases"].diff()

plt.plot(iceland["date"], iceland["total_deaths"].diff())
plt.show()
