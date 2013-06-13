# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'EncodeQueueEntry', fields ['original_filename']
        db.delete_unique(u'transcodeandstream_encodequeueentry', ['original_filename'])

        # Adding field 'EncodeQueueEntry.transcode_format'
        db.add_column(u'transcodeandstream_encodequeueentry', 'transcode_format',
                      self.gf('django.db.models.fields.CharField')(default='webm', max_length=255),
                      keep_default=False)

        # Adding unique constraint on 'EncodeQueueEntry', fields ['transcode_format', 'id', 'original_filename']
        db.create_unique(u'transcodeandstream_encodequeueentry', ['transcode_format', 'id', 'original_filename'])


    def backwards(self, orm):
        # Removing unique constraint on 'EncodeQueueEntry', fields ['transcode_format', 'id', 'original_filename']
        db.delete_unique(u'transcodeandstream_encodequeueentry', ['transcode_format', 'id', 'original_filename'])

        # Deleting field 'EncodeQueueEntry.transcode_format'
        db.delete_column(u'transcodeandstream_encodequeueentry', 'transcode_format')

        # Adding unique constraint on 'EncodeQueueEntry', fields ['original_filename']
        db.create_unique(u'transcodeandstream_encodequeueentry', ['original_filename'])


    models = {
        u'transcodeandstream.encodequeueentry': {
            'Meta': {'ordering': "('created_at',)", 'unique_together': "(('id', 'original_filename', 'transcode_format'),)", 'object_name': 'EncodeQueueEntry'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'error': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'log': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'progress': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'transcode_format': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'working_on': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'transcodeandstream.virtualfilesystemnode': {
            'Meta': {'ordering': "('video', 'name')", 'unique_together': "(('name', 'parent'),)", 'object_name': 'VirtualFilesystemNode'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'children'", 'null': 'True', 'to': u"orm['transcodeandstream.VirtualFilesystemNode']"}),
            'video': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'})
        }
    }

    complete_apps = ['transcodeandstream']