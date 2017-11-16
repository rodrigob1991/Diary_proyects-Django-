from django.conf.urls import url
from .import views

urlpatterns=[
	url(r'^$', views.proyect_name, name='proyect_name'),
	url(r'^proyect/(?P<primary_key>[0-9]+)/',views.proyect_description, name='proyect_description'),
	url(r'^new_proyect/', views.create_proyect,name='create_proyect'),
]