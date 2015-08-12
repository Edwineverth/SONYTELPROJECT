# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Articulossegunda(models.Model):
    art_nombre = models.CharField(max_length=30)
    art_precio = models.FloatField()
    art_cantidad = models.IntegerField()
    art_serie = models.CharField(max_length=50)
    mar = models.ForeignKey('Categoria', blank=True, null=True)
    mod = models.ForeignKey('Modelo', blank=True, null=True)
    art_estado = models.CharField(max_length=1)
    def __unicode__(self):
        return self.art_nombre




class Categoria(models.Model):
    mar_nombre = models.CharField(max_length=30)
    mar_descripcion = models.CharField(max_length=75)
    def __unicode__(self):
        return self.mar_nombre



class Ciudad(models.Model):
   
    ciu_nombre = models.CharField(max_length=30)
    ciu_descripcion = models.CharField(max_length=70)
    def __unicode__(self):
		return self.ciu_nombre


class Clientes(models.Model):
    cli_cedula = models.CharField(max_length=10)
    cli_nombre = models.CharField(max_length=30)
    cli_apellido = models.CharField(max_length=30)
    cli_telefono = models.CharField(max_length=10, blank=True)
    cli_direccion = models.CharField(max_length=75)
    cli_email = models.CharField(max_length=75)
    cli_estado = models.CharField(max_length=1)
    ciu = models.ForeignKey(Ciudad, blank=True, null=True)
    def __unicode__(self):
		return self.cli_nombre
  

class Detalleproveedor(models.Model):
    pro = models.ForeignKey('Productos', primary_key=True)
    kar_precio_proveedor = models.FloatField(db_column='kar_Precio_proveedor')  # Field name made lowercase.
    kar_entra = models.IntegerField()
    kar_sald = models.IntegerField()
    kar_fecha = models.DateTimeField()
    ord = models.ForeignKey('OrdenDeCompra', blank=True, null=True)

   
class Factura(models.Model):
    fac_subtotal = models.FloatField()
    fac_iva = models.FloatField()
    fac_descuento = models.FloatField(verbose_name=u"Ingrese descuento")
    fac_total = models.FloatField()
    fac_fecha = models.DateField()
    fac_estado = models.CharField(max_length=1)
    cli = models.ForeignKey(Clientes, blank=True, null=True)

 

class Facturadetalle(models.Model):
    fac = models.ForeignKey(Factura, blank=True, null=True)
    pro = models.ForeignKey('Productos', blank=True, null=True)
    det_cantiadd = models.IntegerField()
    det_preciou = models.FloatField()
    det_preciot = models.FloatField()


class Facturadetallemantenimiento(models.Model):
    fac = models.ForeignKey(Factura)
    solm = models.ForeignKey('Solicitudmantenimiento')
    fad_preciou = models.FloatField()
    fad_preciot = models.FloatField()


class Mantenimiento(models.Model):
 
    man_fecha = models.DateField()
    man_garantia = models.IntegerField()
    man_informe = models.CharField(max_length=300)
    man_fechaentrega = models.DateField()
    man_estado = models.CharField(max_length=1, blank=True)
    solm = models.ForeignKey('Solicitudmantenimiento')



class Mensajeria(models.Model):
 
    men_asunto = models.CharField(max_length=30)
    men_descripcion = models.CharField(max_length=500)
    cli = models.ForeignKey(Clientes)
    def __unicode__(self):
        return self.men_asunto




class Modelo(models.Model):
   
    mod_nombre = models.CharField(max_length=30)
    mod_descripcion = models.CharField(max_length=75)
    def __unicode__(self):
        return self.mod_nombre

 


class OrdenDeCompra(models.Model):
  
    ord_subtotal = models.FloatField()
    ord_iva = models.FloatField()
    ord_descuento = models.FloatField()
    ord_total = models.FloatField()
    ord_fecha = models.DateField()
    prov = models.ForeignKey('Proveedor')
    ord_estado = models.CharField(max_length=1)

   

class Productos(models.Model):
   
    pro_nombre = models.CharField(max_length=30)
    pro_cantidad = models.IntegerField()
    pro_precio = models.FloatField()
    pro_ecg = models.CharField(max_length=75, blank=True)
    pro_tarifa_iva = models.FloatField()
    pro_ex = models.IntegerField()
    pro_pvp = models.FloatField()
    mar = models.ForeignKey(Categoria, blank=True, null=True)
    def __unicode__(self):
        return self.pro_nombre

   

class Proveedor(models.Model):
   
    prov_ruc = models.CharField(max_length=10)
    prov_cedula = models.CharField(max_length=10)
    prov_nombre = models.CharField(max_length=30)
    prov_representante = models.CharField(max_length=50)
    prov_direccion = models.CharField(max_length=80)
    prov_telefono = models.CharField(max_length=10, blank=True)
    ciu = models.ForeignKey(Ciudad, blank=True, null=True)
    prov_estado = models.CharField(max_length=1, blank=True)




class Repuestos(models.Model):
    man = models.ForeignKey(Mantenimiento)
    pro = models.ForeignKey(Productos)
    rep_cantidad = models.IntegerField()

 

class Solicitudmantenimiento(models.Model):
 
    solm_fecha = models.DateField()
    solm_falla = models.CharField(max_length=100)
    solm_observaciones = models.CharField(max_length=100, blank=True)
    solm_abono = models.FloatField()
    solm_saldo = models.FloatField()
    solm_total = models.FloatField()
    solm_estado = models.CharField(max_length=1, blank=True)
    art = models.ForeignKey(Articulossegunda)
    cli = models.ForeignKey(Clientes, blank=True, null=True)

   
