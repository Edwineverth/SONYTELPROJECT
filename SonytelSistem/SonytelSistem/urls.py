from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('apps.sistema.urls')),
    url(r'^cliente/',include('apps.sistema.urls')),
    url(r'^articulos/',include('apps.articulos.urls')),
    url(r'^modelo/',include('apps.modelo.urls')),
    url(r'^ciudad/',include('apps.ciudad.urls')),
    url(r'^proveedor/',include('apps.proveedor.urls')),
    url(r'^categoria/',include('apps.categoria.urls')),
    url(r'^factura/',include('apps.factura.urls')),
    url(r'^mensajeria/',include('apps.mensajeria.urls')),
    url(r'^facturadetalle/',include('apps.facturadetallle.urls')),
    url(r'^solicitudmantenimiento/',include('apps.solicitudmantenimiento.urls')),
    url(r'^mantenimiento/',include('apps.mantenimiento.urls')),



)
