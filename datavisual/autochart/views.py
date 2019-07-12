from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import os

# Create your views here.
def upload(request):
	content ={'warning':'Pleas Upload Only CSV File'}
	if request.method == 'POST' and request.FILES:
		folder = 'files'
		my_file = request.FILES['document']
		fs = FileSystemStorage(location=folder)
		filename = fs.save(my_file.name, my_file)
		file_url = fs.url(filename)
		return render(request, 'upload.html', content)
	return render(request,"upload.html",content)


def analyze(request):
	if len(os.listdir('./files') ) == 0:
		content ={'warning':'wrong file'}
		# return render(request,"upload.html",content)
		return redirect("../upload/")


	return render(request,"visualization.html")