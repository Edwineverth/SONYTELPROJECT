from django.conf.urls import patterns, include, url
from .views import crearCuidad,editarCiudad,eliminarCiudad
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', index.as_view(),name='home'),
    #********************CLIENTE*********************************************
    url(r'^registrar/$', crearCuidad.as_view(),name='crearCiudad'),
    url(r'^editar/(?P<pk>[\d]+)$', editarCiudad.as_view(),name='editarCiudad'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarCiudad.as_view(),name='eliminarCiudad'),

    #*********************PROVEEDOR***************************************
    
    
)
