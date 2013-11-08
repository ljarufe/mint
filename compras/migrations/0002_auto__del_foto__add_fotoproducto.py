# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Foto'
        db.delete_table(u'compras_foto')

        # Adding model 'FotoProducto'
        db.create_table(u'compras_fotoproducto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('tipo_producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compras.TipoProducto'])),
        ))
        db.send_create_signal(u'compras', ['FotoProducto'])

        # Removing M2M table for field fotos on 'TipoProducto'
        db.delete_table(db.shorten_name(u'compras_tipoproducto_fotos'))


    def backwards(self, orm):
        # Adding model 'Foto'
        db.create_table(u'compras_foto', (
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'compras', ['Foto'])

        # Deleting model 'FotoProducto'
        db.delete_table(u'compras_fotoproducto')

        # Adding M2M table for field fotos on 'TipoProducto'
        m2m_table_name = db.shorten_name(u'compras_tipoproducto_fotos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tipoproducto', models.ForeignKey(orm[u'compras.tipoproducto'], null=False)),
            ('foto', models.ForeignKey(orm[u'compras.foto'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tipoproducto_id', 'foto_id'])


    models = {
        u'compras.envio': {
            'Meta': {'ordering': "('fecha_envio',)", 'object_name': 'Envio'},
            'costo_aduana': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'costo_envio': ('django.db.models.fields.FloatField', [], {}),
            'costo_extra': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'fecha_envio': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'fecha_llegada': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tienda': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compras.Tienda']"}),
            'tipo_cambio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tipo_moneda': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'})
        },
        u'compras.fotoproducto': {
            'Meta': {'object_name': 'FotoProducto'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'tipo_producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compras.TipoProducto']"})
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
            'Meta': {'ordering': "('nombre',)", 'object_name': 'Tienda'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'compras.tipoproducto': {
            'Meta': {'object_name': 'TipoProducto'},
            'foto_principal': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compras.Marca']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['compras']