from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import os
import time
from .models import userfile
import shutil

# Create your views here.
def upload(request,context={}):
	cur_time = time.time()

	for obj in userfile.objects.all():
		folder_name = str(obj.id)
		if int(obj.time) + 3000 < int(cur_time):
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
			
			except:
				user = userfile.objects.create(time=cur_time)
				request.session['id'] = str(user.id)
				folder_id = request.session['id']

			fs = FileSystemStorage(location=folder+'/'+folder_id)
			filename = fs.save(my_file.name, my_file)
			file_url = fs.url(filename)
		else:
			return redirect("../upload",context={'warning':'Wrong Type of Files Detected','color':'red'})

	return render(request,"upload.html",context=context)

def visualization(request):
	folder_name = request.session['id']
	if os.path.exists(f'./files/{folder_name}'):
		return HttpResponse(folder_name)
	else:
		return upload(request,context={'warning':'Session Ended','color':'red'})
	



def filecheck(request):
	try: 
		folder_name = request.session['id']
		user_id = int(folder_name)
		if os.path.exists(f'./files/{folder_name}'):
			return visualization(request)
		else:
			return upload(request,context={'warning':'Session Ended,Please Reupload','color':'red'})
	except:		
		return upload(request,context={'warning':'Wrong Type of Files Detected','color':'red'})

