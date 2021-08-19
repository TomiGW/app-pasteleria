from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import *

class UsuarioInLine(admin.StackedInline):
    model = UsuarioDetalle
    can_delete = False
    verbose_name_plural = 'Usuario_Detalle'

class UserAdmin(BaseUserAdmin):
    inlines = (UsuarioInLine,)



class ProductoImagenAdmin(admin.StackedInline):
	model=ProductoImagen


class ProductoAdmin(admin.ModelAdmin):
	
	inlines = [ProductoImagenAdmin]
	
	class Meta:
		model = Producto

class ProductoImangenAdmin(admin.ModelAdmin):
	pass


admin.site.register(Producto, ProductoAdmin)
admin.site.register(ProductoImagen)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


admin.site.register(Tipo_Producto)
