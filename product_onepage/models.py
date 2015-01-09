from django.db import models
from django.core import urlresolvers
from cms.models.pluginmodel import CMSPlugin
from djangocms_text_ckeditor.fields import HTMLField
from django.utils.translation import ugettext_lazy as _

from paintstore.fields import ColorPickerField


# Abstract Models
class AbstractCMS(CMSPlugin):
    title = models.CharField(_(u'Title'), max_length=200)
    htmlid = models.CharField(_(u'Html ID'), max_length=200)

    def get_admin_url(self):
        return urlresolvers.reverse("admin:%s_%s_change" % (
            self._meta.app_label, self._meta.module_name), args=(self.id,))

    def modify(self):
        return '<a href="%s">Click here to modify</a>' % (self.get_admin_url())
    modify.allow_tags = True

    class Meta:
        abstract = True


class AbstractChildModel(models.Model):
    admin_name = models.CharField(_(u'Admin Name'), max_length=200)

    def get_admin_url(self):
        return urlresolvers.reverse("admin:%s_%s_change" % (
            self._meta.app_label, self._meta.module_name), args=(self.id,))

    def modify(self):
        return '<a href="%s">Click here to modify</a>' % (self.get_admin_url())
    modify.allow_tags = True

    class Meta:
        abstract = True


# Blurb Plugin
class Blurb(AbstractCMS):
    ALIGNMENT_CHOICES = (
        ('1', _(u'Extreme Left')),
        ('3', _(u'Left')),
        ('centered', _(u'Center')),
        ('6', _(u'Right')),
        ('8', _(u'Extreme Right')),
    )
    background = models.ImageField(_(u'Background'),
                                   upload_to='parrot_product/gallery')
    mobile = models.ImageField(_(u'Mobile'),
                               upload_to='parrot_product/gallery', blank=True)
    logo = models.ImageField(_(u'Logo'),
                             upload_to='parrot_product/gallery', blank=True)
    description = HTMLField(_(u'Text'))
    button = models.CharField(_(u'Button'), max_length=200, blank=True)
    url = models.URLField(_(u'URL'), max_length=200, blank=True)
    alignment = models.CharField(_(u'Text Alignment'), max_length=20,
                                 choices=ALIGNMENT_CHOICES, default='centered')

    def __unicode__(self):
        return 'Blurb %s' % (self.title)


# Overview Plugin
class Overview(AbstractCMS):
    badges = models.ManyToManyField('OverviewBadge', verbose_name=_(u'badges'))

    def copy_relations(self, oldinstance):
        self.badges = oldinstance.badges.all()

    def __unicode__(self):
        return 'Overview %s' % (self.title)


class OverviewBadge(AbstractChildModel):
    image = models.ImageField(_(u'Image'),
                              upload_to='parrot_product/gallery')
    text = HTMLField(_(u'Text'))
    weighting = models.IntegerField(_(u'Weighting'), max_length=10, default=0)

    def __unicode__(self):
        return '%s' % (self.admin_name)


# Packaging Plugin

class AbstractPackaging(AbstractCMS):
    colors = models.ManyToManyField('PackagingColor',
                                    verbose_name=_(u'colors'))
    logo = models.ImageField(_(u'Logo'), upload_to='parrot_product/gallery')
    description = HTMLField(_(u'Description'))
    shop_url = models.URLField(_(u'Shop URL'), max_length=200, blank=True)
    shop_availability = models.BooleanField(_(u'Has shop'))
    news_availability = models.BooleanField(_(u'Has News'))

    def __unicode__(self):
        return 'Packaging %s' % (self.title)

    def copy_relations(self, oldinstance):
        self.colors = oldinstance.colors.all()

    class Meta:
        abstract = True


try:
    from project.mcrm.models import Category
except ImportError:
    class Packaging(AbstractPackaging):
        news_slug = models.CharField(
            _(u'News Slug'), max_length=50, blank=True)
else:
    class Packaging(AbstractPackaging):
        news_slug = models.ForeignKey(Category, blank=True)


class PackagingColor(AbstractChildModel):
    package = models.ImageField(_(u'Package'),
                                upload_to='parrot_product/gallery')
    hexa = ColorPickerField(_(u'Hexa'), blank=True)
    icon = models.ImageField(_(u'Icon'),
                             upload_to='parrot_product/gallery', blank=True)
    weighting = models.IntegerField(_(u'Weighting'), max_length=10, default=0)

    def __unicode__(self):
        return '%s' % (self.admin_name)


# Spec Plugin
class Spec(AbstractCMS):
    ALIGNMENT_CHOICES = (
        ('left', _(u'Left')),
        ('right', _(u'Right')),
    )
    alignment = models.CharField(_(u'Text Alignment'), max_length=20,
                                 choices=ALIGNMENT_CHOICES, default='left')
    image = models.ImageField(_(u'Image'),
                              upload_to='parrot_product/gallery', blank=True)
    description = HTMLField(_(u'Text'), blank=True)

    def __unicode__(self):
        return 'Spec %s' % (self.title)


# Tab Plugin
class Tab(AbstractCMS):
    background = models.ImageField(_(u'background'),
                                   upload_to='parrot_product/gallery',
                                   blank=True)
    icons = models.ManyToManyField('TabIcon',
                                   verbose_name=_(u'icons'))

    def copy_relations(self, oldinstance):
        self.icons = oldinstance.icons.all()

    def __unicode__(self):
        return 'Tab %s' % (self.title)


class TabIcon(AbstractChildModel):
    title = models.CharField(_(u'Title'), max_length=200)
    text = HTMLField(_(u'Text'), blank=True)
    background = models.ImageField(_(u'background'),
                                   upload_to='parrot_product/gallery',
                                   blank=True)
    passive_image = models.ImageField(_(u'Passive Image'),
                                      upload_to='parrot_product/gallery')
    active_image = models.ImageField(_(u'Active Image'),
                                     upload_to='parrot_product/gallery',
                                     blank=True)
    weighting = models.IntegerField(_(u'Weighting'), max_length=10, default=0)

    def __unicode__(self):
        return '%s' % (self.admin_name)


# VideoGroup Plugin
class VideoGroup(AbstractCMS):
    files = models.ManyToManyField('VideoGroupFile',
                                   verbose_name=_(u'files'))
    background = models.ImageField(_(u'Background'),
                                   upload_to='parrot_product/gallery')

    def copy_relations(self, oldinstance):
        self.files = oldinstance.files.all()

    def __unicode__(self):
        return 'VideoGroup %s' % (self.title)


class VideoGroupFile(AbstractChildModel):
    title = models.CharField(_(u'Title'), max_length=200)
    url = models.URLField(_(u'URL'), max_length=200)
    image = models.ImageField(_(u'Image'),
                              upload_to='parrot_product/gallery', blank=True)
    weighting = models.IntegerField(_(u'Weighting'), max_length=10, default=0)

    def __unicode__(self):
        return '%s' % (self.admin_name)


# TwentyTwenty Plugin
class TwentyTwenty(AbstractCMS):
    left_legend = models.CharField(_(u'Left Legend'),
                                   max_length=200, blank=True)
    left_image = models.ImageField(_(u'Left Image'),
                                   upload_to='parrot_product/gallery')
    right_legend = models.CharField(_(u'Right Legend'),
                                    max_length=200, blank=True)
    right_image = models.ImageField(_(u'Right Image'),
                                    upload_to='parrot_product/gallery')
    description = HTMLField(_(u'Text'))

    def __unicode__(self):
        return 'TwentyTwenty %s' % (self.title)


# Subscribe Plugin
class AbstractSubscribe(AbstractCMS):
    message = HTMLField(_(u'Text'))

    def __unicode__(self):
        return 'Subscribe %s' % (self.title)

    class Meta:
        abstract = True


try:
    from project.mcrm.models import Category
except ImportError:
    class Subscribe(AbstractSubscribe):
        subscribe_to = models.CharField(
            _(u'Subscribe to'), max_length=50, blank=True)
else:
    class Subscribe(AbstractSubscribe):
        subscribe_to = models.ForeignKey(Category, blank=True)
