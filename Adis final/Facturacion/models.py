from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
    Cedula = models.CharField(max_length=10, primary_key=True)
    Nombre = models.CharField(max_length=45)
    Apellido = models.CharField(max_length=45)
    Direccion = models.CharField(max_length=45)
    Ciudad = models.CharField(max_length=45)
    Cargo = models.CharField(max_length=45)
    Telefono = models.CharField(max_length=10)
    Estado=models.CharField(max_length=10)
    Sexo = models.CharField(max_length=9)
    usuarioDJ=models.ForeignKey(User, unique=True)

class Asistencia(models.Model):
    Hora_entrada = models.DateTimeField(auto_now=True)
    Usuar=models.ForeignKey(Usuario)


class Clientes(models.Model):
    Cedula = models.CharField(max_length=10, primary_key=True)
    Nombre = models.CharField(max_length=45)
    Apellido = models.CharField(max_length=45)
    Direccion = models.CharField(max_length=45)
    Ciudad = models.CharField(max_length=45)
    Telefono = models.CharField(max_length=10)
    Correo_Electronico = models.CharField(max_length=100)
    Estado=models.CharField(max_length=10)
    Sexo = models.CharField(max_length=9)



class Proveedores(models.Model):
    RUC = models.CharField(max_length=13, primary_key=True)
    Razon_Social = models.CharField(max_length=80)
    Direccion = models.CharField(max_length=45)
    Ciudad = models.CharField(max_length=45)
    Telefono = models.CharField(max_length=10)
    Estado=models.CharField(max_length=10)
    Correo_Electronico = models.CharField(max_length=100)

class Categorias(models.Model):
    Nombre = models.CharField(max_length=45)

class Productos(models.Model):
    Codigo = models.CharField(max_length=8, primary_key=True)
    Nombre = models.CharField(max_length=45)
    Cantidad = models.IntegerField()
    Precio_Venta = models.DecimalField(max_digits=8,decimal_places=2)
    Estado=models.CharField(max_length=10)
    categoria=models.ForeignKey(Categorias)


class Pedidos(models.Model):
    Numero = models.IntegerField(primary_key=True)########
    Estado = models.CharField(max_length=10)
    Fecha_Emision = models.DateField(auto_now=True)
    Total = models.DecimalField(max_digits=8,decimal_places=2)
    RUC = models.ForeignKey(Proveedores)

class Detalle_Pedido(models.Model):
    Codigo_Producto = models.ForeignKey(Productos)
    Pedido = models.ForeignKey(Pedidos)
    Cantidad = models.IntegerField()
    Precio_Untario = models.DecimalField(max_digits=8,decimal_places=2)

class Factura_Venta(models.Model):
    Numero = models.IntegerField(primary_key=True)
    Fecha_Emision = models.DateField(auto_now=True)
    Total = models.DecimalField(max_digits=8,decimal_places=2)
    Subtotal = models.DecimalField(max_digits=8,decimal_places=2)
    Dscto = models.DecimalField(max_digits=8,decimal_places=2)
    IVA = models.DecimalField(max_digits=8,decimal_places=2)
    Estado = models.CharField(max_length=10)
    Cedula = models.ForeignKey(Clientes)
    Usuario = models.ForeignKey(Usuario)

class Detalle_Factura_Venta(models.Model):
    Producto = models.ForeignKey(Productos)
    Fact_Venta = models.ForeignKey(Factura_Venta)
    Cantidad = models.IntegerField()
    Precio_Venta = models.DecimalField(max_digits=8,decimal_places=2)

class Cuentas_Cobrar(models.Model):
    Numero = models.IntegerField(primary_key=True)
    Concepto = models.CharField(max_length=45)
    Valor_Total = models.DecimalField(max_digits=8,decimal_places=2)
    Valor_Saldo = models.DecimalField(max_digits=8,decimal_places=2)
    Valor_Cancelado = models.DecimalField(max_digits=8,decimal_places=2)
    Estado = models.CharField(max_length=10)
    Fecha_Inicio = models.DateField(auto_now=True)
    Fecha_Vencimiento = models.DateField()
    Fact_Venta = models.ForeignKey(Factura_Venta)

class Comprobantes_Cuenta_Cobrar(models.Model):
    Numero = models.IntegerField(primary_key=True)
    Fecha_Pago = models.DateField(auto_now=True)
    Valor_Cancelar = models.DecimalField(max_digits=8,decimal_places=2)
    Concepto = models.CharField(max_length=45)
    Saldo = models.DecimalField(max_digits=8,decimal_places=2)
    CCxCC = models.ForeignKey(Cuentas_Cobrar)

class Cuentas_Pagar(models.Model):
    Numero = models.IntegerField(primary_key=True)
    Concepto = models.CharField(max_length=45)
    Valor_Total = models.DecimalField(max_digits=8,decimal_places=2)
    Valor_Saldo = models.DecimalField(max_digits=8,decimal_places=2)
    Valor_Cancelado = models.DecimalField(max_digits=8,decimal_places=2)
    Estado = models.CharField(max_length=10)
    Fecha_Inicio = models.DateField(auto_now=True)
    Fecha_Vencimiento = models.DateField()
    Pedidos = models.ForeignKey(Pedidos)

class Comprobantes_Cuenta_Pagar(models.Model):
    Numero = models.IntegerField(primary_key=True)
    Fecha_Pago = models.DateField(auto_now=True)
    Valor_Cancelar = models.DecimalField(max_digits=8,decimal_places=2)
    Concepto = models.CharField(max_length=45)
    Saldo = models.DecimalField(max_digits=8,decimal_places=2)
    CCxPP = models.ForeignKey(Cuentas_Pagar)
