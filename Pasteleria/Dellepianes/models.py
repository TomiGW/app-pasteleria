from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UsuarioDetalle(models.Model):
	""" Este modelo extiende el modelo predeterminado de los usuarios,
	agrega los datos restantes y se crea en el momento que un usario se loguea """
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	DNI= models.IntegerField(blank= True, null=True)
	Telefono= models.CharField(max_length= 255, null=True)
	Mail= models.CharField(max_length= 255, null=True)

	def __str__(self):
		return '%s'%(self.user)

	@receiver(post_save, sender=User)
	def create_user_usuariodetalle(sender, instance, created, **kwargs):
		if created:
			UsuarioDetalle.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_user_usuariodetalle(sender, instance, **kwargs):
		instance.usuariodetalle.save()

class Tipo_Producto(models.Model):
	Tipo_de_producto= models.CharField(max_length= 255)

	def __str__(self):
		return self.Tipo_de_producto

class Producto(models.Model):
	Nombre= models.CharField(max_length= 255)
	Descripcion= models.CharField(max_length= 255)
	Tipo_de_producto= models.ForeignKey(Tipo_Producto, on_delete=models.CASCADE)
	Cantidad = models.IntegerField(blank=True, null=True)
	Precio= models.FloatField()
		
	def __str__(self):
		return self.Nombre

class ProductoImagen(models.Model):
	Producto= models.ForeignKey(Producto, on_delete=models.CASCADE)
	Imagen= models.ImageField(upload_to='imagenes/', null=True, blank= True,)

	def __str__(self):
		return '%s' % (self.Producto)


