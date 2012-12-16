# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ItemCategory'
        db.create_table('base_itemcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('suffix', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('base', ['ItemCategory'])

        # Adding model 'Item'
        db.create_table('base_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['base.ItemCategory'])),
            ('amperage', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('voltage', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('value_prefix', self.gf('django.db.models.fields.CharField')(default='1', max_length=20)),
            ('value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('value_conversion', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('item_number', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('datasheet', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=600, null=True, blank=True)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('base', ['Item'])


    def backwards(self, orm):
        # Deleting model 'ItemCategory'
        db.delete_table('base_itemcategory')

        # Deleting model 'Item'
        db.delete_table('base_item')


    models = {
        'base.item': {
            'Meta': {'object_name': 'Item'},
            'amperage': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['base.ItemCategory']"}),
            'datasheet': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '600', 'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'value_conversion': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'value_prefix': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '20'}),
            'voltage': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'base.itemcategory': {
            'Meta': {'object_name': 'ItemCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['base']