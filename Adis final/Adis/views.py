
from django.template import RequestContext
from django.shortcuts import  render_to_response, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from Facturacion.models import *
import time
from django.contrib.auth.decorators import login_required

def login_page(request):
    message = ""
    if request.user.is_authenticated():
        usuarioLogeado=request.user.id
        usuarioLogeadoTabla2=Usuario.objects.get(usuarioDJ_id=usuarioLogeado)

        if usuarioLogeadoTabla2.Cargo == 'Usuario':
            return render_to_response('baseUsuarios.html',context_instance=RequestContext(request))
        elif usuarioLogeadoTabla2.Cargo == 'Administrador':
            return render_to_response('base.html',context_instance=RequestContext(request))
    else:
        if request.POST:
            username =request.POST['usuario']
            password =request.POST['pass']
            user =authenticate(username=username, password=password)
            if user is not None and user.is_active:
                usao=user.id
                usi=Usuario.objects.get(usuarioDJ_id=usao)

                asist=Asistencia(
                    Usuar=usi
                )
                asist.save()

                if user.id == usi.usuarioDJ_id and  usi.Cargo == 'Usuario':
                    login(request, user)
                    return render_to_response('baseUsuarios.html',{'usuario': usi},context_instance=RequestContext(request))
                elif user.id == usi.usuarioDJ_id and usi.Cargo == "Administrador":
                    login(request, user)
                    message=str(time.strftime("20%y-%m-%d"))
                    print message
                    return render_to_response('base.html',{'usuario':usi,'cxc':Cuentas_Cobrar.objects.filter(Fecha_Vencimiento=message).count(),'cxp':Cuentas_Pagar.objects.filter(Fecha_Vencimiento=message).exclude(Valor_Saldo=0).count()},context_instance=RequestContext(request))
            else:
                message="Nombre de usuario y Password incorrecto"
        return render_to_response('index.html', {'msj':message},
                                  context_instance=RequestContext(request))

def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')