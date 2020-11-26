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
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd

external_stylesheet = 'https://codepen.io/chriddyp/pen/bWLwgP.css'

data = pd.read_csv("owid-covid-data.csv")
data["date"] = pd.to_datetime(data["date"])
data = data.sort_values(by = "date")
data["total_cases_diff"] = data["total_cases"].diff()


app = dash.Dash(__name__, external_stylesheets = [external_stylesheet])
application = app.server
app.title = "Visualization Project"
app.layout = html.Div(
        children = [
            dcc.Dropdown(
                id = 'graph_filter',
                options = [
                    {
                        'label': i, 'value':i
                        } for i in data["location"].unique()
                    ]
                ),
            dcc.Graph(
                id = 'dailyChange'
                )
            ]
        )

@app.callback(
        Output('dailyChange', 'figure'),
        [Input('graph_filter', 'value')]
        )

def graphDiffperCountry(input_data):
    data = pd.read_csv("owid-covid-data.csv")
    data = data[data["location"] == input_data]
    data = data.sort_values(by = "date")
    data["total_cases_diff"] = data["total_cases"].diff()
    fig = px.line(data, x = 'date', y = 'total_cases_diff')
    return(fig)



if __name__ == '__main__':
    app.run_server(debug=True)
