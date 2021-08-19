from django.urls import path,include
from .views import *

urlpatterns = [
	path('process_pedido', process_pedido, name='process_pedido'),
]