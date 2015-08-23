from django.shortcuts import render
from apps.sistema.models import Articulossegunda
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	


# Create your views here.



class crearArticulo(CreateView):
	template_name='articulos/reportar.html'
	model=Articulossegunda
	success_url=reverse_lazy('home')

#LISTAR ARTICULOS
class listarArticulos(ListView):
	template_name='articulos/listar.html'
	context_object_name='articulos'
	model=Articulossegunda
#ACTUALIZAR ARTICULOS
class editarArticulo(UpdateView):
	model = Articulossegunda
	template_name= 'articulos/actualizar.html'
	success_url=reverse_lazy('home')
#ELIMINAR ARTICULOS
class eliminarArticulo(DeleteView):
	model = Articulossegunda
	context_object_name="articulos"
	template_name = 'articulos/eliminar.html'
	success_url = reverse_lazy('home')