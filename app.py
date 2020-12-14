# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 10:20:54 2020

@author: YANG_LAN
"""


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

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Nutritional Value on Popular Items of World Famous Fast Food Giant and A Guide to Your Daily Intake Levels', style={'textAlign': 'center'}),
    html.Div([html.H5(": "),
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
                 McDonald's has been many people's, including myself, favorite fast food restaurant. However, it has long been criticized for serving unhealthy food. Researches can be found on the Internet that nutritional values (such as sodium, fat, and sugar) of certain McDonald’s menu are way beyond the amounts we need per meal/day. Over the years, McDonald’s have been adding healthier items to their menus like salads and trying to make the existing items less greasy and salty. But for most people, going to McDonald’s is still for Big Mac or other signature meals and sandwiches. Therefore, this dashboard is created for all McDonald’s lover to see the nutritional values of their favorite menus. The dashboard contains some of the most popular items from McDonald’s breakfast, burger, and dessert menu. A user will be able to click on the item they are interested and see the calories of the items in a histogram below.  Users can also select multiple items at the same time to compare calories, or to calculate the total calories of the items. There is also a pie chart in the dashboard indicating the suggested daily intake level. 
                 '

                 """)
    ])

@app.callback(
    Output('mcdygraph','figure'),
    [Input('my-multidropdown','value')]
    )
       
# Update the Histogram

def update_hist(name):
    mcddata = pd.read_csv('mcd.csv')
    mcddata = mcddata[mcddata.name.isin(name)]
    newfig = px.bar(mcddata,x="name",y="Calories")
    return newfig                	
server = app.server           
if __name__ == '__main__':
    app.run_server(debug=True)
    
    
    import pyecharts.options as opts
from pyecharts.charts import Pie
biaozun_title = ['Total Fat', 'Carbohydrates', 'Protein', 'Saturated Fat',  'Trans Fat','Cholesterol']
biaozun_date = [93,350,140,21,3,0.3]


data_pair = [list(z) for z in zip(biaozun_title, biaozun_date)]
data_pair.sort(key=lambda x: x[1])

(
    Pie(init_opts=opts.InitOpts(width="1600px", height="800px", bg_color="#2c343c"))
    .add(
        series_name="index",
        data_pair=data_pair,
        # rosetype="radius",
        # radius="55%",
        center=["50%", "50%"],
        label_opts=opts.LabelOpts(is_show=False, position="center"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Daily Intake Levels",
            pos_left="center",
            pos_top="20",
            title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
        ),
        legend_opts=opts.LegendOpts(is_show=False),
    )
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c}grams ({d}%)"
        ),
        label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
    )
    .render("customized_pie.html")
)
