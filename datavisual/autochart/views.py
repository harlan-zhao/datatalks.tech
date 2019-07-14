from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import os
import uuid

# Create your views here.
def upload(request,context={}):
	if context == {}:
	    context ={'warning':'Please Upload Only CSV Files','color':'white'}
	if request.method == 'POST' and request.FILES:
		folder = 'files'
		my_file = request.FILES['document']
		name = my_file.name
		if name.endswith(".csv"):
			try:
				folder_id = request.session['id']
			except:
				request.session['id'] = str(uuid.uuid1())
				request.session.set_expiry(0)
				folder_id = request.session['id'] 

			fs = FileSystemStorage(location=folder+'/'+folder_id)
			filename = fs.save(my_file.name, my_file)
			file_url = fs.url(filename)
		else:
			return redirect("../upload",{'warning':'Wrong Type of Files Detected','color':'red'})

	return render(request,"upload.html",context)

def visualization(request):
	folder_id = request.session['id']
	return HttpResponse(folder_id)
	return render(request,"visualization.html")



def filecheck(request):
	try: 
		folder_id = request.session['id']
		return redirect('../visualization')
	except:		
		return upload(request,{'warning':'Wrong Type of Files Detected','color':'red'})

