from django.conf.urls import patterns, include, url
from .views import index,registrarCliente,reporteCliente,listarCliente
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index.as_view(),name='home'),
    url(r'^registrar/$', registrarCliente.as_view(),name='registrar_cliente'),
    url(r'^reporte/$', reporteCliente.as_view(),name='reporte_cliente'),
    url(r'^listado/$', listarCliente.as_view(),name='listar_cliente'),
    
)
