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
import plotly.graph_objects as go
import pandas as pd



'''
++++++++++++++++++++++ Style Section ++++++++++++++++++++++
'''

background = '#282a36'
line = '#44475a'
foreground = '#f8f8f2'
comment = '#6272a4'
cyan = '#8be9fd'
green = '#50fa7b'
orange = '#ffb86c'
pink = '#ff79c6'
purple = '#bd93f9'
red = '#ff5555'
yellow = '#f1fa8c'

'''
++++++++++++++++++++++ Initialization ++++++++++++++++++++++
'''

# Import data and data Transformation section
data = pd.read_csv("owid-covid-data.csv")
data["date"] = pd.to_datetime(data["date"]) #create datetime object
data = data.sort_values(by = "date") # sort by data
data["total_cases_diff"] = data["total_cases_per_million"].diff()

descriptiveAttributes=[
        'location',
        'population',
        'gdp_per_capita',
        'life_expectancy',
        'human_development_index'
        ]

dataTableColumns = ['Country', 'Population', 'GDP', 'Life Expectancy', 'HDI']

df = data.drop_duplicates(subset = 'location')
df = df.loc[:,descriptiveAttributes].reset_index(drop=True)
df = df.rename(
        columns = {
            'location': 'Country',
            'population':'Population',
            'gdp_per_capita':'GDP',
            'life_expectancy':'Life Expectancy',
            'human_development_index':'HDI'
            }
        )
df = df.round(2)
colorIndex = 4



############# MAP ####################

mapdata = pd.read_csv("graphWorld.csv")
mapdata = mapdata[mapdata['location'] != 'World']
mapdata = mapdata[mapdata['location'] != 'International']


fig = px.scatter_mapbox(mapdata,
                        lat = "lat",
                        lon = "long",
                        hover_name = "location",
                        hover_data = {
                            'total_cases':False,
                            'Total Cases':True,
                            'location':True,
                            'lat':False,
                            'long':False,
                            'deathsize':True
                            },
                        zoom = 1,
                        size_max=75,
                        height = 800,
                        opacity = 0.7,
                        size = 'deathsize',
                        color = "HDI_INDEX",
                        color_discrete_sequence=px.colors.cyclical.HSV,
                        animation_frame="date",
                        animation_group="location"
                       )


fig.update_layout(mapbox_style = 'carto-positron',
                  paper_bgcolor = background,
                  font_color = cyan
        )
fig.update_layout(
    hoverlabel=dict(
        bgcolor=background,
        font_color = cyan,
        font_size=16,
        font_family="Rockwell"
    )
 )
fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 100
fig.layout.updatemenus[0].buttons[0].args[1]["transition"]["duration"] = 100

############## BUBBLE CHART ##################

bubbledata = pd.read_csv("bubble.csv")
bubbledata = bubbledata[bubbledata['location'] != 'World']
bubbledata = bubbledata[bubbledata['location'] != 'International']

bubblefig = px.scatter(
                 bubbledata, 
                 x="total_cases_per_million",
                 y="total_deaths_per_million",
                 animation_frame="date",
                 animation_group="location",
                 size="gdp_per_capita",
                 color="HDI_INDEX",
                 color_discrete_sequence=px.colors.cyclical.HSV,
                 hover_name="location",
                 size_max=20,
                 height = 800
                )
bubblefig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 100
bubblefig.layout.updatemenus[0].buttons[0].args[1]["transition"]["duration"] = 100
bubblefig.update_layout(
    paper_bgcolor = background,
    plot_bgcolor = background,
    font_color = cyan,
)
bubblefig.update_yaxes(range=[-10,1500])
bubblefig.update_xaxes(range=[-10,80000])


'''
This next function helps identify the comparison countries around the selected
country. 
'''

def indexFinder(input_data):
    '''
    This function takes as input:
    1. Country name 
    2. Gives as output
        - Country with lower HDI than selected country
        - Selected Country
        - Country with higher HDI than selected country
    '''
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


'''
++++++++++++++++++++++ Initialization of the App ++++++++++++++++++++++
'''

app = dash.Dash(__name__)
application = app.server
app.title = "Visualization Project"
app.layout = html.Div(
        children = [
            html.H1(
                "Visualization Project",
                style ={
                    'textAlign':'center',
                    'color':cyan
                }
            ),
        html.Div(
                children = [
                    html.Div(
                        children = [
                            html.H2(
                                "World Map: Total death rate. Color by Humen Development Index",
                                style = {
                                    'textAlign':'center',
                                    'color':cyan
                                    }
                                ),
                            dcc.Graph(
                                id = 'worldGraph',
                                figure = fig
                                )
                            ]
                        )
                    ]
                ),
html.Div(
        children = [
            html.Div(
                children = [
                    html.Div(
                        dcc.Dropdown(
                            id = 'graph_filter',
                            options = [
                                {
                                    'label': i, 'value':i
                                    } for i in data["location"].unique()
                                ],
                            value = 'Denmark'
                            )
                        ),
                    html.Div(
                        dcc.Graph(
                            id = 'dailyChange'
                            )
                        )

                    ],
                className = 'seven columns'
                ),
            html.Div(
                children = [
                    html.H4(
                        "Descriptive Table with Benchmark Countries",
                        style = {
                            'color':cyan,
                            'textAlign':'center'
                        }
                    ),
                   DataTable(
                       id = 'descriptiveTable',
                       columns = [
                           {
                               'name':columnHeader, 'id':columnHeader
                               } for columnHeader in dataTableColumns
                           ],
                       style_cell = {
                           'font_size':'20px',
                           'backgroundColor':background,
                           'color':comment,
                           'textAlign':'left'
                           },
                       style_as_list_view = True,
                       style_header = {
                           'fontWeight':'bold',
                           'text_transform':'capitalize',
                           'backgroundColor':line
                           },
                       style_data_conditional = [
                           {
                           'if':{
                               'row_index':4
                               },
                           'backgroundColor':green,
                           'color':comment
                           },
                           {
                               'if':{
                                   'row_index':5
                                   },
                           'backgroundColor':yellow,
                           'color':comment

                               },
                           {
                               'if':{
                                   'row_index':3
                                   },
                           'backgroundColor':yellow,
                           'color':comment

                               },
                           {
                               'if':{
                                   'column_id':'Life Expectancy'
                                   },
                               'textAlign':'center'
                               },
                           {
                               'if':{
                                   'column_id':'HDI'
                                   },
                               'textAlign':'right'
                               },
                           {
                               'if':{
                                   'column_id':'GDP'
                                   },
                               'textAlign':'center'
                               }
                           ]
                       ) 
                    ],
                className = 'four columns'
                )

            ],
            className = 'row'
        ),
        ## Insert bubblechart
                html.Div(
                children = [
                    html.Div(
                        children = [
                            html.H2(
                                "Bubble Chart",
                                style = {
                                    'textAlign':'center',
                                    'color':cyan
                                    }
                                ),
                            dcc.Graph(
                                id = 'bubbleChart',
                                figure = bubblefig
                                )
                            ]
                        )
                    ]
                ),

    ]
)
@app.callback(
        Output('dailyChange', 'figure'),
        [Input('graph_filter', 'value')]
        )

def graphDiffperCountry(input_data):
    global data
    data = data.sort_values(by = "date")
    countries = indexFinder(input_data)
    country1 = data[data["location"] == countries[0]].reset_index(drop = True)
    country2 = data[data["location"] == countries[1]].reset_index(drop = True)
    country3 = data[data["location"] == countries[2]].reset_index(drop = True)
    country1["total_cases_diff"] = country1["total_cases_per_million"].diff()
    country2["total_cases_diff"] = country2["total_cases_per_million"].diff()
    country3["total_cases_diff"] = country3["total_cases_per_million"].diff()

    country1y = country1["total_cases_diff"].to_list()
    country2y = country2["total_cases_diff"].to_list()
    country3y = country3["total_cases_diff"].to_list()
    country1x = country1["date"].to_list()
    country2x = country2["date"].to_list()
    country3x = country3["date"].to_list()

    fig = go.Figure()
    fig.add_trace(
            go.Scatter(
                x = country1x,
                y = country1y,
                mode = 'lines',
                name = countries[0]
                )
            )
    fig.add_trace(
            go.Scatter(
                x = country2x,
                y = country2y,
                mode = 'lines',
                name = countries[1]
                )
            )
    fig.add_trace(
            go.Scatter(
                x = country3x,
                y = country3y,
                mode = 'lines',
                name = countries[2]
                )
            )
    fig.update_layout(
            plot_bgcolor = background,
            paper_bgcolor = background,
            font_color = cyan,
            legend_title_font_color = cyan,
            xaxis = {
                'showgrid':False
                },
            title = 'Daily Changes in New Cases per Million',
            hovermode = 'x unified'
            )

    return(fig)

@app.callback(
        Output('descriptiveTable', 'data'),
        [Input('graph_filter', 'value')]
        )
def descriptiveTable(input_data):
    df = data
    descriptiveAttributes = [
            'location',
            'population',
            'gdp_per_capita',
            'life_expectancy',
            'human_development_index'
            ]
    indx = input_data
    df = df.drop_duplicates(subset = 'location').reset_index(drop = True)
    df = df.loc[:,descriptiveAttributes].sort_values(by = ['human_development_index']).reset_index(drop=True)
    indx = df[df['location'] == indx].index.tolist()
    ranger = [i+5 for i in indx]
    minRanger = [i - 4 for i in indx]
    slicer = range(minRanger[0], ranger[0])
    df = df.loc[slicer,:].round(3)
    df = df.reset_index(drop = True)
    df = df.rename(
            columns = {
                'location': 'Country',
                'population':'Population',
                'gdp_per_capita':'GDP',
                'life_expectancy':'Life Expectancy',
                'human_development_index':'HDI'
                }
            )
    df = df.round(2)
    return(df.to_dict('records'))


if __name__ == '__main__':
    app.run_server(debug=True)
else:
    print("Something is wrong")
