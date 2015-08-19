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
	


class listarFacturas(ListView):
	template_name='factura/filtrar.html'
	context_object_name='listarFacturas'
	model=Factura
	def get_context_data(self, **kwargs):
		ctx = super(listarFacturas, self).get_context_data(**kwargs)
		ctx['clientes'] = Clientes.objects.all()
		return ctx

				
def generarVentaFactura(request):

	objetosplantilla = {"listarclientes":Clientes.objects.filter(cli_estado="A"),"listarProductos":Productos.objects.all(),'nFactura': 1+Factura.objects.count()}
	return render_to_response('factura/crear.html', objetosplantilla, context_instance=RequestContext(request))

def guardarFactura(request):
	print "ENTROOOOO :V :v "
	codigoProducto= request.GET['codigo']
	cantidad = request.GET['cantidad']
	precio = (request.GET['precio'])
	cedula = request.GET['cedula']
	total =request.GET['total']
	num = request.GET['numero']
	print "SIGEEEE"
	print cedula
	listarClientes = Clientes.objects.get(cli_cedula=cedula)
	print "LISTA CLIENTES"

	listarProductos = Productos.objects.get(id=codigoProducto)
	unCliente= Clientes.objects.get(cli_cedula=cedula)
	print unCliente.id
	f = Factura.objects.filter(id=request.GET['nFactura']).count()
	print request.GET['nFactura']
	print f

	if str(num) =='1':
		fact = Factura(fac_subtotal=request.GET['subtotal'],
			fac_iva=request.GET['iva'],
			fac_descuento=request.GET['descuento'],
			fac_total =request.GET['total'],
			fac_fecha=request.GET['fecha'],
			fac_estado="F",
			cli_id= unCliente.id
			)
		fact.save()
	detalle = Facturadetalle(
		det_cantiadd=cantidad,
		det_preciou= precio,
		det_preciot= total,
		fac_id = request.GET['nFactura'],
		pro_id= listarProductos.id
		)
	detalle.save()
	refrescarStock = listarProductos.pro_cantidad - int(cantidad)
	#PROCESO PARA ACTUALIZAR EL STOCK DEL PRODUCTO ES NECESARIO INGRESAR TODAS LAS CANTIDADES  DEL PRODUCTO
	producto = Productos(
		id=listarProductos.id,
		pro_nombre= listarProductos.pro_nombre,
		pro_cantidad= refrescarStock ,
		pro_precio= listarProductos.pro_precio ,
		pro_ecg = "ESQ",
		pro_tarifa_iva = listarProductos.pro_tarifa_iva,
		pro_ex = listarProductos.pro_ex,
		pro_pvp = listarProductos.pro_pvp,
		mar_id = listarProductos.mar_id,
		)
	producto.save()
	return render_to_response('factura/crear.html',context_instance=RequestContext(request))

	