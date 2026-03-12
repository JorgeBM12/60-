from django.urls import path
from . import views

urlpatterns = [

path('', views.inicio, name='inicio'),
path('servicios/', views.servicios, name='servicios'),
path('eventos/', views.eventos, name='eventos'),
path('registro/', views.registro, name='registro'),

]