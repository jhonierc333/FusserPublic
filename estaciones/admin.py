from django.contrib import admin

from estaciones.models import Station, Product, Service


admin.site.register(Station)
admin.site.register(Service)


@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
	list_display = ('pk', 'product_name', 'price', 'detail')
