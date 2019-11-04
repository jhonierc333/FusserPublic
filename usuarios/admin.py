from django.contrib import admin

from usuarios.models import Profile

@admin.register(Profile)

class PersonAdmin(admin.ModelAdmin):
	list_display = ('pk', 'user', 'phone_number', 'email')
	list_filter = ('created', 'modified')
