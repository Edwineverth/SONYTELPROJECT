from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from django.shortcuts import render_to_response,get_object_or_404
from models import *
from forms import * 
#IMPORTACION PARA LOS FORMS
#from forms import * 
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,DeleteView,CreateView
"********************************************"
"FUNCIONES PARA EL CLIENTE"
# Create your views here.
def cliente(request):
	clientes = Clientes.objects.all()
	template = "clientes.html"
	return render(request,template,locals())
"CREACION DE CLIENTE CON FORMS"
def clientesadd(request):
	if request.POST:
		form = ClienteForm(request.POST)
		if form.is_valid():
			cliente = form.save(commit=False)
			usuario=request.user
			cliente.save()
			return HttpResponseRedirect("/")
	else:
		form = ClienteForm()
	template = "clienteAdd.html"
	return render_to_response(template,context_instance=RequestContext(request,locals()))		

"LISTADO DE CLIENTES"
class ClientesListView(ListView):
	model = Clientes
	context_object_name= 'clientes'
	def get_template_names(self):
		return 'clientes.html'
"DETALLE DE CLIENTE"
class ClienteDetailView(DetailView):
	model = Clientes
	context_object_name= 'clientes'
	def get_template_names(self):

		return 'clientes.html'

"********************************************"

@login_required
def editar_perfil(request):

    if request.method == 'POST':
        # formulario enviado
        user_form = UserForm(request.POST, instance=request.user)
        perfil_form = PerfilForm(request.POST, instance=request.user.perfil)

        if user_form.is_valid() and perfil_form.is_valid():
            # formulario validado correctamente
            user_form.save()
            perfil_form.save()
            return HttpResponseRedirect('/formulario-guardado/')

    else:
        # formulario inicial
        user_form = UserForm(instance=request.user)
        perfil_form = PerfilForm(instance=request.user.perfil)

    return render_to_response('editar_perfil.html', { 'user_form': user_form,  'perfil_form': perfil_form }, context_instance=RequestContext(request))