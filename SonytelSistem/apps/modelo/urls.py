from django.conf.urls import patterns, include, url
from .views import crearModelo,editarModelo,eliminarModelo
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', index.as_view(),name='home'),
    #********************CLIENTE*********************************************
    url(r'^registrar/$', crearModelo.as_view(),name='crearModelo'),
    url(r'^editar/(?P<pk>[\d]+)$', editarModelo.as_view(),name='editarModelo'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarModelo.as_view(),name='eliminarModelo'),

    #*********************PROVEEDOR***************************************
    
    
)
