'''

VISUALIZATION Project

This is our main python file that contains the app we are working on.

There is a simple structure to this app:

    1. Firstly there is the layout section - this is were all the elements in the app
       are located in a html.Div which is the divided into dbc.Row and n-number of 
       dbc.Col
    2. This is the callback section - here we give the data and create the viz that 
       go into the div's we create.
'''

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

data = pd.read_csv("owid-covid-data.csv")

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.SLATE])
application = app.server
app.title = "Visualization Project"
app.layout = html.Div([
    dbc.Row([
        dbc.Col(
            html.Div(
                children = [
                    html.H1("THIS WORKS "),
                    html.H2("THIS AS WELL"),
                    html.H4("THIS HERE TO")
                    ] 

                )
            )
        ])
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
