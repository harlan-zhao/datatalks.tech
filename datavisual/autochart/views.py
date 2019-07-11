from django.shortcuts import render,redirect

# Create your views here.
def upload(request):
	print(request)
	if request.method == 'POST':
		print("submit")
		try:
			loaded_file = request.FILES['document']
		except:
			pass
	return render(request,"upload.html") 


def visualization(request,file):
	return render(request,"visualization.html")

