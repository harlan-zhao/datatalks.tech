from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

# Create your views here.
def upload(request):
	if request.method == 'POST' and request.FILES:
		folder = 'files'
		my_file = request.FILES['document']
		fs = FileSystemStorage(location=folder)
		filename = fs.save(my_file.name, my_file)
		file_url = fs.url(filename)
		return render(request, 'upload.html', {'file_url': file_url})
	content ={'warning':'Pleas Upload Only CSV File'}
	return render(request,"upload.html",content)


def analyze(request):
	if request.FILES:
		print(1)
	return render(request,"visualization.html")