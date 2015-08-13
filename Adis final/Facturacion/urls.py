from django.conf.urls import patterns, include, url
from .views import *
from Adis.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', inicio),
    url(r'^mision/', mision),
    url(r'^vision/', vision),
    url(r'^contacto/', contacto),
    url(r'^acerca/', acerca),
    url(r'^tutorial/', tutorial),

    url(r'^inicioUser/$', bienvenidoUser),
    url(r'^inicio/$', bienvenido),

    url(r'^clientes/$', clientes),
    url(r'^listaClientes/$', listaClientes),
    url(r'^buscarClientes/$',buscarClientes),
    url(r'^eliminarCliente/$',eliminarCliente),

    url(r'^productos/$', productos),
    url(r'^eliminarProductos/$', eliminarProd),
    url(r'^buscarProd/$', buscarProd),
    url(r'^agregarProductos/$', agregarProd),

    url(r'^generarFacturaVenta/$', geneFVenta),
    url(r'^guardarFacturaVenta/$', guardarFVenta),
    url(r'^listarFacturaVenta/$', listaFactVenta),
    url(r'^buscarFacVenta/$', buscarFacturaVenta),

    url(r'^generarFacturaCompra/$',geneFCompra),
    url(r'^generarPedido/$',guardarPedido),
    url(r'^listarPedidos/$', listaPedido),
    url(r'^buscarRegPedidos/$', buscarPedido),

    url(r'^ctpPagar/$', ccxpp),
    url(r'^elemento/(\d+)/$',Edit_CCxPP),
    url(r'^buscarcxp/$', buscarccxpp),

    url(r'^ctaxcobrar/$', ccxcc),
    url(r'^datos/(\d+)/$',Edit_CCxCC),
    url(r'^buscarcxc/$', buscarccxcc),

    url(r'^iniciar/$', login_page),
    url(r'^cerrar/$', cerrar),

    url(r'^usuarios/$', registrar_usuario),
    url(r'^registroUsuarios/$',registrar_usuario),
    url(r'^listaUsuarios/$',listaUsuarios),
    url(r'^eliminarUsuario/$',eliminarUsuario),
    url(r'^buscarUsuarios/$',buscarUsuarios),

    url(r'^proveedores/$', proveedores),
    url(r'^listaProveedores/$',listaProveedores),
    url(r'^eliminarProveedor/$',eliminarProveedor),
    url(r'^buscarProveedores/$',buscarProveedores),

    url(r'^configuracion/$', configuraciones),

    url(r'^confProveedores/$', proveedoresDesactivos),
    url(r'^confProductos/$', productosDesactivos),
    url(r'^confClientes/$', clientesDesactivos),
    url(r'^confUsuarios/$', usuariosDesactivos),
    url(r'^reporte/$', reporteUsuarios)
)
