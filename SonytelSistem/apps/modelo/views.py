from django.shortcuts import render
from apps.sistema.models import Modelo
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	


# Create your views here.
class crearModelo(CreateView):
	template_name='modelos/crear.html'
	model=Modelo
	success_url=reverse_lazy('home')

#LISTAR ARTICULOS
class listarModelo(ListView):
	template_name='modelos/editar.html'
	context_object_name='modelos'
	model=Modelo
#ACTUALIZAR ARTICULOS
class editarModelo(UpdateView):
	model = Modelo
	template_name= 'modelos/editar.html'
	success_url=reverse_lazy('home')
#ELIMINAR ARTICULOS
class eliminarModelo(DeleteView):
	model = Modelo
	context_object_name="modelos"
	template_name = 'modelos/eliminar.html'
	success_url = reverse_lazy('home')