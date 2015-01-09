# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'Packaging.news_slug' to match new field type.
        db.rename_column(u'cmsplugin_packaging', 'news_slug', 'news_slug_id')
        # Changing field 'Packaging.news_slug'
        db.alter_column(u'cmsplugin_packaging', 'news_slug_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mcrm.Category']))

    def backwards(self, orm):

        # Renaming column for 'Packaging.news_slug' to match new field type.
        db.rename_column(u'cmsplugin_packaging', 'news_slug_id', 'news_slug')
        # Changing field 'Packaging.news_slug'
        db.alter_column(u'cmsplugin_packaging', 'news_slug', self.gf('django.db.models.fields.SlugField')(max_length=50))

    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'mcrm.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'parrot_product.blurb': {
            'Meta': {'object_name': 'Blurb', 'db_table': "u'cmsplugin_blurb'"},
            'alignment': ('django.db.models.fields.CharField', [], {'default': "'centered'", 'max_length': '20'}),
            'background': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'button': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('djangocms_text_ckeditor.fields.HTMLField', [], {}),
            'htmlid': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'parrot_product.overview': {
            'Meta': {'object_name': 'Overview', 'db_table': "u'cmsplugin_overview'"},
            'badges': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['parrot_product.OverviewBadge']", 'symmetrical': 'False'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'htmlid': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'parrot_product.overviewbadge': {
            'Meta': {'object_name': 'OverviewBadge'},
            'admin_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'text': ('djangocms_text_ckeditor.fields.HTMLField', [], {}),
            'weighting': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '10'})
        },
        u'parrot_product.packaging': {
            'Meta': {'object_name': 'Packaging', 'db_table': "u'cmsplugin_packaging'"},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'colors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['parrot_product.PackagingColor']", 'symmetrical': 'False'}),
            'description': ('djangocms_text_ckeditor.fields.HTMLField', [], {}),
            'htmlid': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'news_availability': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'news_slug': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mcrm.Category']"}),
            'shop_availability': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'shop_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'parrot_product.packagingcolor': {
            'Meta': {'object_name': 'PackagingColor'},
            'admin_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'hexa': ('paintstore.fields.ColorPickerField', [], {'max_length': '7', 'blank': 'True'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'package': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'weighting': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '10'})
        },
        u'parrot_product.spec': {
            'Meta': {'object_name': 'Spec', 'db_table': "u'cmsplugin_spec'"},
            'alignment': ('django.db.models.fields.CharField', [], {'default': "'left'", 'max_length': '20'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('djangocms_text_ckeditor.fields.HTMLField', [], {'blank': 'True'}),
            'htmlid': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'parrot_product.subscribe': {
            'Meta': {'object_name': 'Subscribe', 'db_table': "u'cmsplugin_subscribe'"},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'htmlid': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'message': ('djangocms_text_ckeditor.fields.HTMLField', [], {}),
            'subscribe_to': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mcrm.Category']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'parrot_product.tab': {
            'Meta': {'object_name': 'Tab', 'db_table': "u'cmsplugin_tab'"},
            'background': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'htmlid': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'icons': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['parrot_product.TabIcon']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'parrot_product.tabicon': {
            'Meta': {'object_name': 'TabIcon'},
            'active_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'admin_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'background': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'passive_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'text': ('djangocms_text_ckeditor.fields.HTMLField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'weighting': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '10'})
        },
        u'parrot_product.twentytwenty': {
            'Meta': {'object_name': 'TwentyTwenty', 'db_table': "u'cmsplugin_twentytwenty'"},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('djangocms_text_ckeditor.fields.HTMLField', [], {}),
            'htmlid': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'left_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'left_legend': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'right_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'right_legend': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'parrot_product.videogroup': {
            'Meta': {'object_name': 'VideoGroup', 'db_table': "u'cmsplugin_videogroup'"},
            'background': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'files': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['parrot_product.VideoGroupFile']", 'symmetrical': 'False'}),
            'htmlid': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'parrot_product.videogroupfile': {
            'Meta': {'object_name': 'VideoGroupFile'},
            'admin_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'weighting': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '10'})
        }
    }

    complete_apps = ['parrot_product']