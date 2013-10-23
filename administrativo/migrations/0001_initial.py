# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EgresoAdministrativo'
        db.create_table(u'administrativo_egresoadministrativo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('detalle_general', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('fecha', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
            ('tipo_cambio', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('tipo_moneda', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('precio_unitario', self.gf('django.db.models.fields.FloatField')()),
            ('multiple', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('precio_neto', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('unidad', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'administrativo', ['EgresoAdministrativo'])

        # Adding model 'Ingreso'
        db.create_table(u'administrativo_ingreso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('detalle_general', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('administrador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('fecha', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
            ('monto', self.gf('django.db.models.fields.FloatField')()),
            ('tipo_cambio', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('tipo_moneda', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'administrativo', ['Ingreso'])


    def backwards(self, orm):
        # Deleting model 'EgresoAdministrativo'
        db.delete_table(u'administrativo_egresoadministrativo')

        # Deleting model 'Ingreso'
        db.delete_table(u'administrativo_ingreso')


    models = {
        u'administrativo.egresoadministrativo': {
            'Meta': {'object_name': 'EgresoAdministrativo'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'detalle_general': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'multiple': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'precio_neto': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'precio_unitario': ('django.db.models.fields.FloatField', [], {}),
            'tipo_cambio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tipo_moneda': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'administrativo.ingreso': {
            'Meta': {'object_name': 'Ingreso'},
            'administrador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'detalle_general': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.FloatField', [], {}),
            'tipo_cambio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tipo_moneda': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['administrativo']