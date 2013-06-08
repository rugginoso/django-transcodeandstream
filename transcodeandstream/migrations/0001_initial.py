# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EncodeQueueEntry'
        db.create_table(u'transcodeandstream_encodequeueentry', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=10, primary_key=True)),
            ('original_filename', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('working_on', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'transcodeandstream', ['EncodeQueueEntry'])


    def backwards(self, orm):
        # Deleting model 'EncodeQueueEntry'
        db.delete_table(u'transcodeandstream_encodequeueentry')


    models = {
        u'transcodeandstream.encodequeueentry': {
            'Meta': {'ordering': "('created_at',)", 'object_name': 'EncodeQueueEntry'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'working_on': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['transcodeandstream']