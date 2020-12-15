import pandas as pd
import numpy as np
from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
import plotly.express as px
import plotly.graph_objs as go
import matplotlib.pyplot as plt



################ Getting the data ##################
df = pd.read_csv('owid-covid-data.csv')
df['datetime'] = pd.to_datetime(df['date'])

################# Replace NA's with 0 #################
# remove na
df = df.fillna(0)

################# Define colour by HDI #################

df['HDI_INDEX'] = 1

conditions = [
    (df['human_development_index'] <= 0.65),
    (df['human_development_index'] > 0.65) & (df['human_development_index'] <= 0.80),
    (df['human_development_index'] > 0.80) & (df['human_development_index'] <= 0.90),
    (df['human_development_index'] > 0.90) & (df['human_development_index'] <= 1.0),
    ]

values = ['Poorly Developed', 'Moderate Developed', 'Very Developed', 'Higest Developed']

df['HDI_INDEX'] = np.select(conditions,values)

df.to_csv("bubble.csv")





