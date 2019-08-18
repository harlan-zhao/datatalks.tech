import pandas as pd
import os
from django.conf import settings
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool, LassoSelectTool, WheelZoomTool, PointDrawTool, ColumnDataSource
from bokeh.palettes import Category20c, Spectral6
from bokeh.transform import cumsum
from bokeh.resources import CDN



def analyze(file_id,file,ins1,ins2):
    path = '/home/harlanzhao/files/'+file_id+'/'+file
    df = pd.read_csv(path)
    if ins1 == ins2:
        pass
    else:
        df = pd.read_csv(path)
        xaxis,yaxis = df[ins1],df[ins2]
        p = figure(plot_width=1020,plot_height=710, title=f"{ins1}/{ins2}",
            toolbar_location="right", tools="pan,wheel_zoom,box_zoom,reset, hover, save,tap, crosshair")
        p.add_tools(LassoSelectTool())
        p.add_tools(WheelZoomTool())
        p.circle(xaxis, yaxis)
	script, div = components(p)
    script, div = components(p)
    return script, div



def get_columns(file_id,file):
    path = '/home/harlanzhao/files/'+file_id+'/'+file
    try:
        df = pd.read_csv(path)
        columns = list(df.columns.values)
    except:
        return False
    return columns or None

