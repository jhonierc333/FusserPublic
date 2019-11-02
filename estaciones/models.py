from django.db import models

# Create your models here.


class Station(models.Model):
	id_station = models.CharField(max_length=15, primary_key=True)
	station_name = models.CharField(max_length=40, blank=True)
	phone_number = models.CharField(max_length=20, blank=True)
	detail = models.CharField(max_length=100, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.station_name


class Product(models.Model):
	id_product = models.CharField(max_length=15, primary_key=True)
	product_name = models.CharField(max_length=50, blank=False)
	price = models.CharField(max_length=10, blank=False)
	detail = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.product_name

class Service(models.Model):
	id_service = models.CharField(max_length=15, primary_key=True)
	service_name = models.CharField(max_length=50, blank=False)
	price = models.CharField(max_length=10, blank=False)
	detail = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.service_name

class gasoil_today(models.Model):
	price = models.CharField(max_length=10, blank=False)

	def __str__(self):
		return self.price
