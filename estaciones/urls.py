from django.conf.urls import url, include
from estaciones import views



urlpatterns = [
	url(r'^nueva$', views.crear_estacion, name='crear_estacion'),
	url(r'^nuevo_producto$', views.crear_producto.as_view(), name='crear_producto'),
	url(r'^listar_producto$', views.ProductoList.as_view(), name='listar_productos'),
	url(r'^eliminar_producto/(?P<pk>[\w]+)$', views.ProductoDelete.as_view(), name='eliminar_producto'),

	url(r'^nuevo_servicio$', views.crear_servicio.as_view(), name='crear_servicio'),
	url(r'^listar_servicios$', views.ServiceList.as_view(), name='listar_servicios'),
	url(r'^eliminar_servicio/(?P<pk>[\w]+)$', views.ServiceDelete.as_view(), name='eliminar_servicio'),

]
