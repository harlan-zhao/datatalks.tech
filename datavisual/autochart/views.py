from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
import os
import time
from .models import UserFile
import shutil

from .data_analyze import analyze,get_columns



cookie_time = 3000 # store cookie for only 60 seconds for testing
# Create your views here.
def upload(request,context={}):
	cur_time = time.time()

	for obj in UserFile.objects.all():
		folder_name = str(obj.id)
		if int(obj.time) + cookie_time < int(cur_time):
			try:
				shutil.rmtree(f'/home/harlanzhao/files/{folder_name}')
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
				UserFile.objects.filter(id = int(folder_id)).update_or_create(time=cur_time)


			except:
				user = UserFile.objects.create(time=cur_time)
				request.session['id'] = str(user.id)
				folder_id = request.session['id']


			fs = FileSystemStorage(location=folder+'/'+folder_id)
			filename = fs.save(my_file.name, my_file)
			file_url = fs.url(filename)
		else:
			return redirect("../upload",context={'warning':'Wrong Type of Files Detected','color':'red'})

	return render(request,"upload.html",context=context)

def checkbox(request,context={}):
	if request.method == 'POST':
		if request.POST.getlist('checks')==[]:
			print(1)
			context['filechoose_warning'] = 'Please Choose One File'
		else:
			try:
				del context['filechoose_warning']
			except:
				pass
			request.session['filename'] = request.POST.getlist('checks')[0]
			return redirect('../visualization')

	try:
		names = []
		folder_name = request.session['id']
		if len(os.listdir(f'/home/harlanzhao/files/{folder_name}')) > 1:
			for file in os.listdir(f'/home/harlanzhao/files/{folder_name}'):
				names.append(file)
			context['files'] = names
			return render(request,"filechoose.html",context=context)
		else:
			# for file in os.listdir(f'./files/{folder_name}'):
			request.session['filename'] = os.listdir(f'/home/harlanzhao/files/{folder_name}')[0]
		return  redirect('../visualization')

	except:
		return redirect("../upload",context={'warning':'Session Ended','color':'red'})



def visualization(request,context={}):
	filename = request.session['filename']
	file_id = request.session['id']
	columns = get_columns(file_id,filename)
	if not columns:
		context = {'invalid':'The file you uploaded has no columns,please use a valid file.'}

		return render(request, 'visualization.html',context)
	context['columns'] = columns
	context['filename'] = filename
	instances = []
	try:
		del context['warning']
	except:
		pass
	if request.method == "POST":
		context['warning'] = ""
		instances = request.POST.getlist('instances')
		if not instances:
			context['warning'] = 'No instances chosen'
			return render(request, 'visualization.html' , context)
		if len(instances) == 1:
			script, div = analyze(file_id,filename,instances[0],instances[0])
		else:
			script, div = analyze(file_id,filename,instances[0],instances[1])
		context['div'] = div
		context['script'] = script

		context['display_image'] = 'none'


		return render(request, 'visualization.html' , context)

	context['display_image'] = 'true'
	try:
		del context['div']
		del context['script']
	except:
		pass

	return render(request, 'visualization.html' , context)

def filecheck(request):
	try:
		folder_name = request.session['id']
		if os.path.exists(f'/home/harlanzhao/files/{folder_name}'):
			return redirect('../filechoose')
		else:
			return upload(request,context={'warning':'Session Ended','color':'red'})
	except:
		return upload(request,context={'warning':'Wrong Type of Files Detected','color':'red'})

