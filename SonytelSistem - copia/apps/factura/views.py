from django.shortcuts import render
from apps.sistema.models import Factura,Clientes
from apps.sistema.views import registrarCliente
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	
from django.contrib import admin

# Create your views here.
class index(TemplateView):
	template_name='inicio/index.html'


#CREAR CLIENTE
class registrarFactura(CreateView):
	template_name='factura/crear.html'
	model=Factura
	success_url=reverse_lazy('home')

#LISTAR Factura
class listarFactura(ListView):
	template_name='factura/reportarFactura.html'
	context_object_name='facturas'
	model=Factura

#ACTUALIZAR Factura
class editarFactura(UpdateView):
	model = Factura
	template_name= 'factura/editar.html'
	success_url=reverse_lazy('home')

#ELIMINAR Factura
class eliminarFactura(DeleteView):
	model = Factura
	context_object_name="facturas"
	template_name = 'factura/eliminar.html'
	success_url = reverse_lazy('home')

#FILTRAR Factura
class filtrarFactura(TemplateView):
	template_name='factura/filtrar.html'


#RETORNO AJAX FILTRADO
class filtrarAjaxFactura(TemplateView):
	def get(self,request,*args,**kwargs):
		nombreFactura = request.GET.get('nombre')
		factura = Factura.objects.filter(cli_id__contains =nombreFactura)
		data = serializers.serialize('json',factura,fields=('fac_subtotal','fac_iva','fac_descuento','fac_total','fac_fecha','fac_estado','ciu'))
		return HttpResponse(data,content_type='application/json')


