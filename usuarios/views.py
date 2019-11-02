from django.shortcuts import render, redirect

from usuarios.forms import UsuarioForm
# Create your views here.

def crear_usuario(request):
	if request.method == 'POST':
		form = UsuarioForm(request.POST)

		if form.is_valid():
			form.save()
		#return redirect('usuario:usuario_creado')

	else:
		form = UsuarioForm()


	return render(request, 'usuario_form.html', {'form':form})
