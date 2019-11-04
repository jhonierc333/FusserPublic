from django.conf.urls import url, include
from usuarios import views


urlpatterns = [
	url(r'^registro$', views.signup, name='registro'),
	url(r'^inicio$', views.login_view, name='inicio'),



]
