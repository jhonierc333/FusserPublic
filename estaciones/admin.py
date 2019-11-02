from django.contrib import admin

# Register your models here.

from estaciones.models import Station
from estaciones.models import Product
from estaciones.models import Service


admin.site.register(Station)
@admin.register(Product)
@admin.register(Service)



class ProductAdmin(admin.ModelAdmin):
	list_display = ('id_product', 'product_name', 'price', 'detail')



class ServiceAdmin(admin.ModelAdmin):
	list_display = ('id_service', 'service_name', 'price', 'detail')
