from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.shortcuts import render, redirect, render_to_response, RequestContext, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import time
# Create your views here.

def inicio(request):
    return render_to_response("index.html", context_instance=RequestContext(request))


@login_required(login_url='/')
def bienvenidoUser(request):
    us=User.objects.get(username=request.user)
    usi=Usuario.objects.get(usuarioDJ=us)
    if usi.Cargo == "Usuario":
        return render_to_response('baseUsuarios.html',{'usuario':usi},context_instance=RequestContext(request))
    else:
        message=str(time.strftime("20%y-%m-%d"))
        return render_to_response('base.html',{'usuario':usi,'cxc':Cuentas_Cobrar.objects.filter(Fecha_Vencimiento=message).count(),'cxp':Cuentas_Pagar.objects.filter(Fecha_Vencimiento=message).count()},context_instance=RequestContext(request))


@login_required(login_url='/')
def bienvenido(request):
    message=str(time.strftime("20%y-%m-%d"))
    us=User.objects.get(username=request.user)
    usi=Usuario.objects.get(usuarioDJ=us)
    if usi.Cargo == "Administrador":
        return render_to_response('base.html',{'usuario':usi,'cxc':Cuentas_Cobrar.objects.filter(Fecha_Vencimiento=message).count(),'cxp':Cuentas_Pagar.objects.filter(Fecha_Vencimiento=message).count()},context_instance=RequestContext(request))
    else:
        return render_to_response('baseUsuarios.html',{'usuario':usi},context_instance=RequestContext(request))

################################################--- Clientes ---##################################################################################################################################################################################################################

@login_required(login_url='/')
def clientes(request):
    if request.POST:
        cli = Clientes(Cedula=request.POST['cedula'], Nombre=request.POST['nombre'],
                      Apellido=request.POST['apellido'],
                      Direccion=request.POST['direccion'],
                      Ciudad=request.POST['ciudad'],
                      Telefono=request.POST['tlfono'],
                      Estado="Activo",
                      Sexo=request.POST['sexo'],
                      Correo_Electronico =request.POST['correo'])
        cli.save()
        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id), 'msj': "LOS DATOS SE HAN GUARDADO CORRECTAMENTE"}
        return render_to_response('clientes.html', cntx,context_instance = RequestContext(request))
    else:
        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id)}
        return render_to_response('clientes.html', cntx,context_instance=RequestContext(request))


@login_required(login_url='/')
def listaClientes(request):
    template_name = 'listaClientes.html'
    if request.POST:
        cli = Clientes(Cedula=request.POST['cedula'], Nombre=request.POST['nombre'],
                      Apellido=request.POST['apellido'],
                      Direccion=request.POST['direccion'],
                      Ciudad=request.POST['ciudad'],
                      Telefono=request.POST['tlfono'],
                      Estado="Activo",
                      Sexo=request.POST['sexo'],
                      Correo_Electronico =request.POST['correo'])
        cli.save()

        clientes = Clientes.objects.filter(Estado="Activo").order_by('Apellido')
        paginator = Paginator(clientes,5)

        try: pagina = int (request.GET.get("page",'1'))
        except ValueError: pagina = 1

        try:
            clientes = paginator.page(pagina)
        except (InvalidPage,EmptyPage):
            clientes = paginator.page(paginator._num_pages)

        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'lista':clientes}

        return render_to_response(template_name,cntx,context_instance = RequestContext(request))

    else:
        clientes = Clientes.objects.filter(Estado="Activo").order_by('Apellido')
        paginator = Paginator(clientes,5)

        try: pagina = int (request.GET.get("page",'1'))
        except ValueError: pagina = 1

        try:
            clientes = paginator.page(pagina)
        except (InvalidPage,EmptyPage):
            clientes = paginator.page(paginator._num_pages)

        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'lista':clientes}

        return render_to_response(template_name,cntx,context_instance = RequestContext(request))

@login_required(login_url='/')
def buscarClientes(request):
    if request.POST:
        cli=Clientes.objects.filter(Cedula__contains=request.POST['buscar']) | \
            Clientes.objects.filter(Nombre__contains= request.POST['buscar']) | \
            Clientes.objects.filter(Apellido__contains = request.POST['buscar']) | \
            Clientes.objects.filter(Direccion__contains = request.POST['buscar']) | \
            Clientes.objects.filter(Ciudad__contains = request.POST['buscar']) | \
            Clientes.objects.filter(Telefono__contains = request.POST['buscar']) | \
            Clientes.objects.filter(Sexo__contains = request.POST['buscar']) | \
            Clientes.objects.filter(Correo_Electronico__contains = request.POST['buscar'])
        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'lista':cli}
        return render(request,'listaClientes.html',cntx)
    else:
        return redirect('/listaClientes')

@login_required(login_url='/')
def eliminarCliente(request):
    if request.POST:
        cli=Clientes.objects.get(Cedula=request.POST['eliminarCli'])
        cliente=Clientes(
            Cedula=cli.Cedula,
            Nombre=cli.Nombre,
            Apellido=cli.Apellido,
            Direccion=cli.Direccion,
            Ciudad=cli.Ciudad,
            Telefono=cli.Telefono,
            Estado="Desactivo",
            Sexo=cli.Sexo,
            Correo_Electronico =cli.Correo_Electronico
        )
        cliente.save()
        return redirect('/listaClientes')


#######################################--- PRODUCTOS ---#################################################################################

@login_required(login_url='/')
def productos(request):
    template_name = "productos.html"

    if request.POST:
        cat=Categorias.objects.get(id=request.POST['categoriaID'])
        prod=Productos(
            Codigo = request.POST['codigo'],
            Nombre = request.POST['nombre'],
            Cantidad = request.POST['cantidad'],
            Precio_Venta = request.POST['PVenta'],
            Estado="Activo",
            categoria=cat
        )
        prod.save()

        productos = Productos.objects.order_by('Codigo').filter(Estado="Activo")
        paginator = Paginator(productos,5)

        try: pagina = int (request.GET.get("page",'1'))
        except ValueError: pagina = 1

        try:
            productos = paginator.page(pagina)
        except (InvalidPage,EmptyPage):
            productos = paginator.page(paginator._num_pages)

        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'productos':productos, 'nProd':Productos.objects.count()+1,'categorias':Categorias.objects.all()}

        return render_to_response(template_name,cntx,context_instance = RequestContext(request))
    else:
        productos = Productos.objects.order_by('Codigo').filter(Estado="Activo")
        paginator = Paginator(productos,5)

        try: pagina = int (request.GET.get("page",'1'))
        except ValueError: pagina = 1

        try:
            productos = paginator.page(pagina)
        except (InvalidPage,EmptyPage):
            productos = paginator.page(paginator._num_pages)
        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'productos':productos, 'nProd':Productos.objects.count()+1,'categorias':Categorias.objects.all()}

        return render_to_response(template_name,cntx,context_instance = RequestContext(request))


@login_required(login_url='/')
def eliminarProd(request):
    if request.POST:
        prod=Productos.objects.get(Codigo=request.POST['codigoElim'])
        produ=Productos(
            Codigo = prod.Codigo,
            Nombre = prod.Nombre,
            Cantidad = prod.Cantidad,
            Precio_Venta = prod.Precio_Venta,
            Estado="Desactivo",
            categoria=prod.categoria
        )
        produ.save()
        return redirect('/productos')

@login_required(login_url='/')
def buscarProd(request):
    if request.POST:
        if request.POST['buscar'] !="":
            prod=Productos.objects.filter(Codigo__contains=request.POST['buscar']) | \
                 Productos.objects.filter(Nombre__contains=request.POST['buscar'])

            us=User.objects.get(username=request.user)
            cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'productos':prod}
            return render(request,'productos.html', cntx)
        else:
            return redirect('/productos')

@login_required(login_url='/')
def agregarProd(request):
    if request.POST:
        cat=Categorias.objects.get(id=request.POST['info'])
        prod=Productos(
            Codigo = request.POST['codigo'],
            Nombre = request.POST['nombre'],
            Cantidad = request.POST['cantidad'],
            Precio_Venta = request.POST['PVenta'],
            Estado="Activo",
            categoria=cat
        )
        prod.save()
    return redirect("/productos")

#######################################--- USUARIO ---################################################################################

@login_required(login_url='/')
def registrar_usuario(request):
    message = ""

    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            cedula=request.POST['cedula']
            nombre=request.POST['nombre']
            apellido=request.POST['apellido']
            direccion=request.POST['direccion']
            cargo=request.POST['info']
            ciudad=request.POST['ciudad']
            telefono=request.POST['tlfono']
            sexo=request.POST['sexo']

            if not Usuario.objects.filter(pk=cedula).exists():
                password =request.POST['password1']
                confirmPassword=request.POST['password2']
                if password != confirmPassword:
                    message="Las contrasenias no coinciden"
                else:
                    #pU =User (username=correoFor, password=passwordFor, is_superuser=False, email='', first_name=nombresfor,last_name=apellidosFor, is_staff=True, is_active=True, date_joined=timezone.now(), last_login=timezone.now())
                    fornaea=form.save()
                    usua = Usuario(Cedula=cedula,
                                  Nombre=nombre,
                                  Apellido=apellido,
                                  Direccion=direccion,
                                  Cargo=cargo,
                                  Ciudad=ciudad,
                                  Telefono=telefono,
                                  Sexo=sexo,
                                  Estado="Activo",
                                  usuarioDJ=fornaea
                    )
                    message="Usuario Registrado Correctamente"
                    usua.save()
                    form=UserCreationForm
            else:
                message="El Usuario ya posee una Cuenta"
        else:
            message="Error al Registrarse"
    else:
        form=UserCreationForm

    us=User.objects.get(username=request.user)
    cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'msj':message, 'form':form}

    return render_to_response('usuarios.html',cntx ,context_instance=RequestContext(request))

@login_required(login_url='/')
def listaUsuarios(request):
    template_name = 'listaUsuarios.html'
    if request.POST:
        dj=User.objects.get(id=request.POST['dj'])
        usua = Usuario(Cedula=request.POST['cedula'],
                      Nombre=request.POST['nombre'],
                      Apellido=request.POST['apellido'],
                      Direccion=request.POST['direccion'],
                      Cargo=request.POST['info'],
                      Ciudad=request.POST['ciudad'],
                      Telefono=request.POST['telefono'],
                                  Estado="Activo",
                      Sexo=request.POST['sexo'],
                      usuarioDJ=dj
                      )
        usua.save()
        usuario = Usuario.objects.all().filter(Estado="Activo")
        paginator =  Paginator(usuario,5)
        try: pagina = int (request.GET.get("page",'1'))
        except ValueError: pagina=1
        try:
            usuario = paginator.page(pagina)
        except (InvalidPage, EmptyPage):
            usuario= paginator.page(paginator._num_pages)

        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'entrada':usuario}
        return render_to_response(template_name,cntx,context_instance=RequestContext(request))
    else:
        usuario = Usuario.objects.all().filter(Estado="Activo")
        paginator = Paginator(usuario,5)
        try: pagina = int (request.GET.get("page",'1'))
        except ValueError: pagina = 1
        try:
            usuario = paginator.page(pagina)
        except (InvalidPage,EmptyPage):
            usuario = paginator.page(paginator._num_pages)
        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'entrada':usuario}
        return render_to_response(template_name,cntx,context_instance=RequestContext(request))

@login_required(login_url='/')
def eliminarUsuario(request):
    if request.POST:
        usu= Usuario.objects.get(Cedula=request.POST['eliminarCed'])
        user=User.objects.get(id=usu.usuarioDJ.id)
        usua = Usuario(Cedula=usu.Cedula,
                      Nombre=usu.Nombre,
                      Apellido=usu.Apellido,
                      Direccion=usu.Direccion,
                      Cargo=usu.Cargo,
                      Ciudad=usu.Ciudad,
                      Telefono=usu.Telefono,
                                  Estado="Desactivo",
                      Sexo=usu.Sexo,
                      usuarioDJ=usu.usuarioDJ
                      )
        usua.save()

        user=User(
            id=user.id,
            password=user.password,
            last_login=user.last_login,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            is_staff=user.is_staff,
            is_active=False,
            date_joined=user.date_joined
        )
        user.save()
        return redirect('/listaUsuarios')

@login_required(login_url='/')
def buscarUsuarios(request):
    if request.POST:
        usu=Usuario.objects.filter(Cedula__contains=request.POST['buscar']) | \
            Usuario.objects.filter(Nombre__contains= request.POST['buscar']) | \
            Usuario.objects.filter(Apellido__contains = request.POST['buscar']) | \
            Usuario.objects.filter(Direccion__contains = request.POST['buscar']) | \
            Usuario.objects.filter(Cargo__contains = request.POST['buscar']) | \
            Usuario.objects.filter(Ciudad__contains = request.POST['buscar']) | \
            Usuario.objects.filter(Telefono__contains = request.POST['buscar']) | \
            Usuario.objects.filter(Sexo__contains = request.POST['buscar'])
        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'entrada':usu}
        return render(request,'listaUsuarios.html',cntx)
    else:
        return redirect('/listaUsuarios')

##################################################################--- PEDIDOS ---######################################################################################################################

@login_required(login_url='/')
def geneFCompra(request):
    us=User.objects.get(username=request.user)
    cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'listaProveedores':Proveedores.objects.filter(Estado="Activo"), 'listaProductos':Productos.objects.all(),'nPedido':Pedidos.objects.count()+1,'categorias':Categorias.objects.all()}
    return render_to_response('fCompra.html', cntx, context_instance=RequestContext(request))

@login_required(login_url='/')
def guardarPedido(request):

    prod=request.GET['codigo']
    cant=request.GET['cantidad']
    precio=request.GET['precio']
    ruc=request.GET['ruc']

    idruc = Proveedores.objects.get(RUC=ruc)
    pd=Productos.objects.get(Codigo=prod)

    f=Pedidos.objects.filter(Numero=request.GET['nPedido']).count()

    if f== 0:
        pedi = Pedidos(
            Numero = request.GET['nPedido'],
            Estado = request.GET['estado'],
            Fecha_Emision = request.GET['fecha'],
            Total = request.GET['total'],
            RUC = idruc
        )
        pedi.save()

    detalle=Detalle_Pedido(
            Codigo_Producto = pd,
            Pedido_id = request.GET['nPedido'],
            Cantidad = cant,
            Precio_Untario = precio
    )
    detalle.save()

    nuevaCantidad= pd.Cantidad + int(cant)

    produc= Productos(
        Codigo = pd.Codigo,
        Nombre = pd.Nombre,
        Cantidad = nuevaCantidad,
        Estado="Activo",
        Precio_Venta = precio,
        categoria=pd.categoria
    )
    produc.save()

    if request.GET['estado']=='Emitida' and request.GET['i']=='1':
        numero = Cuentas_Pagar.objects.count()+1
        cancelado=request.GET['cancelado']
        saldo=float(request.GET['total'])-float(cancelado)
        cxp=Cuentas_Pagar(
            Numero = numero,
            Concepto = "Pedido #"+request.GET['nPedido'],
            Valor_Total = request.GET['total'],
            Valor_Saldo = saldo,
            Valor_Cancelado = cancelado,
            Estado = "Abierto",
            Fecha_Inicio = request.GET['fecha'],
            Fecha_Vencimiento = request.GET['fecha'],
            Pedidos_id = request.GET['nPedido']
        )
        cxp.save()

    return render_to_response('fCompra.html', context_instance=RequestContext(request))

#cuentas por pagar vistas
##################################---- Cuentas por Pagar ---######################################################################################################################################################

@login_required(login_url='/')
def ccxpp(request):
    cxp=Cuentas_Pagar.objects.all().order_by('Numero')
    paginator =  Paginator(cxp,5)
    try: pagina = int (request.GET.get("page",'1'))
    except ValueError: pagina=1
    try:
        cxp = paginator.page(pagina)
    except (InvalidPage, EmptyPage):
        cxp= paginator.page(paginator._num_pages)

    us=User.objects.get(username=request.user)
    cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'entrada':cxp}
    return render_to_response('ccxpp.html',cntx,context_instance=RequestContext(request))

@login_required(login_url='/')
def buscarccxpp(request):
    cxp=Cuentas_Pagar.objects.filter(Estado__contains=request.POST['buscar'])
    us=User.objects.get(username=request.user)
    cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'entrada':cxp}
    return render_to_response('ccxpp.html',cntx, context_instance=RequestContext(request))


@login_required(login_url='/')
def Edit_CCxPP(request,n):
    cat=Cuentas_Pagar.objects.get(Numero=n)
    factura = cat.Pedidos
    pro=Proveedores.objects.get(RUC=factura.RUC.RUC)
    if request.POST:
        saldo=float(request.POST['saldo'])-float(request.POST['valor'])
        comprobante=Comprobantes_Cuenta_Pagar(
            Numero = request.POST['numero'],
            Valor_Cancelar = request.POST['valor'],
            Concepto = request.POST['concepto'],
            Saldo = saldo,
            CCxPP = cat
        )
        comprobante.save()
        estado="Parcial"
        if saldo==0:
            estado="Cancelada"
            p=Pedidos(
                Numero = factura.Numero,
                Estado = estado,
                Fecha_Emision = factura.Fecha_Emision,
                Total = factura.Total,
                RUC = factura.RUC,
            )
            p.save()

        cta=Cuentas_Pagar(
            Numero = cat.Numero,
            Concepto = request.POST['concepto'],
            Valor_Total = cat.Valor_Total,
            Valor_Saldo = float(request.POST['saldo'])-float(request.POST['valor']),
            Valor_Cancelado = float(cat.Valor_Cancelado)+float(request.POST['valor']),
            Estado = estado,
            Fecha_Inicio = cat.Fecha_Inicio,
            Fecha_Vencimiento = cat.Fecha_Vencimiento,
            Pedidos = factura
        )
        cta.save()
        comp=Comprobantes_Cuenta_Pagar.objects.filter(CCxPP=cat)

        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),"datos":cta, "proveedor":pro,"comprobantes":comp, "num": Comprobantes_Cuenta_Pagar.objects.count()+1}

        return render_to_response("editCCxPP.html",cntx, context_instance=RequestContext(request))
    else:
        try:
            comprobante=Comprobantes_Cuenta_Pagar.objects.filter(CCxPP=cat)
            us=User.objects.get(username=request.user)
            cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),"datos":cat, "proveedor":pro,"comprobantes":comprobante, "num": Comprobantes_Cuenta_Pagar.objects.count()+1}
            return render_to_response("editCCxPP.html",cntx, context_instance=RequestContext(request))
        except Exception as error:
            us=User.objects.get(username=request.user)
            cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),"datos":cat, "proveedor":pro,"num": Comprobantes_Cuenta_Pagar.objects.count()+1}
            return render_to_response("editCCxPP.html",cntx, context_instance=RequestContext(request))


###################################################--- FACTURA ----############################################################################################################################

@login_required(login_url='/')
def geneFVenta(request):
    us=User.objects.get(username=request.user)
    cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'listaClientes':Clientes.objects.filter(Estado="Activo"), 'listaProductos':Productos.objects.all(), 'nFactura': 1+Factura_Venta.objects.count()}
    return render_to_response('fVenta.html', cntx, context_instance=RequestContext(request))

@login_required(login_url='/')
def guardarFVenta(request):
    prod=request.GET['codigo']
    cant=request.GET['cantidad']
    precio=request.GET['precio']
    ci=request.GET['ci']

    us=User.objects.get(username=request.user)
    usua=Usuario.objects.get(usuarioDJ_id=us.id)

    ced=Clientes.objects.get(Cedula=ci)
    pd=Productos.objects.get(Codigo=prod)

    f=Factura_Venta.objects.filter(Numero=request.GET['nFact']).count()
    print f

    if f == 0:
        fact=Factura_Venta(Numero = request.GET['nFact'],
                              Total = request.GET['total'],
                              Subtotal = request.GET['subtotal'],
                              Dscto = request.GET['dscto'],
                              IVA = request.GET['iva'],
                              Estado = request.GET['estado'],
                              Cedula = ced,
                              Usuario = usua
        )
        fact.save()


    detalle=Detalle_Factura_Venta(
            Producto = pd,
            Fact_Venta_id = request.GET['nFact'],
            Cantidad = cant,
            Precio_Venta = precio
        )
    detalle.save()

    nuevaCantidad= pd.Cantidad - int(cant)


    produc= Productos(
        Codigo = pd.Codigo,
        Nombre = pd.Nombre,
        Cantidad = nuevaCantidad,
        Estado="Activo",
        Precio_Venta = precio,
        categoria=pd.categoria
    )
    produc.save()

    if request.GET['estado']=='Emitida' and request.GET['i']=='1':
        print "ntro"
        numero = Cuentas_Cobrar.objects.count()+1
        cancelado=request.GET['cancelado']
        saldo=float(request.GET['total'])-float(cancelado)
        cxc=Cuentas_Cobrar(
            Numero = numero,
            Concepto = "Venta de Factura #"+request.GET['nFact'],
            Valor_Total = request.GET['total'],
            Valor_Saldo = saldo,
            Valor_Cancelado = cancelado,
            Estado = "Abierto",
            Fecha_Inicio = request.GET['fecha'],
            Fecha_Vencimiento = request.GET['fecha'],
            Fact_Venta_id = request.GET['nFact']
        )
        cxc.save()

    return render_to_response('fVenta.html', context_instance=RequestContext(request))

####################################################--- CUENTAS POR COBRAR -----####################################################################################################################################

@login_required(login_url='/')
def ccxcc(request):
    cxc=Cuentas_Cobrar.objects.all().order_by('Numero')
    paginator =  Paginator(cxc,5)
    try: pagina = int (request.GET.get("page",'1'))
    except ValueError: pagina=1
    try:
        cxc = paginator.page(pagina)
    except (InvalidPage, EmptyPage):
        cxc= paginator.page(paginator._num_pages)

    us=User.objects.get(username=request.user)
    cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'entrada':cxc}

    return render_to_response('ccxcc.html',cntx, context_instance=RequestContext(request))

@login_required(login_url='/')
def buscarccxcc(request):
    cxc=Cuentas_Cobrar.objects.filter(Estado__contains=request.POST['buscar'])
    us=User.objects.get(username=request.user)
    cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'entrada':cxc}
    return render_to_response('ccxcc.html',cntx, context_instance=RequestContext(request))

@login_required(login_url='/')
def Edit_CCxCC(request,n):
    cat=Cuentas_Cobrar.objects.get(Numero=n)
    factura = cat.Fact_Venta
    cli=Clientes.objects.get(Cedula=factura.Cedula.Cedula)
    if request.POST:
        saldo=float(request.POST['saldo'])-float(request.POST['valor'])
        comprobante=Comprobantes_Cuenta_Cobrar(
            Numero = request.POST['numero'],
            Valor_Cancelar = request.POST['valor'],
            Concepto = request.POST['concepto'],
            Saldo = saldo,
            CCxCC = cat
        )
        comprobante.save()
        estado="Parcial"
        if saldo==0:
            estado="Cancelada"
            f=Factura_Venta(
                Numero = factura.Numero,
                Fecha_Emision = factura.Fecha_Emision,
                Total = factura.Total,
                Subtotal = factura.Subtotal,
                Dscto = factura.Dscto,
                IVA = factura.IVA,
                Estado = estado,
                Cedula = factura.Cedula,
                Usuario = factura.Usuario
            )
            f.save()

        cta=Cuentas_Cobrar(
            Numero = cat.Numero,
            Concepto = request.POST['concepto'],
            Valor_Total = cat.Valor_Total,
            Valor_Saldo = float(request.POST['saldo'])-float(request.POST['valor']),
            Valor_Cancelado = float(cat.Valor_Cancelado)+float(request.POST['valor']),
            Estado = estado,
            Fecha_Inicio = cat.Fecha_Inicio,
            Fecha_Vencimiento = cat.Fecha_Vencimiento,
            Fact_Venta = factura
        )
        cta.save()
        comp=Comprobantes_Cuenta_Cobrar.objects.filter(CCxCC=cat)

        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),"datos":cta, "cliente":cli,"comprobantes":comp, "num": Comprobantes_Cuenta_Cobrar.objects.count()+1}

        return render_to_response("editCCxCC.html",cntx, context_instance=RequestContext(request))
    else:
        try:
            comprobante=Comprobantes_Cuenta_Cobrar.objects.filter(CCxCC=cat)
            us=User.objects.get(username=request.user)
            cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),"datos":cat, "cliente":cli,"comprobantes":comprobante, "num": Comprobantes_Cuenta_Cobrar.objects.count()+1}
            return render_to_response("editCCxCC.html",cntx, context_instance=RequestContext(request))
        except Exception as error:
            us=User.objects.get(username=request.user)
            cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),"datos":cat, "cliente":cli,"num": Comprobantes_Cuenta_Cobrar.objects.count()+1}
            return render_to_response("editCCxCC.html",cntx, context_instance=RequestContext(request))


###############################################--- PROVEEDORES ----#########################################################################################################################################

@login_required(login_url='/')
def proveedores(request):
    template_name = 'proveedores.html'

    if request.POST:
        pro = Proveedores(RUC=request.POST['RUC'],
                          Razon_Social = request.POST['Razon_Social'],
                          Direccion = request.POST['direccion'],
                          Ciudad = request.POST['ciudad'],
                          Estado="Activo",
                          Telefono = request.POST['telefono'],
                          Correo_Electronico = request.POST['Correo_electronico'])
        pro.save()
        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'msj':"LOS DATOS DEL PROVEEDOR SE HAN GUARDADO CORRECTAMENTE"}
        return render_to_response(template_name,cntx,context_instance=RequestContext(request))
    else:
        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id)}
        return render_to_response(template_name,cntx,context_instance=RequestContext(request))

@login_required(login_url='/')
def listaProveedores(request):
    template_name = "listaProveedores.html"

    if request.POST:
        pro = Proveedores(RUC=request.POST['RUC'],
                          Razon_Social = request.POST['Razon_Social'],
                          Direccion = request.POST['direccion'],
                          Ciudad = request.POST['ciudad'],
                          Telefono = request.POST['telefono'],
                          Estado="Activo",
                          Correo_Electronico = request.POST['Correo_electronico'])
        pro.save()
        proveedor = Proveedores.objects.all().filter(Estado='Activo')
        paginator =  Paginator(proveedor,5)
        try: pagina = int (request.GET.get("page",'1'))
        except ValueError: pagina=1
        try:
            proveedor = paginator.page(pagina)
        except (InvalidPage, EmptyPage):
            proveedor= paginator.page(paginator._num_pages)
        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'entrada':proveedor}
        return render_to_response(template_name,cntx,context_instance=RequestContext(request))

    else:
        proveedor = Proveedores.objects.all().filter(Estado='Activo')
        paginator =  Paginator(proveedor,5)
        try: pagina = int (request.GET.get("page",'1'))
        except ValueError: pagina=1
        try:
            proveedor = paginator.page(pagina)
        except (InvalidPage, EmptyPage):
            proveedor= paginator.page(paginator._num_pages)

        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'entrada':proveedor}

        return render_to_response(template_name,cntx,context_instance=RequestContext(request))


@login_required(login_url='/')
def eliminarProveedor(request):
    if request.POST:
        pro= Proveedores.objects.get(RUC=request.POST['eliminarRUC'])
        prod = Proveedores(RUC=pro.RUC,
                          Razon_Social = pro.Razon_Social,
                          Direccion = pro.Direccion,
                          Ciudad = pro.Ciudad,
                          Telefono = pro.Telefono,
                          Estado="Desactivo",
                          Correo_Electronico = pro.Correo_Electronico)
        prod.save()
        return redirect('/listaProveedores')

@login_required(login_url='/')
def buscarProveedores(request):
    if request.POST:
        pro = Proveedores.objects.filter(RUC__contains=request.POST['buscar']) | \
                Proveedores.objects.filter(Razon_Social__contains=request.POST['buscar']) | \
                Proveedores.objects.filter(Direccion__contains=request.POST['buscar']) | \
                Proveedores.objects.filter(Ciudad__contains=request.POST['buscar']) | \
                Proveedores.objects.filter(Telefono__contains=request.POST['buscar']) | \
                Proveedores.objects.filter(Direccion__contains=request.POST['buscar']) | \
                Proveedores.objects.filter(Correo_Electronico__contains=request.POST['buscar'])
        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'entrada':pro}
        return render(request,"listaProveedores.html",cntx)
    else:
        return redirect('/listaProveedores')


########################################---- Listar ----############################################################################

@login_required(login_url='/')
def listaFactVenta(request):
    template_name = 'listaFactVenta.html'
    if request.POST:
        FVenta = Factura_Venta.objects.all()
        paginator = Paginator(FVenta,5)

        try: pagina = int (request.GET.get("page",'1'))
        except ValueError: pagina = 1

        try:
            FVenta = paginator.page(pagina)
        except (InvalidPage,EmptyPage):
            FVenta = paginator.page(paginator._num_pages)

        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'lista':FVenta}

        return render_to_response(template_name,cntx,context_instance = RequestContext(request))
    else:
        FVenta = Factura_Venta.objects.all()
        paginator = Paginator(FVenta,5)

        try: pagina = int (request.GET.get("page",'1'))
        except ValueError: pagina = 1

        try:
            FVenta = paginator.page(pagina)
        except (InvalidPage,EmptyPage):
            FVenta = paginator.page(paginator._num_pages)

        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'lista':FVenta}

        return render_to_response(template_name,cntx,context_instance = RequestContext(request))

@login_required(login_url='/')
def buscarFacturaVenta(request):

    if request.POST:
        fact = Factura_Venta.objects.filter(Estado=request.POST['buscar'])
        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'lista':fact}

        return render(request,"listaFactVenta.html",cntx)
    else:
        return redirect('/listarFacturaVenta')


########################################################################################################################

@login_required(login_url='/')
def listaPedido(request):
    template_name = 'listaPedidos.html'
    if request.POST:
        listPedido = Pedidos.objects.all()
        paginator = Paginator(listPedido,5)

        try: pagina = int (request.GET.get("page",'1'))
        except ValueError: pagina = 1

        try:
            listPedido = paginator.page(pagina)
        except (InvalidPage,EmptyPage):
            listPedido = paginator.page(paginator._num_pages)

        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'lista':listPedido}
        return render_to_response(template_name,cntx,context_instance = RequestContext(request))

    else:
        listPedido = Pedidos.objects.all()
        paginator = Paginator(listPedido,5)

        try: pagina = int (request.GET.get("page",'1'))
        except ValueError: pagina = 1

        try:
            listPedido = paginator.page(pagina)
        except (InvalidPage,EmptyPage):
            listPedido = paginator.page(paginator._num_pages)

        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'lista':listPedido}
        return render_to_response(template_name,cntx,context_instance = RequestContext(request))

@login_required(login_url='/')
def buscarPedido(request):

    if request.POST:
        listPedido = Pedidos.objects.filter(Estado=request.POST['buscar'])

        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'lista': listPedido}
        return render(request,"listaPedidos.html",cntx)
    else:
        return redirect('/listarPedidos')

########################################################################################################################
@login_required(login_url='/')
def configuraciones(request):
    us=User.objects.get(username=request.user)
    cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id)}
    return render_to_response('conf/plantillaConf.html',cntx, context_instance = RequestContext(request))

@login_required(login_url='/')
def proveedoresDesactivos(request):
    if request.POST:
        proveedor=Proveedores.objects.get(RUC=request.POST['habilitarRUC'])
        p=Proveedores(RUC=proveedor.RUC,
                      Ciudad=proveedor.Ciudad,
                      Correo_Electronico=proveedor.Correo_Electronico,
                      Razon_Social=proveedor.Razon_Social,
                      Telefono=proveedor.Telefono,
                      Estado="Activo",
                      Direccion=proveedor.Direccion)
        p.save()

        prov = Proveedores.objects.all().filter(Estado="Desactivo")
        paginator =  Paginator(prov,5)
        try: pagina = int (request.GET.get("page",'1'))
        except ValueError: pagina=1
        try:
            prov = paginator.page(pagina)
        except (InvalidPage, EmptyPage):
            prov= paginator.page(paginator._num_pages)

        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'entrada':prov}
        return render_to_response('conf/habProveedores.html',cntx,context_instance=RequestContext(request))
    else:
        prov = Proveedores.objects.all().filter(Estado="Desactivo")
        paginator =  Paginator(prov,5)
        try: pagina = int (request.GET.get("page",'1'))
        except ValueError: pagina=1
        try:
            prov = paginator.page(pagina)
        except (InvalidPage, EmptyPage):
            prov= paginator.page(paginator._num_pages)

        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'entrada':prov}
        return render_to_response('conf/habProveedores.html',cntx,context_instance=RequestContext(request))

@login_required(login_url='/')
def productosDesactivos(request):
    if request.POST:
        productos=Productos.objects.get(Codigo=request.POST['habilitarProducto'])
        p=Productos(
            Codigo = productos.Codigo,
            Nombre = productos.Nombre,
            Cantidad = productos.Cantidad,
            Precio_Venta = productos.Precio_Venta,
            Estado="Activo",
            categoria=productos.categoria
        )
        p.save()

        prod = Productos.objects.all().filter(Estado="Desactivo")
        paginator =  Paginator(prod,5)
        try: pagina = int (request.GET.get("page",'1'))
        except ValueError: pagina=1
        try:
            prod = paginator.page(pagina)
        except (InvalidPage, EmptyPage):
            prod= paginator.page(paginator._num_pages)

        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'entrada':prod}
        return render_to_response('conf/habProductos.html',cntx,context_instance=RequestContext(request))
    else:
        prod = Productos.objects.all().filter(Estado="Desactivo")
        paginator =  Paginator(prod,5)
        try: pagina = int (request.GET.get("page",'1'))
        except ValueError: pagina=1
        try:
            prod = paginator.page(pagina)
        except (InvalidPage, EmptyPage):
            prod= paginator.page(paginator._num_pages)

        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'entrada':prod}
        return render_to_response('conf/habProductos.html',cntx,context_instance=RequestContext(request))

@login_required(login_url='/')
def clientesDesactivos(request):
    if request.POST:
        cliente=Clientes.objects.get(Cedula=request.POST['habilitar'])
        c=Clientes(Cedula=cliente.Cedula, Nombre=cliente.Nombre,
                      Apellido=cliente.Apellido,
                      Direccion=cliente.Direccion,
                      Ciudad=cliente.Ciudad,
                      Telefono=cliente.Telefono,
                      Estado="Activo",
                      Sexo=cliente.Sexo,
                      Correo_Electronico =cliente.Correo_Electronico)
        c.save()

        cliente = Clientes.objects.all().filter(Estado="Desactivo")
        paginator =  Paginator(cliente,5)
        try: pagina = int (request.GET.get("page",'1'))
        except ValueError: pagina=1
        try:
            cliente = paginator.page(pagina)
        except (InvalidPage, EmptyPage):
            cliente= paginator.page(paginator._num_pages)

        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'entrada':cliente}
        return render_to_response('conf/habClientes.html',cntx,context_instance=RequestContext(request))
    else:
        prod = Clientes.objects.all().filter(Estado="Desactivo")
        paginator =  Paginator(prod,5)
        try: pagina = int (request.GET.get("page",'1'))
        except ValueError: pagina=1
        try:
            cliente = paginator.page(pagina)
        except (InvalidPage, EmptyPage):
            cliente= paginator.page(paginator._num_pages)

        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'entrada':cliente}
        return render_to_response('conf/habClientes.html',cntx,context_instance=RequestContext(request))

@login_required(login_url='/')
def usuariosDesactivos(request):
    if request.POST:
        usu=Usuario.objects.get(Cedula=request.POST['habilitar'])
        usua = Usuario(Cedula=usu.Cedula,
                      Nombre=usu.Nombre,
                      Apellido=usu.Apellido,
                      Direccion=usu.Direccion,
                      Cargo=usu.Cargo,
                      Ciudad=usu.Ciudad,
                      Telefono=usu.Telefono,
                            Estado="Activo",
                      Sexo=usu.Sexo,
                      usuarioDJ=usu.usuarioDJ
                      )
        usua.save()

        user=User.objects.get(id=usua.usuarioDJ.id)
        user=User(
            id=user.id,
            password=user.password,
            last_login=user.last_login,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            is_staff=user.is_staff,
            is_active=True,
            date_joined=user.date_joined
        )
        user.save()

        usuario = Usuario.objects.all().filter(Estado="Desactivo")
        paginator =  Paginator(usuario,5)
        try: pagina = int (request.GET.get("page",'1'))
        except ValueError: pagina=1
        try:
            usuario = paginator.page(pagina)
        except (InvalidPage, EmptyPage):
            usuario= paginator.page(paginator._num_pages)

        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'entrada':usuario}
        return render_to_response('conf/habUsuarios.html',cntx,context_instance=RequestContext(request))
    else:
        usuario = Usuario.objects.all().filter(Estado="Desactivo")
        paginator =  Paginator(usuario,5)
        try: pagina = int (request.GET.get("page",'1'))
        except ValueError: pagina=1
        try:
            usuario = paginator.page(pagina)
        except (InvalidPage, EmptyPage):
            usuario= paginator.page(paginator._num_pages)

        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'entrada':usuario}
        return render_to_response('conf/habUsuarios.html',cntx,context_instance=RequestContext(request))

@login_required(login_url='/')
def reporteUsuarios(request):
    if request.POST:
        usu=Usuario.objects.get(Cedula=request.POST['buscar'])
        asist=Asistencia.objects.filter(Usuar=usu)
        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'entrada':asist}
        return render_to_response('conf/reporte.html',cntx, context_instance=RequestContext(request))
    else:
        asist=Asistencia.objects.all()
        us=User.objects.get(username=request.user)
        cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id),'entrada':asist}
        return render_to_response('conf/reporte.html',cntx, context_instance=RequestContext(request))


#############################################################################################################################################

def mision(request):
    return  render_to_response('mision.html',context_instance=RequestContext(request))

def vision(request):
    return  render_to_response('vision.html',context_instance=RequestContext(request))

def contacto(request):
    return  render_to_response('contacto.html',context_instance=RequestContext(request))

def acerca(request):
    us=User.objects.get(username=request.user)
    cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id)}
    return  render_to_response('acercaDe.html',cntx,context_instance=RequestContext(request))

def tutorial(request):
    us=User.objects.get(username=request.user)
    cntx={'usuario':Usuario.objects.get(usuarioDJ_id=us.id)}
    return render_to_response('conf/tutorial.html',cntx,context_instance=RequestContext(request))