from django.shortcuts import render
from .models import Clientes,Ciudad
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	

# Create your views here.
class index(TemplateView):
	template_name='inicio/index.html'
#CREAR CLIENTE
class registrarCliente(CreateView):
	template_name='cliente/registrarcliente.html'
	model=Clientes
	success_url=reverse_lazy('home')
#LISTAR CLIENTE
class listarCliente(ListView):
	template_name='cliente/reportarcliente.html'
	context_object_name='clientes'
	model=Clientes
#ACTUALIZAR CLIENTE
class editar(UpdateView):
	model = Clientes
	template_name= 'cliente/editar.html'
	success_url=reverse_lazy('home')
#ELIMINAR CLIENTE
class eliminar(DeleteView):
	model = Clientes
	context_object_name="clientes"
	template_name = 'cliente/eliminar.html'
	success_url = reverse_lazy('home')
#FILTRAR CLIENTE
class filtrarCliente(TemplateView):
	template_name='cliente/filtrar.html'
#RETORNO AJAX FILTRADO
class filtrarAjaxcliente(TemplateView):
	def get(self,request,*args,**kwargs):
		nombrecliente = request.GET.get('nombre')
		cliente = Clientes.objects.filter(cli_nombre__contains =nombrecliente)
		data = serializers.serialize('json',cliente,fields=('cli_nombre','cli_cedula','cli_apellido','cli_direccion','cli_telefono','cli_email','cli_estado','ciu'))
		return HttpResponse(data,content_type='application/json')
