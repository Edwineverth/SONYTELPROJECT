from django.shortcuts import render
from apps.sistema.models import Proveedor
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	


# Create your views here.
class crearProveedor(CreateView):
	template_name='proveedor/crear.html'
	model=Proveedor
	success_url=reverse_lazy('home')

#LISTAR ARTICULOS
class listarProveedor(ListView):
	template_name='proveedor/editar.html'
	context_object_name='Proveedores'
	model=Proveedor
#ACTUALIZAR ARTICULOS
class editarProveedor(UpdateView):
	model = Proveedor
	template_name= 'proveedor/editar.html'
	success_url=reverse_lazy('home')
#ELIMINAR ARTICULOS
class eliminarProveedor(DeleteView):
	model = Proveedor
	context_object_name="Proveedores"
	template_name = 'proveedor/eliminar.html'
	success_url = reverse_lazy('home')