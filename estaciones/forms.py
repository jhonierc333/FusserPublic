from django import forms

from estaciones.models import Station
from estaciones.models import Product
from estaciones.models import Service


class EstacionForm(forms.ModelForm):
	class Meta:
		model = Station
		fields = '__all__'
		labels = {
			'id_station':'Id_estacion',
			'station_name':'Station_name',
			'phone_number' : 'Phone_number',
			'detail' : ' Detail',

		}

	def __init__(self, *args, **kwargs):
		super(EstacionForm, self).__init__(*args, **kwargs)

		for field in self.fields:
			self.fields[field].widget.attrs.update({'class':'form_control'})

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = '__all__'
		labels = {
			'id_product' : 'Id producto',
			'product_name' :'Nombre del producto ',
			'price' : 'Precio',
			'detail' : 'Detalle'
		}

	def __init__(self, *args, **kwargs):
		super(ProductForm, self).__init__(*args, **kwargs)

		for field in self.fields:
			self.fields[field].widget.attrs.update({'class':'form_control'})


class ServiceForm(forms.ModelForm):
	class Meta:
		model = Service
		fields = '__all__'
		labels = {

			'id_service' : 'Id servicio',
			'service_name' : 'Nombre del servicio',
			'price' : 'Precio',
			'detail': 'Detalle',
		}

	def __init__(self, *args, **kwargs):
		super(ServiceForm, self).__init__(*args, **kwargs)

		for field in self.fields:
			self.fields[field].widget.attrs.update({'class':'form_control'})
