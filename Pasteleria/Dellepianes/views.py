from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from cart.cart import Cart

from .models import *
from .forms import *


def Perfil(request):
	""" La vista toma todos los datos del usuario y las lleva a la pagina del perfil """
	args={'user':request.user, 'detalle': request.user.usuariodetalle}
	return render(request, 'Perfil.html', args)

def Cuenta_Edit(request):
	""" La vista se encarga de editar y guardar en el sistema los datos 
	que el usuario tiene disponible """
	if request.method == 'POST':

		user_form = UsuarioForm(request.POST, instance=request.user)
		detalle_form = UsuarioDetalleForm(request.POST, instance=request.user.usuariodetalle)
	
		if user_form.is_valid() and detalle_form.is_valid():
				usuario = user_form.save(commit=False)
				detalle = detalle_form.save(commit=False)
				usuario.save()
				detalle.save()
				return redirect('Perfil',)
	else:
		user_form = UsuarioForm(request.POST, instance=request.user)
		detalle_form = UsuarioDetalleForm(request.POST, instance=request.user.usuariodetalle)
	return render(request, 'Cuenta_Edit.html', {'user_form':user_form, 'detalle_form':detalle_form} )

def Home(request):
	cart = Cart(request)
	return render(request, 'home.html')

def Sobre_Mi (request):
	return render(request, 'Sobre_Mi.html')

def Contacto(request):
	return render(request, 'Contacto.html')

def Pedidos(request):
	cart = Cart(request)
	args={
		'producto': Producto.objects.all(),
		'imagenes': ProductoImagen.objects.all()
	}
	return render(request, 'Pedidos.html', args)

def Productos(request, pk):
	i = 0
	args={
		'producto': get_object_or_404(Producto, pk=pk),
		'imagenes': ProductoImagen.objects.all(),
		'i': i
	}
	return render(request, 'Producto.html', args)

def New_Producto(request):
	context = {}
	if request.method == 'POST':
		productof = ProductoForm(request.POST)		
		
		if productof.is_valid():
			producto= productof.save()
			producto.save()

			objeto = producto.pk

			imagenform = ImagenesForm(request.POST, request.FILES)
			if imagenform.is_valid():
				imagen = imagenform.save(commit= False)
				imagen.Producto_id = objeto
				imagen.save()


			return redirect('Home')
			
	else:
		productof = ProductoForm()
		imagenform = ImagenesForm()
	
	context['productof'] = productof
	context ['imagenform'] = imagenform
	return render(request, 'AñadirProducto.html', context)

def Producto_Edit(request, pk):
	args={}
	if request.method == 'POST':
		post= get_object_or_404(Producto, pk=pk)
		productof = ProductoForm(request.POST, instance= post)
		if productof.is_valid():
			producto= productof.save()
			producto.save()

			objeto = producto.pk

			imagenform = ImagenesForm(request.POST, request.FILES)
			
			imagen = imagenform.save(commit= False)
			imagen.Producto_id = objeto
			imagen.save()
			return redirect('Producto', pk= producto.pk)
	else:
		productof = ProductoForm()
		imagenform = ImagenesForm()
	
	args['productof'] = productof
	args['imagenform']= imagenform
	return render(request, 'EditarProducto.html', args)


def Add(request):
    cart = Cart(request.session)
    product = Producto.objects.get(id=request.GET.get('Producto_id'))
    cart.add(product, price=product.Precio)
    return HttpResponse("Added")

def show(request):
    return render(request, 'shopping/show-cart.html')
