# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 09:55:54 2020

@author: YANG_LAN
"""



"""
Dash Core Component example template
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
mcddata = pd.read_csv('mcd.csv')
available_name = mcddata['name'].unique()
app.layout = html.Div([
    html.H1('Nutrition Facts on Popular Items of World Famous Fast Food Giant and A Guide to Your Daily Intake Levels', style={'textAlign': 'center'}),
    html.Div([html.H5("Select your Item here: "),
             dcc.Dropdown(options=[{'label': 'Big-Mac', 'value': 'big-mac'},
                                    {'label': 'Quarter Pounder with Cheese', 'value': 'Quarter Pounder with Cheese'},
                                    {'label': 'Quarter Pounder with Cheese Deluxe', 'value': 'Quarter Pounder with Cheese Deluxe'},
                                    {'label': 'McDouble', 'value': 'McDouble'},
                                    {'label': 'Chocolate Shake', 'value': 'Chocolate Shake'},
                                    {'label': 'Vanilla Shake', 'value': 'Vanilla Shake'},
                                    {'label': 'Strawberry Shake', 'value': 'Strawberry Shake'},
                                    {'label': 'Vanilla Cone', 'value': 'Vanilla Cone'},
                                    {'label': 'Bacon, Egg  & Cheese Biscuit', 'value': 'Bacon, Egg  & Cheese Biscuit'},
                                    {'label': 'Egg McMuffin', 'value': 'Egg McMuffin'},
                                    {'label': 'Sausage McMuffin', 'value': 'Sausage McMuffin'},
                                    {'label': 'Sausage Biscuit  with Egg', 'value': 'Sausage Biscuit  with Egg'},
                                    ],
                          id='my-multidropdown',
                           multi=True,
                           value=['Big-Mac','Quarter Pounder with Cheese','Quarter Pounder with Cheese Deluxe','McDouble','Chocolate Shake','Vanilla Shake','Strawberry Shake','Vanilla Cone','Bacon, Egg  & Cheese Biscuit','Egg McMuffin','Sausage McMuffin','Sausage Biscuit  with Egg']),
             dcc.Graph(id='mcdygraph'),
                  ],
              style={'width': '49%', 'display': 'inline-block', 'float': 'right',}),
    
    dcc.Markdown("""
                 McDonald's has been many people's, including myself, favorite fast food restaurant. However, it has long been criticized for serving unhealthy food. 
                 Researches can be found on the Internet that nutritional values (such as sodium, fat, and sugar) of certain McDonald’s menu are way beyond the amounts we need per meal/day. Over the years, McDonald’s have been adding healthier items to their menus like salads and trying to make the existing items less greasy and salty. But for most people, going to McDonald’s is still for Big Mac or other signature meals and sandwiches. 
                 Therefore, this dashboard is created for all McDonald’s lover to see the nutritional values of their favorite menus. The dashboard contains some of the most popular items from McDonald’s breakfast, burger, and dessert menu. A user will be able to click on the item(s) they are interested in from the dropdown and see the calories of the items, which will display in a histogram below.  
                 Users can also select/de-select multiple items at a time to compare calories, or to calculate the total calories of different items. In the bottom of the dashboard, uses may also choose one of the three important nutritional values (total sugars, total fat, and protein) from the dropdown. Once the user chooses a value, a pie chart displaying the amounts of the value containing in all of the items we have. This way, users may compare nutritional values among various items and choose a healthier option from there.   
                 """),
    html.Div([
    dcc.Dropdown(
        id='values', 
        value='Total Fat', 
        options=[{'value': x, 'label': x} for x in ['Total Fat','Protein','Total Sugars']],
        clearable=False
    ),
    dcc.Graph(id="pie-chart")
])])
                 
@app.callback(
    dash.dependencies.Output('mcdygraph','figure'),
    [dash.dependencies.Input('my-multidropdown','value')]
    )
       
# Update the Histogram

def update_hist(name):
    mcddata = pd.read_csv('mcd.csv')
    mcddata = mcddata[mcddata.name.isin(name)]
    newfig = px.bar(mcddata,x="name",y="Calories")
    return newfig                	
server = app.server     

@app.callback(
    dash.dependencies.Output("pie-chart", "figure"), 
    [dash.dependencies.Input("values", "value")])
def generate_chart(values):
    mcddata = pd.read_csv('mcd.csv')
    fig = px.pie(mcddata, values=values, names='name')
    return fig             	
      
if __name__ == '__main__':
    app.run_server(debug=True)
    
