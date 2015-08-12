from django.shortcuts import render
from apps.sistema.models import Facturadetalle,Factura
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	
from django.db.models import Q

# Create your views here.

class crearFacturadetalle(CreateView):
	template_name='detalleFactura/crear.html'
	model=Facturadetalle
	success_url=reverse_lazy('home')

#LISTAR ARTICULOS
class listarFacturadetalle(ListView):
	template_name='detalleFactura/editar.html'
	context_object_name='facturadetalle'
	model=Facturadetalle
#ACTUALIZAR ARTICULOS
class editarFacturadetalle(UpdateView):
	model = Facturadetalle
	template_name= 'detalleFactura/editar.html'
	success_url=reverse_lazy('home')
#ELIMINAR ARTICULOS
class eliminarFacturadetalle(DeleteView):
	model = Facturadetalle
	context_object_name="facturadetalle"
	template_name = 'detalleFactura/eliminar.html'
	success_url = reverse_lazy('home')

#FILTRADO DE Facturadetalle *****
class filtrarFacturadetalle(TemplateView):
	template_name='detalleFactura/filtrar.html'


#RETORNO AJAX FILTRADO *****
class filtrarAjaxFacturadetalle(TemplateView):
	def get(self,request,*args,**kwargs):
		nombreFacturadetalle = request.GET.get('nombre')
		Facturadetalle = Facturadetalle.objects.filter(Q(men_asunto__contains=nombreMensajeria)| Q(men_descripcion__contains=nombreMensajeria))
		data = serializers.serialize('json',mensajeria,fields=('men_asunto','men_descripcion','cli'))
		return HttpResponse(data,content_type='application/json')