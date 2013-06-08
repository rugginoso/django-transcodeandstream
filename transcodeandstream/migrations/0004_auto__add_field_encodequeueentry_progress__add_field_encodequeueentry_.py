# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'EncodeQueueEntry.progress'
        db.add_column(u'transcodeandstream_encodequeueentry', 'progress',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'EncodeQueueEntry.error'
        db.add_column(u'transcodeandstream_encodequeueentry', 'error',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'EncodeQueueEntry.log'
        db.add_column(u'transcodeandstream_encodequeueentry', 'log',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'EncodeQueueEntry.progress'
        db.delete_column(u'transcodeandstream_encodequeueentry', 'progress')

        # Deleting field 'EncodeQueueEntry.error'
        db.delete_column(u'transcodeandstream_encodequeueentry', 'error')

        # Deleting field 'EncodeQueueEntry.log'
        db.delete_column(u'transcodeandstream_encodequeueentry', 'log')


    models = {
        u'transcodeandstream.encodequeueentry': {
            'Meta': {'ordering': "('created_at',)", 'object_name': 'EncodeQueueEntry'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'error': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10', 'primary_key': 'True'}),
            'log': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'progress': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'working_on': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['transcodeandstream']