from django.conf.urls import url, include
from usuarios import views


urlpatterns = [
	url(r'^nuevo$', views.crear_usuario, name='crear_usuario'),


]