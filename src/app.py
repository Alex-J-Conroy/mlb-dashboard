import sys
import pandas as pd
import re
import numpy as np
import scipy.io
import pandas as pd

import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

### App layout

app.layout = html.Div([
    style={'backgroundColor': colors['background']},
    html.H1("MLB Team Management Dashboard", style={'text-align': 'center'}),
    html.Div("Controls", style={'text-align': 'centre'}),
    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "2015", "value": 2015},
                     {"label": "2016", "value": 2016},
                     {"label": "2017", "value": 2017},
                     {"label": "2018", "value": 2018}],
                 multi=False,
                 value=2015,
                 style={'width': "40%"}
                 ),
    html.H1("Player", style={'text-align': 'center',
                             'background-color': 'grey',
                             'display':'inline-block', 
                             'width': '50%'}),
    html.H1("Team", style={'text-align': 'center', 
                           'display':'inline-block',
                           'background-color': 'grey',
                           'width': '50%'}),
    
    
    html.Div(id='output_container', children=[]),
    html.Br(),
    
    #dcc.Graph(id='map', figure={}) for output: Output(component_id='map', component_property='figure')

######### TAB stuff ##############
#     app.layout = html.Div([
#     dcc.Tabs(id="tabs", value='tab-1', children=[
#         dcc.Tab(label='Batting', value='tab-1'),
#         dcc.Tab(label='Pitching', value='tab-2'),
#     ]),
#     html.Div(id='tabs-content')
    
# @app.callback(Output('tabs-content', 'children'),
#               [Input('tabs', 'value')])
# def render_content(tab):
#     if tab == 'tab-1':
#         return html.Div([
#             html.H3('Tab content 1')
#         ])
#     elif tab == 'tab-2':
#         return html.Div([
#             html.H3('Tab content 2')
#         ])

])


# # Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children')],
    [Input(component_id='slct_year', component_property='value')]
)

def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The Year chosen by user was: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["Year"] == option_slctd]
    #dff = dff[dff["Affected by"] == "Varroa_mites"]

     # Plotly Express
    fig = px.choropleth(
        data_frame=dff,
        locationmode='USA-states',
        locations='state_code',
        scope="usa",
        color='Pct of Colonies Impacted',
        hover_data=['State', 'Pct of Colonies Impacted'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
        template='plotly_dark'
    )

#     # Plotly Graph Objects (GO)
#     fig = go.Figure(
#         data=[go.Choropleth(
#             locationmode='USA-states',
#             locations=dff['state_code'],
#             z=dff["Pct of Colonies Impacted"].astype(float),
#             colorscale='Reds',
#         )]
#     )
    
#     fig.update_layout(
#         title_text="Bees Affected by Mites in the USA",
#         title_xanchor="center",
#         title_font=dict(size=24),
#         title_x=0.5,
#         geo=dict(scope='usa'),
#     )
#    return container,fig

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)


colors = {
    'background': '##72DDFA',
    'text': '#FFFFFF'
}
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")



app.layout = html.Div(style={'backgroundColor': colors['background']},children=[
    html.H1("MLB Team Management Dashboard", style={'text-align': 'center'}),
    html.Div("Controls", style={'text-align': 'centre'}),
    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "2015", "value": 2015},
                     {"label": "2016", "value": 2016},
                     {"label": "2017", "value": 2017},
                     {"label": "2018", "value": 2018}],
                 multi=False,
                 value=2015,
                 style={'width': "40%"}
                 ),
    html.H1("Player", style={'text-align': 'center',
                             'background-color': 'grey',
                             'display':'inline-block', 
                             'width': '50%',
                            'height': '50%'}),
    html.H1("Team", style={'text-align': 'center', 
                           'display':'inline-block',
                           'background-color': 'grey',
                           'width': '50%'}),
    
    
    html.Div(id='output_container', children=[]),
    html.Br(),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=False)