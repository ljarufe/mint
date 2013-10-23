# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Foto'
        db.create_table(u'compras_foto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'compras', ['Foto'])

        # Adding model 'Tienda'
        db.create_table(u'compras_tienda', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('observaciones', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'compras', ['Tienda'])

        # Adding model 'Envio'
        db.create_table(u'compras_envio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tienda', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compras.Tienda'])),
            ('costo_envio', self.gf('django.db.models.fields.FloatField')()),
            ('tipo_cambio', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('tipo_moneda', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('costo_aduana', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('costo_extra', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('fecha_envio', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
            ('fecha_llegada', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'compras', ['Envio'])

        # Adding model 'Marca'
        db.create_table(u'compras_marca', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'compras', ['Marca'])

        # Adding model 'TipoProducto'
        db.create_table(u'compras_tipoproducto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('marca', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compras.Marca'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('foto_principal', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'compras', ['TipoProducto'])

        # Adding M2M table for field fotos on 'TipoProducto'
        m2m_table_name = db.shorten_name(u'compras_tipoproducto_fotos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tipoproducto', models.ForeignKey(orm[u'compras.tipoproducto'], null=False)),
            ('foto', models.ForeignKey(orm[u'compras.foto'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tipoproducto_id', 'foto_id'])

        # Adding model 'Producto'
        db.create_table(u'compras_producto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=5)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compras.TipoProducto'])),
            ('talla', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('envio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compras.Envio'])),
            ('precio_compra', self.gf('django.db.models.fields.FloatField')()),
            ('costo_envio', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('costo_total', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('utilidad', self.gf('django.db.models.fields.FloatField')()),
            ('precio_venta', self.gf('django.db.models.fields.FloatField')()),
            ('precio_final', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('estado', self.gf('django.db.models.fields.CharField')(default='P', max_length=1)),
        ))
        db.send_create_signal(u'compras', ['Producto'])


    def backwards(self, orm):
        # Deleting model 'Foto'
        db.delete_table(u'compras_foto')

        # Deleting model 'Tienda'
        db.delete_table(u'compras_tienda')

        # Deleting model 'Envio'
        db.delete_table(u'compras_envio')

        # Deleting model 'Marca'
        db.delete_table(u'compras_marca')

        # Deleting model 'TipoProducto'
        db.delete_table(u'compras_tipoproducto')

        # Removing M2M table for field fotos on 'TipoProducto'
        db.delete_table(db.shorten_name(u'compras_tipoproducto_fotos'))

        # Deleting model 'Producto'
        db.delete_table(u'compras_producto')


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
        }
    }

    complete_apps = ['compras']