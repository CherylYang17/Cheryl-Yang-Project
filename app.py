# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 10:20:54 2020

@author: YANG_LAN
"""

#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Dash Core Component example template
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(_name_, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Mcdonald Burger Nutrition', style={'textAlign': 'center'}),
    html.Div([html.H5("Dropdown: "),
             dcc.Dropdown(options=[{'label': 'big-mac', 'value': 'big-mac'},
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
                           value=['big-mac','Quarter Pounder with Cheese','Quarter Pounder with Cheese Deluxe','McDouble','Chocolate Shake','Vanilla Shake','Strawberry Shake','Vanilla Cone','Bacon, Egg  & Cheese Biscuit','Egg McMuffin','Sausage McMuffin','Sausage Biscuit  with Egg']),
             dcc.Graph(id='mcdygraph'),
                  ],
              style={'width': '49%', 'display': 'inline-block', 'float': 'right',}),
    
    dcc.Markdown("""
                 Add some Junkfood Quotes Here
                 """)
    ])

@app.callback(
    Output('mcdygraph','figure'),
    [Input('my-multidropdown','value')]
    )
       
# Update the histogram

def update_hist(name):
    mcddata = pd.read_csv('mcd.csv')
    mcddata = mcddata[mcddata.name.isin(name)]
    newfig = px.bar(mcddata,x="name",y="Calories")
    return newfig                	
                 
if _name_ == '_main_':
    app.run_server(debug=True)