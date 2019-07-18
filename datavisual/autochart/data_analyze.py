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
	path = os.path.join(settings.BASE_DIR, f"files\\{file_id}\\{file}")
	xaxis,yaxis = [],[]
	df = pd.read_csv(path)

	Xaxis = ['Welcome', 'To', 'World', 'Of', 'Data', 'Science']
	Yaxis = [25, 30, 8, 22, 12, 17]

	p = figure(x_range=Xaxis, plot_width=1020,plot_height=710, title=f"{ins1}/{ins2}",
	       toolbar_location="right", tools="pan,wheel_zoom,box_zoom,reset, hover, save,tap, crosshair")
	source = ColumnDataSource(data=dict(Xaxis=Xaxis, Yaxis=Yaxis, color=Spectral6))
	p.add_tools(LassoSelectTool())
	p.add_tools(WheelZoomTool())       

	p.vbar(x='Xaxis', top='Yaxis', width=.8, color='color', legend="Xaxis", source=source)
	p.legend.orientation = "horizontal"
	p.legend.location = "top_center"

	script, div = components(p)
	return script, div
	


def get_columns(id,file):
	path = os.path.join(settings.BASE_DIR, f"files\\{id}\\{file}")
	df = pd.read_csv(path)
	columns = list(df.columns.values)
	return columns or None

