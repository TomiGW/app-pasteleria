from django.urls import path,include
from django.conf.urls import url
from django.conf import settings 
from django.conf.urls.static import static 
from . import views
from .models import *

urlpatterns = [
	path('', views.Home, name='Home'),
	path('MiCuenta/', views.Perfil, name='Perfil'),
	path('MiCuenta_edit/', views.Cuenta_Edit, name='Cuenta_Edit'),
	path('Sobre_Mi/', views.Sobre_Mi, name='Sobre_Mi'),
	path('Contacto/', views.Contacto, name='Contacto'),
	path('Pedidos/', views.Pedidos, name='Pedidos'),
	path('Producto/<int:pk>', views.Productos, name='Producto'),
	path('AñadirProducto/', views.New_Producto, name='AñadirProducto'),
	path('EditarProducto/<int:pk>', views.Producto_Edit, name='EditarProducto'),
]
if settings.DEBUG: 
		urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 