from django.conf.urls import patterns, include, url
from .views import index,registrarCliente,reporteCliente,listarCliente,buscarCliente,buscadorAjaxCliente,busqueda,editar,eliminar
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index.as_view(),name='home'),
    url(r'^registrar/$', registrarCliente.as_view(),name='registrar_cliente'),
    url(r'^reporte/$', reporteCliente.as_view(),name='reporte_cliente'),
    url(r'^listado/$', listarCliente.as_view(),name='listar_cliente'),
    url(r'^buscar/$', buscarCliente.as_view(),name='buscar_cliente'),
    url(r'^buscador/$', buscadorAjaxCliente.as_view(),name='buscar_clienteajax'),
    url(r'^busqueda/$', busqueda.as_view(),name='busqueda'),
    url(r'^editar/(?P<pk>[\d]+)$', editar.as_view(),name='editar'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminar.as_view(),name='eliminar'),
    
)
