from django import forms

from usuarios.models import Profile
from django.contrib.auth.models import User


class ContactForm(forms.Form):
	nombre = forms.CharField(max_length=100)
	email = forms.EmailField()
	mensaje = forms.CharField(widget=forms.Textarea)
