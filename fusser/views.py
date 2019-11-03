from usuarios.forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get('email')
		form_mensaje = form.cleaned_data.get('mensaje')
		form_nombre = form.cleaned_data.get('nombre')
		asunto = 'Form de contacto'
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from]
		email_mensaje = '%s: %s enviado por %s'%(form_nombre, form_mensaje, form_email)
		send_mail(asunto,
			email_mensaje,
			email_from,
			email_to,
			fail_silently = True
		)
	context = {
		'form':form,
	}
	return render(request, 'contact.html', context)
