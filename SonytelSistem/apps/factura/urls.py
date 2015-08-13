from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^crear/$', generarVentaFactura,name='crearFactura'),
    url(r'^crear/$', guardarFactura,name='crearFactura'),
   
    
)
