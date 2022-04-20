#!/usr/bin/env python
# -*- coding: latin-1 -*-
import os
my_TeX=open("miprimer.tex","w+")
my_TeX.write("hola\n\\bye")
my_TeX.close()


import plotly.express as px

fig = px.line(x=[1, 2, 3, 4], y=[1, 4, 9, 16], title=r'$\alpha_{1c} = 352 \pm 11 \text{ km s}^{-1}$')
fig.update_layout(
    xaxis_title=r'$\sqrt{(n_\text{c}(t|{T_\text{early}}))}$',
    yaxis_title=r'$d, r \text{ (solar radius)}$'
)
fig.show()


import plotly.graph_objs as go

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4],
    y=[1, 4, 9, 16],
    name=r'$\alpha_{1c} = 352 \pm 11 \text{ km s}^{-1}$'
))
fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4],
    y=[0.5, 2, 4.5, 8],
    name=r'$\beta_{1c} = 25 \pm 11 \text{ km s}^{-1}$'
))
fig.update_layout(
    xaxis_title=r'$\sqrt{(n_\text{c}(t|{T_\text{early}}))}$',
    yaxis_title=r'$d, r \text{ (solar radius)}$'
)
fig.show()

import plotly.graph_objects as go # or plotly.express as px
fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
