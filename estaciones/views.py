from django.shortcuts import render

from django.views import generic
from estaciones.forms import EstacionForm
from estaciones.forms import ProductForm
from estaciones.forms import ServiceForm
from estaciones.models import Service
from estaciones.models import Product
# Create your views here.

from django.core.urlresolvers import reverse_lazy

def crear_estacion(request):
	if request.method == 'POST':
		form = EstacionForm(request.POST)

		if form.is_valid():
			form.save()
		#return redirect('usuario:usuario_creado')

	else:
		form = EstacionForm()


	return render(request, 'estacion_form.html', {'form':form})

def crear_producto(request):
	if request.method == 'POST':
		form = ProductForm(request.POST)

		if form.is_valid():
			form.save()
		#return redirect('usuario:usuario_creado')

	else:
		form = ProductForm()


	return render(request, 'productos_form.html', {'form':form})

def crear_servicio(request):
	if request.method == 'POST':
		form = ServiceForm(request.POST)

		if form.is_valid():
			form.save()
		#return redirect('usuario:usuario_creado')

	else:
		form = ServiceForm()


	return render(request, 'servicios_form.html', {'form':form})

class ServiceList(generic.ListView):
	model = Service
	template_name = 'service_list.html'

class ProductoList(generic.ListView):
	model = Product
	template_name = 'product_list.html'

class ProductoDelete(generic.DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('estaciones:listar_productos')

class ServiceDelete(generic.DeleteView):
    model = Service
    template_name = 'service_delete.html'
    success_url = reverse_lazy('estaciones:listar_servicios')
