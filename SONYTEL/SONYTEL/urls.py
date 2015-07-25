from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from aplicacion.views import cliente,ClientesListView,editar_perfil,ClienteDetailView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SONYTEL.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',TemplateView.as_view(template_name='base.html'),name='home'),
    url(r'^QuienesSomos/',TemplateView.as_view(template_name='inicio.html'),name='quienessomos'),
    url(r'^Servicios/',TemplateView.as_view(template_name='inicio.html'),name='sercios'),
    url(r'^Contactos/',TemplateView.as_view(template_name='inicio.html'),name='contactos'),
    url(r'^Clientes/',TemplateView.as_view(template_name='clientes.html'),name='clientes'),
    url(r'^ClientesN/','aplicacion.views.cliente',name='cclientes'),
    url(r'^ClientesAdd/','aplicacion.views.clientesadd',name='addclientes'),
    #url(r'^editarPerfil/','aplicacion.views.editar_perfil',name='editarperfil'),

    url(r'^Clienteslista/$',ClientesListView.as_view(),name='clientesl'),
    url(r'^Cliente/(?P<pk>[\d]+)$',ClienteDetailView.as_view(),name='clientee'),


)
