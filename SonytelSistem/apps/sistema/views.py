from django.shortcuts import render
from .models import Clientes
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
# Create your views here.
class index(TemplateView):
	template_name='inicio/index.html'
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