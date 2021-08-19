from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from .models import *
from cart.cart import Cart


@login_required

def process_pedido(request):
	pedido = Pedido.objects.create(user=request.user,)
	cart = Cart(request)
	pedido_lines = list()

	for key, value in cart.cart.items():
		pedido_lines.append(
			PedidoLine(
				producto_id=key,
				cantidad= value["Cantidad"],
				user= request.user,
				pedido= pedido
			)
		)

	PedidoLine.objects.bulk_create(pedido_lines)

	send_pedido_email(
		pedido = pedido,
		pedido_lines = pedido_lines,
		username = request.user.username,
		user_email= request.user.email,
	)

	cart.clear()

	messages.success(request, "El pedido se ha creado correctamente")

	return redirect('Pedidos')

def send_pedido_email(**kwargs):
	subject= "Gracias por tu pedido"
	html_messages= render_to_string("emails/nuevo_pedido.html", {
		"pedido": kwargs.get("pedido"),
		"pedido_lines": kwargs.get("pedido_lines"),
		"username": kwargs.get("username"),
	})

	plain_messages = strip_tags(html_messages)
	from_email = "tomi.loqi@gmail.com"
	to= kwargs.get("user_email")
	send_mail(subject, plain_messages, from_email, [to], html_message=html_messages,)