from django.contrib import admin


from usuarios.models import Person

# Register your models here.


@admin.register(Person)

class PersonAdmin(admin.ModelAdmin):
	list_display = ('cedula', 'username', 'phone_number', 'email')
	list_filter = ('created', 'modified')
