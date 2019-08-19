from django.shortcuts import render
from rest_framework import viewsets,status,views
from django.contrib.auth.models import User
from .serializers import UserSerializer,VisualSerializer
from bokeh.plotting import figure
from rest_framework.response import Response
from bokeh.embed import components
from bokeh.models import HoverTool, LassoSelectTool, WheelZoomTool, PointDrawTool, ColumnDataSource
from bokeh.palettes import Category20c, Spectral6
from bokeh.transform import cumsum
from bokeh.resources import CDN
import pandas as pd

# Create your views here.

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def api_visual(col1_title,col2_title,col1,col2):
    col1,col2=eval(col1),eval(col2)
    temp = { col1_title : col1, col2_title : col2}
    df = pd.DataFrame(temp)
    xaxis = df[col1_title]
    yaxis = df[col2_title]
    # return xaxis,yaxis
    if col1 == []:
        p = figure(plot_width=1020,plot_height=710, title=f"{col1_title}/{col2_title}",x_axis_label = f'{col1_title}',
            y_axis_label = f'{col2_title}',toolbar_location="right", tools="pan,wheel_zoom,box_zoom,reset, hover, save,tap, crosshair")
        p.vbar(x=[i+1 for i in range(len(xaxis))], width=0.5, bottom=0,
        top=xaxis, color="firebrick")

    else:

        p = figure(plot_width=1020,plot_height=710, title=f"{col1_title}/{col2_title}",x_axis_label = f'{col1_title}',
            y_axis_label = f'{col2_title}',toolbar_location="right", tools="pan,wheel_zoom,box_zoom,reset, hover, save,tap, crosshair")
        p.circle(xaxis, yaxis)

    p.add_tools(LassoSelectTool())
    p.add_tools(WheelZoomTool())
    script,div = components(p)
    return script, div

class VisualView(views.APIView):

    def post(self, request):
        if request.method == 'POST':
            try:
                col1_title,col2_title,col1_data,col2_data = request.data['col1_title'],request.data['col2_title'],request.data['col1_data'],request.data['col2_data']
                div_block,js_block = api_visual(col1_title,col2_title,col1_data,col2_data)
                data = [{'div':div_block,'js':js_block}]
                results = VisualSerializer(data, many=True).data
            except Exception as e:
                return Response({"Error": e})   #"Syntax Error,please check the API usage"})
            return Response(results)