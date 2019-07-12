from django.shortcuts import render,redirect

# Create your views here.
def upload(request):
	print(request.method)
	if request.method == 'POST':
		print("post")
		try:
			loaded_file = request.FILES['document']
			print(loaded_file.name)
		except:
			pass
	return render(request,"upload.html") 


def analyze(request):
	return render(request,"footer.html")