from django.conf.urls import patterns, include, url
from .views import index,registrarFactura,editarFactura,eliminarFactura,filtrarAjaxFactura,filtrarFactura,listarFactura
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', index.as_view(),name='home'),
    url(r'^registrar/$', registrarFactura.as_view(),name='registrar_Factura'),
    url(r'^listado/$', listarFactura.as_view(),name='listar_Factura'),
    url(r'^filtrar/$', filtrarFactura.as_view(),name='buscar_Factura'),
    url(r'^filtrador/$', filtrarAjaxFactura.as_view(),name='filtrador_Factura'),
    url(r'^editar/(?P<pk>[\d]+)$', editarFactura.as_view(),name='editar_Factura'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarFactura.as_view(),name='eliminar_Factura'),
    
)
