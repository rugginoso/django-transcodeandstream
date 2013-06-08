# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'EncodeQueueEntry', fields ['id', 'original_filename']
        db.delete_unique(u'transcodeandstream_encodequeueentry', ['id', 'original_filename'])

        # Adding unique constraint on 'EncodeQueueEntry', fields ['original_filename']
        db.create_unique(u'transcodeandstream_encodequeueentry', ['original_filename'])


    def backwards(self, orm):
        # Removing unique constraint on 'EncodeQueueEntry', fields ['original_filename']
        db.delete_unique(u'transcodeandstream_encodequeueentry', ['original_filename'])

        # Adding unique constraint on 'EncodeQueueEntry', fields ['id', 'original_filename']
        db.create_unique(u'transcodeandstream_encodequeueentry', ['id', 'original_filename'])


    models = {
        u'transcodeandstream.encodequeueentry': {
            'Meta': {'ordering': "('created_at',)", 'object_name': 'EncodeQueueEntry'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10', 'primary_key': 'True'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'working_on': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['transcodeandstream']