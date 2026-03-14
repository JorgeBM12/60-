from django.urls import path
from . import views

urlpatterns = [

path('', views.inicio, name='inicio'),
path('servicios/', views.servicios, name='servicios'),
path('eventos/', views.eventos, name='eventos'),
path('registro/', views.registro, name='registro'),
path('redirect/', views.redirect_user, name='redirect_user'),
path('evento/crear/', views.crear_evento, name='crear_evento'),
path('evento/editar/<int:id>/', views.editar_evento, name='editar_evento'),
path('evento/eliminar/<int:id>/', views.eliminar_evento, name='eliminar_evento'),
path('acceso-requerido/', views.acceso_requerido, name='acceso_requerido'),
path('evento/<int:id>/', views.detalle_evento, name='detalle_evento'),

]