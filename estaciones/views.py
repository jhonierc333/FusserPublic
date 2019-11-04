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

class crear_producto(generic.CreateView):
	model = Product
	form_class = ProductForm
	template_name = 'productos_form.html'
	success_url = reverse_lazy('estaciones:listar_productos')

class crear_servicio(generic.CreateView):
	model = Service
	form_class = ServiceForm
	template_name = 'servicios_form.html'
	success_url = reverse_lazy('estaciones:listar_servicios')

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
