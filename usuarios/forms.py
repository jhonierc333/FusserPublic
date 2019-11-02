from django import forms

from usuarios.models import Person


class UsuarioForm(forms.ModelForm):
	class Meta:
		model = Person

		fields = '__all__'

		labels = {

			'cedula':'Cedula',
			'username':'Username',
			'phone_number':'Phone_number',
			'email' :'Email',
			'picture':'Picture',


		}

	def __init__(self, *args, **kwargs):
		super(UsuarioForm, self).__init__(*args, **kwargs)

		for field in self.fields:
			self.fields[field].widget.attrs.update({'class':'form_control'})
