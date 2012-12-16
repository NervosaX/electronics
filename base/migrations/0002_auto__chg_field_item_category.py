# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Item.category'
        db.alter_column('base_item', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['base.ItemCategory']))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Item.category'
        raise RuntimeError("Cannot reverse this migration. 'Item.category' and its values cannot be restored.")

    models = {
        'base.item': {
            'Meta': {'object_name': 'Item'},
            'amperage': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['base.ItemCategory']"}),
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