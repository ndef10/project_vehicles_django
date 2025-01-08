from django.urls import path
from . import views 


urlpatterns = [
    path('', views.v_index, name = 'index'),
    path('vehicle/add', views.v_add, name = 'add'),
    path('vehicle/listar', views.v_listar, name = 'listar')
]