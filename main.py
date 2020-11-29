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

# All modules imported shall be placed here
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
from dash_table import DataTable
import plotly.express as px
import pandas as pd

# Style sheet to use
external_stylesheet = 'https://codepen.io/chriddyp/pen/bWLwgP.css'

# Import data and data Transformation section
data = pd.read_csv("owid-covid-data.csv")
data["date"] = pd.to_datetime(data["date"]) #create datetime object
data = data.sort_values(by = "date") # sort by data
data["total_cases_diff"] = data["total_cases"].diff()

descriptiveAttributes=[
        'location',
        'population',
        'gdp_per_capita',
        'life_expectancy',
        'median_age',
        'human_development_index'
        ]

'''
This is the init. of the dash app. I (Eirikur) have never done this before but I propose a
guideline of sorts. 

After the start of every bracket please have a line between them like this

variable = [
    some stuff(
        some more stuff{

        }
    )
]
This has helped me in the past hold some resemblance of control of those
millions of brackets we have to use - and I hope it helps you as well
'''
app = dash.Dash(__name__, external_stylesheets = [external_stylesheet])
application = app.server
app.title = "Visualization Project"
app.layout = html.Div(
        children = [
            html.H1("Visualization Project",
                style ={'textAlign':'center'} ),
            html.Div(
                children = [
                    html.Div(
                        dcc.Dropdown(
                            id = 'graph_filter',
                            options = [
                                {
                                    'label': i, 'value':i
                                    } for i in data["location"].unique()
                                ]
                            )
                        ),
                    html.Div(
                        dcc.Graph(
                            id = 'dailyChange'
                            )
                        )

                    ],
                className = 'six columns'
                ),
            html.Div(
                children = [
                   DataTable(
                       id = 'descriptiveTable',
                       columns = [
                           {
                               'name':columnHeader, 'id':columnHeader
                               } for columnHeader in descriptiveAttributes
                           ],
                       style_cell = {
                           'font_size':'16px'
                           }
                       ) 
                    ],
                className = 'four columns'
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
    fig = px.line(
            data,
            x = 'date',
            y = 'total_cases_diff',
            labels = {
                'date':'Date',
                'total_cases_diff': 'Total New Cases per Day'
                },
            title = input_data)

    return(fig)

@app.callback(
        Output('descriptiveTable', 'data'),
        [Input('graph_filter', 'value')]
        )
def descriptiveTable(input_data):
    df = pd.read_csv("owid-covid-data.csv")

    descriptiveAttributes = [
            'location',
            'population',
            'gdp_per_capita',
            'life_expectancy',
            'median_age',
            'human_development_index'
            ]
    df = df[df["location"] == input_data]
    df = df.drop_duplicates(subset = 'location')
    df = df.loc[:,descriptiveAttributes].reset_index(drop=True)
    return(df.to_dict('records'))


if __name__ == '__main__':
    app.run_server(debug=True)
