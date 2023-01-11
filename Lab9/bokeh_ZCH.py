import numpy as np
import pandas as pd
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from bokeh.io import curdoc
from bokeh.plotting import figure, show
from bokeh.models import Slider, Div, ColumnDataSource
from bokeh.layouts import row, column, gridplot

N = 10000
S_0 = 9999
I_0 = N - S_0
R_0 = 0
y_0 = S_0,I_0,R_0
b = 0.50
gamma = 0.50
t = np.linspace(0,100,1000)

def SIR(y,t,N,b,g):
    S,I,R = y
    dS = -b*S*I/N
    dI = b*I*S/N-g*I
    dR = g*I
    return dS,dI,dR

res = odeint(SIR, y_0, t, (N,b,gamma))
disp = pd.DataFrame({"t" : t, "S" : list(res[:,0]), "I" : list(res[:,1]), "R" : list(res[:,2])})
source = ColumnDataSource(disp)

fig = figure(x_axis_label = "t", y_axis_label = "N", width = 1000, aspect_ratio = 2)
fig.line("t","S", color = "blue", line_width = 2, source=source, legend_label="S")
fig.line("t","I", color = "red", line_width = 2, source=source, legend_label="I")
fig.line("t","R", color = "green", line_width = 2, source=source, legend_label="R")
fig.title.text = "SIR model"
fig.title.align = "center"
fig.toolbar.autohide = True
fig.border_fill_color = "thistle"
fig.background_fill_color = "ghostwhite"

def update_b(attr,old,new): #to update beta using slider
    global b
    b = new
    res = odeint(SIR, y_0, t, (N,b,gamma))
    disp = pd.DataFrame({"t" : t, "S" : list(res[:,0]), "I" : list(res[:,1]), "R" : list(res[:,2])})
    source.data = ColumnDataSource.from_df(disp)

def update_g(attr,old,new): #to update gamma using slider
    global gamma
    gamma = new
    res = odeint(SIR, y_0, t, (N,b,gamma))
    disp = pd.DataFrame({"t" : t, "S" : list(res[:,0]), "I" : list(res[:,1]), "R" : list(res[:,2])})
    source.data = ColumnDataSource.from_df(disp)

s1 = Slider(start = 0, end = 1, step = 0.02, value = gamma, title = "Gamma", bar_color = 'darkseagreen', background = 'whitesmoke')
s2 = Slider(start = 0, end = 1, step = 0.02, value = b, title = "Beta", bar_color = 'lightsteelblue',  background = 'whitesmoke')
s1.on_change("value",update_g)
s2.on_change("value",update_b)

div = Div(text=r"""
SIR model:
<p \><p \>
$$\frac{dS}{dt} = - \frac{\beta SI}{N}$$
<p \><p \>
$$\frac{dI}{dt} = \frac{\beta SI}{N} - \gamma I$$
<p \><p \>
$$\frac{dR}{dt} = \gamma I$$
<p \><p \>
Start: $$S(0) + I(0) + R(0) = N = const$$
<p \><p \>
S = susceptible, I - infected, R - recovered
""")

curdoc().add_root(row(fig, column(s1,s2, div)))