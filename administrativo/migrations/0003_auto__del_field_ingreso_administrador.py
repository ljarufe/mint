# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Ingreso.administrador'
        db.delete_column(u'administrativo_ingreso', 'administrador_id')


    def backwards(self, orm):
        # Adding field 'Ingreso.administrador'
        db.add_column(u'administrativo_ingreso', 'administrador',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['auth.User']),
                      keep_default=False)


    models = {
        u'administrativo.egresoadministrativo': {
            'Meta': {'ordering': "('fecha',)", 'object_name': 'EgresoAdministrativo'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'detalle_general': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'multiple': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'precio_neto': ('django.db.models.fields.FloatField', [], {}),
            'precio_unitario': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tipo_cambio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tipo_moneda': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'administrativo.ingreso': {
            'Meta': {'object_name': 'Ingreso'},
            'detalle_general': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.FloatField', [], {}),
            'tipo_cambio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tipo_moneda': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['administrativo']