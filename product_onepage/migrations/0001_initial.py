# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Blurb'
        db.create_table(u'cmsplugin_blurb', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('htmlid', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('background', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('mobile', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('description', self.gf('djangocms_text_ckeditor.fields.HTMLField')()),
            ('button', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('alignment', self.gf('django.db.models.fields.CharField')(default='centered', max_length=20)),
        ))
        db.send_create_signal(u'parrot_product', ['Blurb'])

        # Adding model 'Overview'
        db.create_table(u'cmsplugin_overview', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('htmlid', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'parrot_product', ['Overview'])

        # Adding M2M table for field badges on 'Overview'
        m2m_table_name = db.shorten_name(u'cmsplugin_overview_badges')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('overview', models.ForeignKey(orm[u'parrot_product.overview'], null=False)),
            ('overviewbadge', models.ForeignKey(orm[u'parrot_product.overviewbadge'], null=False))
        ))
        db.create_unique(m2m_table_name, ['overview_id', 'overviewbadge_id'])

        # Adding model 'OverviewBadge'
        db.create_table(u'parrot_product_overviewbadge', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('admin_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('text', self.gf('djangocms_text_ckeditor.fields.HTMLField')(blank=True)),
            ('weighting', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=10)),
        ))
        db.send_create_signal(u'parrot_product', ['OverviewBadge'])

        # Adding model 'Packaging'
        db.create_table(u'cmsplugin_packaging', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('htmlid', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('news_slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('description', self.gf('djangocms_text_ckeditor.fields.HTMLField')()),
            ('shop_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('shop_availability', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('news_availability', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'parrot_product', ['Packaging'])

        # Adding M2M table for field colors on 'Packaging'
        m2m_table_name = db.shorten_name(u'cmsplugin_packaging_colors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('packaging', models.ForeignKey(orm[u'parrot_product.packaging'], null=False)),
            ('packagingcolor', models.ForeignKey(orm[u'parrot_product.packagingcolor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['packaging_id', 'packagingcolor_id'])

        # Adding model 'PackagingColor'
        db.create_table(u'parrot_product_packagingcolor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('admin_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('package', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('hexa', self.gf('project.parrot_product.utils.ColourField')(max_length=6, blank=True)),
            ('icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('weighting', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=10)),
        ))
        db.send_create_signal(u'parrot_product', ['PackagingColor'])

        # Adding model 'Spec'
        db.create_table(u'cmsplugin_spec', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('htmlid', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('description', self.gf('djangocms_text_ckeditor.fields.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'parrot_product', ['Spec'])

        # Adding model 'Tab'
        db.create_table(u'cmsplugin_tab', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('htmlid', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('background', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'parrot_product', ['Tab'])

        # Adding M2M table for field icons on 'Tab'
        m2m_table_name = db.shorten_name(u'cmsplugin_tab_icons')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tab', models.ForeignKey(orm[u'parrot_product.tab'], null=False)),
            ('tabicon', models.ForeignKey(orm[u'parrot_product.tabicon'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tab_id', 'tabicon_id'])

        # Adding model 'TabIcon'
        db.create_table(u'parrot_product_tabicon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('admin_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('text', self.gf('djangocms_text_ckeditor.fields.HTMLField')(blank=True)),
            ('background', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('passive_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('active_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('weighting', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=10)),
        ))
        db.send_create_signal(u'parrot_product', ['TabIcon'])

        # Adding model 'VideoGroup'
        db.create_table(u'cmsplugin_videogroup', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('htmlid', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('background', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'parrot_product', ['VideoGroup'])

        # Adding M2M table for field files on 'VideoGroup'
        m2m_table_name = db.shorten_name(u'cmsplugin_videogroup_files')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('videogroup', models.ForeignKey(orm[u'parrot_product.videogroup'], null=False)),
            ('videogroupfile', models.ForeignKey(orm[u'parrot_product.videogroupfile'], null=False))
        ))
        db.create_unique(m2m_table_name, ['videogroup_id', 'videogroupfile_id'])

        # Adding model 'VideoGroupFile'
        db.create_table(u'parrot_product_videogroupfile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('admin_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('weighting', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=10)),
        ))
        db.send_create_signal(u'parrot_product', ['VideoGroupFile'])


    def backwards(self, orm):
        # Deleting model 'Blurb'
        db.delete_table(u'cmsplugin_blurb')

        # Deleting model 'Overview'
        db.delete_table(u'cmsplugin_overview')

        # Removing M2M table for field badges on 'Overview'
        db.delete_table(db.shorten_name(u'cmsplugin_overview_badges'))

        # Deleting model 'OverviewBadge'
        db.delete_table(u'parrot_product_overviewbadge')

        # Deleting model 'Packaging'
        db.delete_table(u'cmsplugin_packaging')

        # Removing M2M table for field colors on 'Packaging'
        db.delete_table(db.shorten_name(u'cmsplugin_packaging_colors'))

        # Deleting model 'PackagingColor'
        db.delete_table(u'parrot_product_packagingcolor')

        # Deleting model 'Spec'
        db.delete_table(u'cmsplugin_spec')

        # Deleting model 'Tab'
        db.delete_table(u'cmsplugin_tab')

        # Removing M2M table for field icons on 'Tab'
        db.delete_table(db.shorten_name(u'cmsplugin_tab_icons'))

        # Deleting model 'TabIcon'
        db.delete_table(u'parrot_product_tabicon')

        # Deleting model 'VideoGroup'
        db.delete_table(u'cmsplugin_videogroup')

        # Removing M2M table for field files on 'VideoGroup'
        db.delete_table(db.shorten_name(u'cmsplugin_videogroup_files'))

        # Deleting model 'VideoGroupFile'
        db.delete_table(u'parrot_product_videogroupfile')


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
        u'parrot_product.blurb': {
            'Meta': {'object_name': 'Blurb', 'db_table': "u'cmsplugin_blurb'", '_ormbases': ['cms.CMSPlugin']},
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
            'Meta': {'object_name': 'Overview', 'db_table': "u'cmsplugin_overview'", '_ormbases': ['cms.CMSPlugin']},
            'badges': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['parrot_product.OverviewBadge']", 'symmetrical': 'False'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'htmlid': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'parrot_product.overviewbadge': {
            'Meta': {'object_name': 'OverviewBadge'},
            'admin_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'text': ('djangocms_text_ckeditor.fields.HTMLField', [], {'blank': 'True'}),
            'weighting': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '10'})
        },
        u'parrot_product.packaging': {
            'Meta': {'object_name': 'Packaging', 'db_table': "u'cmsplugin_packaging'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'colors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['parrot_product.PackagingColor']", 'symmetrical': 'False'}),
            'description': ('djangocms_text_ckeditor.fields.HTMLField', [], {}),
            'htmlid': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'news_availability': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'news_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'shop_availability': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'shop_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'parrot_product.packagingcolor': {
            'Meta': {'object_name': 'PackagingColor'},
            'admin_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'hexa': ('project.parrot_product.utils.ColourField', [], {'max_length': '6', 'blank': 'True'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'package': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'weighting': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '10'})
        },
        u'parrot_product.spec': {
            'Meta': {'object_name': 'Spec', 'db_table': "u'cmsplugin_spec'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('djangocms_text_ckeditor.fields.HTMLField', [], {'blank': 'True'}),
            'htmlid': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'parrot_product.tab': {
            'Meta': {'object_name': 'Tab', 'db_table': "u'cmsplugin_tab'", '_ormbases': ['cms.CMSPlugin']},
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
        u'parrot_product.videogroup': {
            'Meta': {'object_name': 'VideoGroup', 'db_table': "u'cmsplugin_videogroup'", '_ormbases': ['cms.CMSPlugin']},
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