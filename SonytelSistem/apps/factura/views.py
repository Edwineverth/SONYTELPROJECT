from django.shortcuts import render
from apps.sistema.models import Factura,Clientes,Facturadetalle,Productos
from apps.sistema.views import registrarCliente
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, render_to_response, RequestContext, HttpResponse, HttpResponseRedirect

from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	
from django.contrib import admin
from django.contrib.auth.models import User



def generarVentaFactura(request):

	objetosplantilla = {"listarclientes":Clientes.objects.filter(cli_estado="A"),"listarproductos":Productos.objects.all(),'nFactura': 1+Factura.objects.count()}
	print objetosplantilla
	return render_to_response('factura/crear.html', objetosplantilla, context_instance=RequestContext(request))

def guardarFactura(request):

	codigoProducto= request.GET['codigo']
	cantidad = request.GET['cantidad']
	precio = request.GET['precio']
	cedula = request.GET['cedula']

	listarClientes = Clientes.objects.get(cli_cedula=cedula)
	listarProductos = Productos.objects.get(pro_codigo=codigoProducto)

	
	""



