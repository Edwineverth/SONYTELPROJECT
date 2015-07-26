# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulossegunda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('art_nombre', models.CharField(max_length=30)),
                ('art_precio', models.FloatField()),
                ('art_cantidad', models.IntegerField()),
                ('art_serie', models.CharField(max_length=50)),
                ('art_estado', models.CharField(max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mar_nombre', models.CharField(max_length=30)),
                ('mar_descripcion', models.CharField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ciu_nombre', models.CharField(max_length=30)),
                ('ciu_descripcion', models.CharField(max_length=70)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cli_cedula', models.CharField(max_length=10)),
                ('cli_nombre', models.CharField(max_length=30)),
                ('cli_apellido', models.CharField(max_length=30)),
                ('cli_telefono', models.CharField(max_length=10, blank=True)),
                ('cli_direccion', models.CharField(max_length=75)),
                ('cli_email', models.CharField(max_length=75)),
                ('cli_estado', models.CharField(max_length=1)),
                ('ciu', models.ForeignKey(blank=True, to='sistema.Ciudad', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fac_subtotal', models.FloatField()),
                ('fac_iva', models.FloatField()),
                ('fac_descuento', models.FloatField()),
                ('fac_total', models.FloatField()),
                ('fac_fecha', models.DateField()),
                ('fac_estado', models.CharField(max_length=1)),
                ('cli', models.ForeignKey(blank=True, to='sistema.Clientes', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Facturadetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('det_cantiadd', models.IntegerField()),
                ('det_preciou', models.FloatField()),
                ('det_preciot', models.FloatField()),
                ('fac', models.ForeignKey(blank=True, to='sistema.Factura', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Facturadetallemantenimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fad_preciou', models.FloatField()),
                ('fad_preciot', models.FloatField()),
                ('fac', models.ForeignKey(to='sistema.Factura')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('man_fecha', models.DateField()),
                ('man_garantia', models.IntegerField()),
                ('man_informe', models.CharField(max_length=300)),
                ('man_fechaentrega', models.DateField()),
                ('man_estado', models.CharField(max_length=1, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mensajeria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('men_asunto', models.CharField(max_length=30)),
                ('men_descripcion', models.CharField(max_length=500)),
                ('cli', models.ForeignKey(to='sistema.Clientes')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mod_nombre', models.CharField(max_length=30)),
                ('mod_descripcion', models.CharField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrdenDeCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ord_subtotal', models.FloatField()),
                ('ord_iva', models.FloatField()),
                ('ord_descuento', models.FloatField()),
                ('ord_total', models.FloatField()),
                ('ord_fecha', models.DateField()),
                ('ord_estado', models.CharField(max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pro_nombre', models.CharField(max_length=30)),
                ('pro_cantidad', models.IntegerField()),
                ('pro_precio', models.FloatField()),
                ('pro_ecg', models.CharField(max_length=75, blank=True)),
                ('pro_tarifa_iva', models.FloatField()),
                ('pro_ex', models.IntegerField()),
                ('pro_pvp', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Detalleproveedor',
            fields=[
                ('pro', models.ForeignKey(primary_key=True, serialize=False, to='sistema.Productos')),
                ('kar_precio_proveedor', models.FloatField(db_column='kar_Precio_proveedor')),
                ('kar_entra', models.IntegerField()),
                ('kar_sald', models.IntegerField()),
                ('kar_fecha', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prov_ruc', models.CharField(max_length=10)),
                ('prov_cedula', models.CharField(max_length=10)),
                ('prov_nombre', models.CharField(max_length=30)),
                ('prov_representante', models.CharField(max_length=50)),
                ('prov_direccion', models.CharField(max_length=80)),
                ('prov_telefono', models.CharField(max_length=10, blank=True)),
                ('prov_estado', models.CharField(max_length=1, blank=True)),
                ('ciu', models.ForeignKey(blank=True, to='sistema.Ciudad', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Repuestos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rep_cantidad', models.IntegerField()),
                ('man', models.ForeignKey(to='sistema.Mantenimiento')),
                ('pro', models.ForeignKey(to='sistema.Productos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Solicitudmantenimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('solm_fecha', models.DateField()),
                ('solm_falla', models.CharField(max_length=100)),
                ('solm_observaciones', models.CharField(max_length=100, blank=True)),
                ('solm_abono', models.FloatField()),
                ('solm_saldo', models.FloatField()),
                ('solm_total', models.FloatField()),
                ('solm_estado', models.CharField(max_length=1, blank=True)),
                ('art', models.ForeignKey(to='sistema.Articulossegunda')),
                ('cli', models.ForeignKey(blank=True, to='sistema.Clientes', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='productos',
            name='mar',
            field=models.ForeignKey(blank=True, to='sistema.Categoria', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ordendecompra',
            name='prov',
            field=models.ForeignKey(to='sistema.Proveedor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mantenimiento',
            name='solm',
            field=models.ForeignKey(to='sistema.Solicitudmantenimiento'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='facturadetallemantenimiento',
            name='solm',
            field=models.ForeignKey(to='sistema.Solicitudmantenimiento'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='facturadetalle',
            name='pro',
            field=models.ForeignKey(blank=True, to='sistema.Productos', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detalleproveedor',
            name='ord',
            field=models.ForeignKey(blank=True, to='sistema.OrdenDeCompra', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articulossegunda',
            name='mar',
            field=models.ForeignKey(blank=True, to='sistema.Categoria', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articulossegunda',
            name='mod',
            field=models.ForeignKey(blank=True, to='sistema.Modelo', null=True),
            preserve_default=True,
        ),
    ]
