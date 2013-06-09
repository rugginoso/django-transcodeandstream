# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'VirtualFilesystemNode'
        db.create_table(u'transcodeandstream_virtualfilesystemnode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('video', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='children', to=orm['transcodeandstream.VirtualFilesystemNode'])),
        ))
        db.send_create_signal(u'transcodeandstream', ['VirtualFilesystemNode'])

        # Adding unique constraint on 'VirtualFilesystemNode', fields ['name', 'parent']
        db.create_unique(u'transcodeandstream_virtualfilesystemnode', ['name', 'parent_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'VirtualFilesystemNode', fields ['name', 'parent']
        db.delete_unique(u'transcodeandstream_virtualfilesystemnode', ['name', 'parent_id'])

        # Deleting model 'VirtualFilesystemNode'
        db.delete_table(u'transcodeandstream_virtualfilesystemnode')


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
        },
        u'transcodeandstream.virtualfilesystemnode': {
            'Meta': {'ordering': "('video', 'name')", 'unique_together': "(('name', 'parent'),)", 'object_name': 'VirtualFilesystemNode'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'children'", 'to': u"orm['transcodeandstream.VirtualFilesystemNode']"}),
            'video': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'})
        }
    }

    complete_apps = ['transcodeandstream']