from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from Dellepianes.models import Producto

from .cart import Cart

# Create your views here.
@login_required
def add_producto(request, producto_id):
	cart = Cart(request)
	producto = Producto.objects.get(id=producto_id)
	cart.add(producto= producto)
	return redirect('Pedidos')


@login_required
def remove_producto(request, producto_id):
	cart = Cart(request)
	producto = Producto.objects.get(id=producto_id)
	cart.remove(producto)
	return redirect('Pedidos')

@login_required
def decrement_producto(request, producto_id):
	cart = Cart(request)
	producto = Producto.objects.get(id=producto_id)
	cart.decrement(producto= producto)
	return redirect('Pedidos')

@login_required
def clear_producto(request):
	cart = Cart(request)
	cart.clear()
	return redirect('Pedidos')
