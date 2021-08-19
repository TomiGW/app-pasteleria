from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import F, Sum, FloatField
from Dellepianes.models import *

User = get_user_model()


class Pedido(models.Model):
	user= models.ForeignKey(User, on_delete=models.CASCADE)

	creado_desde= models.DateTimeField(auto_now_add= True)

	@property
	def tota(self):
		return self.pedidoline_set.aggregate(
			total=Sum(F("producto__Precio") * F("cantidad"), output_field=FloatField())
		)["total"] or FloatField(0)

	def __str__(self):
		return self.id


class PedidoLine(models.Model):
	user= models.ForeignKey(User, on_delete=models.CASCADE)
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
	cantidad = models.IntegerField(default= 1)
	creado_desde= models.DateTimeField(auto_now_add= True)

	def __str__(self):
		return f'{self.cantidad} de {self.producto.Nombre}'

	class Meta:
		db_table= 'orderlines'
		verbose_name= 'Linea de pedido'
		verbose_name_plural= 'Linea de pedidos'
		ordering= ['id']