from django.db import models
from django.shortcuts import render
# Create your models here.

class Person(models.Model):
	cedula =  models.CharField(max_length=15, primary_key=True)
	username =  models.CharField(max_length=50)
	phone_number = models.CharField(max_length=20, blank=True)
	email = models.EmailField()
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.username
