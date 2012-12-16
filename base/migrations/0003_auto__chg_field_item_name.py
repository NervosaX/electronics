# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Item.name'
        db.alter_column('base_item', 'name', self.gf('django.db.models.fields.CharField')(default='Test', max_length=100))

    def backwards(self, orm):

        # Changing field 'Item.name'
        db.alter_column('base_item', 'name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

    models = {
        'base.item': {
            'Meta': {'object_name': 'Item'},
            'amperage': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['base.ItemCategory']"}),
            'datasheet': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '600', 'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'value_conversion': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'value_prefix': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '20', 'blank': 'True'}),
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