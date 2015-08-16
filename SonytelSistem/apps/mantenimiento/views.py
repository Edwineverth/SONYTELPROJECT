from django.shortcuts import render,render_to_response,RequestContext
from apps.sistema.models import Solicitudmantenimiento, Clientes,Articulossegunda
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers	
from django.db.models import Q

def generarRegistroMantenimiento(request):
	
	
	return render_to_response('mantenimiento/apertura.html',context_instance=RequestContext(request))
	