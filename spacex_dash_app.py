# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('My SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
# TASK 1: Add a dropdown list to enable Launch Site selection
# The default select value is for ALL sites
# dcc.Dropdown(id='site-dropdown',...)
html.Br(),
dcc.Dropdown(id='site_dropdown',
            options=[{'label': 'All Sites', 'value': 'ALL'},
                    {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                    {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                    {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'}],
            value='ALL', placeholder ='Do select a site', searchable = True),
html.Br(),
# TASK 2: Add a pie chart to show the total successful launches count for all sites
# If a specific launch site was selected, show the Success vs. Failed counts for the site
html.Div(dcc.Graph(id='success-pie-chart')),
html.Br(),
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(site_dropdown):
    filtered_df = spacex_df[spacex_df['Launch Site'] == 'site_dropdown']
    if site_dropdown == 'ALL':
        fig = px.pie(data, values='class', names='Launch Site', title='Successful Lanch')
    return fig
    else:
        filtered_df = spacex_df[spacex_df['Launch Site']=='site_dropdown']
        fig = px.pie(filtered_df, values = 'Class count' names = 'Class',
        title = 'Successful launches by site.')
    return figure
html.P("Payload range (Kg):"),

# TASK 3: Add a slider to select payload range
#dcc.RangeSlider(id='payload-slider',...)
dcc.RangeSlider(id='payload-slider',
                min=0, max=10000, step=1000,
                marks={0: '0', 100: '100'},
                value=[min_payload, max_payload])

# TASK 4: Add a scatter chart to show the correlation between payload and launch success
html.Div(dcc.Graph(id='success-payload-scatter-chart')),
        ])

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'),
	       Input(component_id='payload-slider', component_prpoerty='value')])

def build_scatteer(site_dropdown, slider_range):
low, high = slider_range
mask = (space_df['Payload Mass'] > low) & (spacex_df['Payload Mass'] < high)
    filtered_df = spacex_df[mask]
    if site_dropdown == 'ALL':
        fig = px.scatter(space_df, x='Payload Mass', y='class', color='Booster Version Category', 
	title='Payload')
    return fig
    else:
        filtered_df1 = filtered_df['Launch Site']==['site_dropdown']
        fig = px.scatter(filtered_df1, x = 'Payload Mass' y = 'Class', color = 'Booster Version Category',
        title = 'Payload')
    return figure
# Run the app
if __name__ == '__main__':
    app.run_server()
