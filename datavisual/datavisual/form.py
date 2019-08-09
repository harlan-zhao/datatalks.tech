from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control',
		'placeholder':'Name'
		}),required=True)
	email = forms.EmailField(widget=forms.TextInput(attrs={
		'class':'form-control',
		'placeholder':'Email'
		}))
	message = forms.CharField(widget=forms.Textarea(attrs={
		'class':'form-control',
		'placeholder':'Message'
		}))

		
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']