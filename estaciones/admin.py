from django.contrib import admin

# Register your models here.

from estaciones.models import Station
from estaciones.models import Product
from estaciones.models import Service


admin.site.register(Station)
admin.site.register(Product)
admin.site.register(Service)
