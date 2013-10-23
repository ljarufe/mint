# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cliente'
        db.create_table(u'ventas_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=9, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
        ))
        db.send_create_signal(u'ventas', ['Cliente'])

        # Adding model 'Vale'
        db.create_table(u'ventas_vale', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ventas.Cliente'])),
        ))
        db.send_create_signal(u'ventas', ['Vale'])

        # Adding model 'Credito'
        db.create_table(u'ventas_credito', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('capital_pactado', self.gf('django.db.models.fields.FloatField')()),
            ('saldo_capital', self.gf('django.db.models.fields.FloatField')()),
            ('numero_cuotas', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha_inicial', self.gf('django.db.models.fields.DateField')()),
            ('fecha_final', self.gf('django.db.models.fields.DateField')()),
            ('estado_credito', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'ventas', ['Credito'])

        # Adding model 'PlanPago'
        db.create_table(u'ventas_planpago', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('credito', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ventas.Credito'])),
            ('numero_cuota', self.gf('django.db.models.fields.IntegerField')()),
            ('estado_cuota', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('capital_pactado', self.gf('django.db.models.fields.FloatField')()),
            ('capital_pagado', self.gf('django.db.models.fields.FloatField')()),
            ('fecha_vencimiento', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'ventas', ['PlanPago'])

        # Adding model 'Venta'
        db.create_table(u'ventas_venta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ventas.Cliente'])),
            ('fecha', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
            ('vale', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ventas.Vale'], null=True, blank=True)),
            ('descuento', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('total', self.gf('django.db.models.fields.FloatField')()),
            ('tipo_pago', self.gf('django.db.models.fields.CharField')(default=u'Co', max_length=2)),
            ('credito', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ventas.Credito'], null=True, blank=True)),
        ))
        db.send_create_signal(u'ventas', ['Venta'])

        # Adding M2M table for field productos on 'Venta'
        m2m_table_name = db.shorten_name(u'ventas_venta_productos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('venta', models.ForeignKey(orm[u'ventas.venta'], null=False)),
            ('producto', models.ForeignKey(orm[u'compras.producto'], null=False))
        ))
        db.create_unique(m2m_table_name, ['venta_id', 'producto_id'])


    def backwards(self, orm):
        # Deleting model 'Cliente'
        db.delete_table(u'ventas_cliente')

        # Deleting model 'Vale'
        db.delete_table(u'ventas_vale')

        # Deleting model 'Credito'
        db.delete_table(u'ventas_credito')

        # Deleting model 'PlanPago'
        db.delete_table(u'ventas_planpago')

        # Deleting model 'Venta'
        db.delete_table(u'ventas_venta')

        # Removing M2M table for field productos on 'Venta'
        db.delete_table(db.shorten_name(u'ventas_venta_productos'))


    models = {
        u'compras.envio': {
            'Meta': {'object_name': 'Envio'},
            'costo_aduana': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'costo_envio': ('django.db.models.fields.FloatField', [], {}),
            'costo_extra': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'fecha_envio': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'fecha_llegada': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tienda': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compras.Tienda']"}),
            'tipo_cambio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tipo_moneda': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'compras.foto': {
            'Meta': {'object_name': 'Foto'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'compras.marca': {
            'Meta': {'object_name': 'Marca'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'compras.producto': {
            'Meta': {'object_name': 'Producto'},
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5'}),
            'costo_envio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'costo_total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'envio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compras.Envio']"}),
            'estado': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio_compra': ('django.db.models.fields.FloatField', [], {}),
            'precio_final': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'precio_venta': ('django.db.models.fields.FloatField', [], {}),
            'talla': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compras.TipoProducto']"}),
            'utilidad': ('django.db.models.fields.FloatField', [], {})
        },
        u'compras.tienda': {
            'Meta': {'object_name': 'Tienda'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'compras.tipoproducto': {
            'Meta': {'object_name': 'TipoProducto'},
            'foto_principal': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fotos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['compras.Foto']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compras.Marca']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'ventas.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'})
        },
        u'ventas.credito': {
            'Meta': {'object_name': 'Credito'},
            'capital_pactado': ('django.db.models.fields.FloatField', [], {}),
            'estado_credito': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fecha_final': ('django.db.models.fields.DateField', [], {}),
            'fecha_inicial': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero_cuotas': ('django.db.models.fields.IntegerField', [], {}),
            'saldo_capital': ('django.db.models.fields.FloatField', [], {})
        },
        u'ventas.planpago': {
            'Meta': {'object_name': 'PlanPago'},
            'capital_pactado': ('django.db.models.fields.FloatField', [], {}),
            'capital_pagado': ('django.db.models.fields.FloatField', [], {}),
            'credito': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ventas.Credito']"}),
            'estado_cuota': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fecha_vencimiento': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero_cuota': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ventas.vale': {
            'Meta': {'object_name': 'Vale'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ventas.Cliente']"}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'ventas.venta': {
            'Meta': {'object_name': 'Venta'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ventas.Cliente']"}),
            'credito': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ventas.Credito']", 'null': 'True', 'blank': 'True'}),
            'descuento': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['compras.Producto']", 'symmetrical': 'False'}),
            'tipo_pago': ('django.db.models.fields.CharField', [], {'default': "u'Co'", 'max_length': '2'}),
            'total': ('django.db.models.fields.FloatField', [], {}),
            'vale': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ventas.Vale']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['ventas']