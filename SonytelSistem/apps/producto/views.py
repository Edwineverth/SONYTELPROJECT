from django.shortcuts import render
from apps.sistema.models import Productos,Categoria,Modelo
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, render_to_response, RequestContext, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	
from django.contrib import admin
from django.contrib.auth.models import User


class Insertar_Producto(CreateView):
	template_name="productos/crear.html"
	model=Productos
	reverse_lazy="sistema"


class listarProducto(ListView):
	template_name= "productos/listar.html"
	model = Productos
	context_object_name='productos'
	reverse_lazy="sistema"
	def get_context_data(self, **kwargs):
		ctx = super(listarProducto, self).get_context_data(**kwargs)
		ctx['categorias'] = Categoria.objects.all()
		return ctx


class filtrarAjaxProducto(TemplateView):
	def get(self,request,*args,**kwargs):
		nombreProducto = request.GET.get('nombre')
		cliente = Productos.objects.filter(pro_nombre__contains =nombreProducto)
		data = serializers.serialize('json',cliente,fields=('id','pro_nombre','pro_cantidad','pro_precio','pro_ecg','pro_tarifa_iva','pro_ex','pro_pvp','mar_id'))
		return HttpResponse(data,content_type='application/json')
