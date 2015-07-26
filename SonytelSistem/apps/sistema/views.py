from django.shortcuts import render
from .models import Clientes
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
# Create your views here.
class index(TemplateView):
	template_name='inicio/index.html'
#CREAR
class registrarCliente(CreateView):
	template_name='cliente/registrarcliente.html'
	model=Clientes
	success_url=reverse_lazy('home')

class reporteCliente(TemplateView):
	template_name='cliente/reportarcliente.html'

class listarCliente(ListView):
	template_name='cliente/reportarcliente.html'
	context_object_name='clientes'
	model=Clientes
class buscarCliente(TemplateView):

	def post(self,request,*args,**Kwargs):
		buscar = request.POST.get('buscalo')
		print buscar
		cliente = Clientes.objects.filter(cli_nombre__contains=buscar)
		print cliente
		return render(request,'cliente/buscarcliente.html',{'clientes':cliente,'cliente':True})
from django.core import serializers	
class buscadorAjaxCliente(TemplateView):
	def get(self,request,*args,**kwargs):
		id_cliente = request.GET.get('id')
		print id_cliente
		cliente = Clientes.objects.filter(id =id_cliente)
		data = serializers.serialize('json',cliente,fields=('cli_nombre','cli_cedula','cli_direccion','cli_telefono','cli_email','cli_estado','ciu'))
		return HttpResponse(data,content_type='application/json')

class busqueda(ListView):
	model = Clientes
	template_name = 'cliente/busqueda.html'
	context_object_name = 'clientes'

class editar(UpdateView):
	model = Clientes
	template_name= 'cliente/editar.html'
	success_url=reverse_lazy('home')
class eliminar(DeleteView):
	model = Clientes
	context_object_name="clientes"
	template_name = 'cliente/eliminar.html'
	success_url = reverse_lazy('home')