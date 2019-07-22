from django.shortcuts import render,HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from .form import ContactForm
from django.contrib import messages

def mail(name,message,email):
	subject = 'email from datatalks.tech'
	from_email = settings.EMAIL_HOST_USER
	to_email = ['zhaohehe520@gmail.com']
	contact_message = f"name:{name}\n" + f"email: {email}\n" + "content:\n" +f"{message}"
	send_mail(subject,
		contact_message,
		from_email,
		to_email,
		fail_silently = False)

def homepage(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			message = form.cleaned_data['message']
			mail(name,message,email)
			messages.success(request,'Email sent successfully, Thank You!')
			return HttpResponseRedirect('#contact')  #form.get_absolute_url()
		else:
			messages.error(request,'Information is not valid')
			return HttpResponseRedirect('#contact')


	form = ContactForm()
	return render(request,'index.html',{'form':form})