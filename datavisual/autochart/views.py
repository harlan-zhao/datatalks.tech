from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import os
import time
from .models import userfile
import shutil
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool, LassoSelectTool, WheelZoomTool, PointDrawTool, ColumnDataSource
from bokeh.palettes import Category20c, Spectral6
from bokeh.transform import cumsum
from bokeh.resources import CDN
import pandas as pd


cookie_time = 1000 # store cookie for only 60 seconds for testing
# Create your views here.
def upload(request,context={}):
	cur_time = time.time()

	for obj in userfile.objects.all():
		folder_name = str(obj.id)
		if int(obj.time) + cookie_time < int(cur_time):
			try:
				shutil.rmtree(f'./files/{folder_name}')
			except:
				pass

			try:
				if request.session['id'] == str(obj.id):
					del request.session['id']
			except:
				pass
			obj.delete()


	if context == {}:
	    context ={'warning':'Please Upload Only CSV Files','color':'white'}
	if request.method == 'POST' and request.FILES:
		folder = 'files'
		my_file = request.FILES['document']
		name = my_file.name
		
		if name.endswith(".csv"):
			try:
				folder_id = request.session['id']
				userfile.objects.filter(id = int(folder_id)).update_or_create(time=cur_time)
				print(1)
			
			except:
				user = userfile.objects.create(time=cur_time)
				request.session['id'] = str(user.id)
				folder_id = request.session['id']
				print(2)

			fs = FileSystemStorage(location=folder+'/'+folder_id)
			filename = fs.save(my_file.name, my_file)
			file_url = fs.url(filename)
		else:
			return redirect("../upload",context={'warning':'Wrong Type of Files Detected','color':'red'})

	return render(request,"upload.html",context=context)

def checkbox(request):
	if request.method == 'POST':
		context = {'filename':request.POST.getlist('checks')[0]}
		return visualization(request,context)

	try:
		names = []
		context={'files':['test']}
		folder_name = request.session['id']
		if len(os.listdir(f'./files/{folder_name}')) > 1:		
			for file in os.listdir(f'./files/{folder_name}'):
				names.append(file)
			context = {'files':names}
			return render(request,"filechoose.html",context)
		else:
			for file in os.listdir(f'./files/{folder_name}'):
				context = {'filename':file}
			return visualization(request,context)
	
	except:
		print(1)
		return redirect("../upload",context={'warning':'Session Ended','color':'red'})

	
	
def visualization(request,context):
	lang = ['Python', 'JavaScript', 'C#', 'PHP', 'C++', 'Java']
	counts = [25, 30, 8, 22, 12, 17]
	p = figure(x_range=lang, plot_width=1020,plot_height=710, title="Programming Languages Popularity",
	       toolbar_location="right", tools="pan,wheel_zoom,box_zoom,reset, hover, save,tap, crosshair")

	source = ColumnDataSource(data=dict(lang=lang, counts=counts, color=Spectral6))
	p.add_tools(LassoSelectTool())
	p.add_tools(WheelZoomTool())       

	p.vbar(x='lang', top='counts', width=.8, color='color', legend="lang", source=source)
	p.legend.orientation = "horizontal"
	p.legend.location = "top_center"

	# p.xgrid.grid_line_color = "black"
	# p.y_range.start = 0
	# p.line(x=lang, y=counts, color="black", line_width=2)
	script, div = components(p)
	return render(request, 'visualization.html' , {'script': script, 'div':div})
 	# return render(request,"visualization.html",context)


def filecheck(request):
	try: 
		folder_name = request.session['id']
		user_id = int(folder_name)
		if os.path.exists(f'./files/{folder_name}'):
			return checkbox(request)
		else:
			return upload(request,context={'warning':'Session Ended','color':'red'})
	except:		
		return upload(request,context={'warning':'Wrong Type of Files Detected','color':'red'})

