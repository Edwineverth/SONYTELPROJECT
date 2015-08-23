from django.shortcuts import render
from .models import Clientes,Ciudad,Productos
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView,FormView
from django.http import HttpResponse
from django.core import serializers	
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, render_to_response, RequestContext, HttpResponse, HttpResponseRedirect

import json
from .forms import TestForm
class AjaxTemplateMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'ajax_template_name'):
            split = self.template_name.split('.html')
            split[-1] = '_inner'
            split.append('.html')
            self.ajax_template_name = ''.join(split)
        if request.is_ajax():
            self.template_name = self.ajax_template_name
        return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)

class TestFormView(SuccessMessageMixin, AjaxTemplateMixin, FormView):
    template_name = 'cliente/test_form.html'
    form_class = TestForm
    
    success_url = reverse_lazy('login')
    success_message = "Way to go!"
    
    
# Create your views here.

				
def presentacionsistema(request):

	objetosplantilla = {'productos': Productos.objects.all() }
	return render_to_response('index.html', objetosplantilla, context_instance=RequestContext(request))

class index(TemplateView):
	template_name='index.html'
	model = Productos
	context_object_name = "Productos"

#CREAR CLIENTE
class registrarCliente(CreateView):
	#registrarcliente"
	template_name='cliente/registrarcliente.html'
	model=Clientes
	success_url=reverse_lazy('login')
#LISTAR CLIENTE
class listarCliente(ListView):
	template_name='cliente/reportarcliente.html'
	context_object_name='clientes'
	model=Clientes
#ACTUALIZAR CLIENTE
class editar(UpdateView):
	model = Clientes
	tempalte_name= 'cliente/editar.html'
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
#
#RETORNO AJAX FILTRADO
class filtrarAjaxcliente(TemplateView):
	def get(self,request,*args,**kwargs):
		nombrecliente = request.GET.get('nombre')
		cliente = Clientes.objects.filter(cli_nombre__contains =nombrecliente)
		data = serializers.serialize('json',cliente,fields=('cli_nombre','cli_cedula','cli_apellido','cli_direccion','cli_telefono','cli_email','cli_estado','ciu'))
		return HttpResponse(data,content_type='application/json')
