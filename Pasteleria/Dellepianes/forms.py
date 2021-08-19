from django import forms
from django.forms import modelformset_factory
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class UsuarioForm(UserChangeForm):
	class Meta:
		model= User
		fields= ('first_name',)


class UsuarioDetalleForm(UserChangeForm):
	class Meta:
		model= UsuarioDetalle
		fields= ('DNI', 'Mail', 'Telefono')

class ProductoForm(forms.ModelForm):
 	class Meta:
 		model= Producto
 		fields=('Nombre', 'Descripcion', 'Tipo_de_producto', 'Precio',)

class ImagenesForm(forms.ModelForm):	
	class Meta:
		model= ProductoImagen	
		exclude= ('Producto',)

ImagenesFormset= modelformset_factory(ProductoImagen, exclude= ('Producto',), extra= 1)