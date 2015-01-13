from django.conf import settings
from django.db import models
from django.core import urlresolvers
from cms.models.pluginmodel import CMSPlugin
from djangocms_text_ckeditor.fields import HTMLField
from django.utils.translation import ugettext_lazy as _

from paintstore.fields import ColorPickerField

class AbstractCMS(CMSPlugin):
    """
    Abstracted base model for all plugins
    """
    title = models.CharField(_(u'Title'), max_length=200)
    htmlid = models.CharField(_(u'Html ID'), max_length=200)

    def get_admin_url(self):
        return urlresolvers.reverse("admin:%s_%s_change" % (
            self._meta.app_label, self._meta.module_name),
            args=(self.id,)
        )

    def modify(self):
        return _('<a href="%s">Click here to modify</a>') % (self.get_admin_url())
    modify.allow_tags = True

    class Meta:
        abstract = True


class AbstractChildModel(models.Model):
    """
    Abstracted base model for some plugins relations
    """
    admin_name = models.CharField(_(u'Admin Name'), max_length=200)

    def get_admin_url(self):
        return urlresolvers.reverse("admin:%s_%s_change" % (
            self._meta.app_label, self._meta.module_name),
            args=(self.id,)
        )

    def modify(self):
        return '<a href="%s">Click here to modify</a>' % (self.get_admin_url())
    modify.allow_tags = True

    class Meta:
        abstract = True


class Tab(AbstractCMS):
    """
    Tab container for content tabs
    """
    background = models.ImageField(_(u'background'), upload_to='product_onepage', blank=True)
    icons = models.ManyToManyField('TabIcon', verbose_name=_(u'icons'))
    template = models.CharField(_('template'), choices=settings.ONEPAGE_TAB_TEMPLATE_CHOICES, default=ONEPAGE_TAB_DEFAULT_TEMPLATE, max_length=100, blank=False)

    def copy_relations(self, oldinstance):
        self.icons = oldinstance.icons.all()

    def __unicode__(self):
        return 'Tab %s' % (self.title)


class TabIcon(AbstractChildModel):
    """
    Tab content element
    """
    title = models.CharField(_(u'Title'), max_length=200)
    text = HTMLField(_(u'Text'), blank=True)
    background = models.ImageField(_(u'background'), upload_to='product_onepage', blank=True)
    passive_image = models.ImageField(_(u'Passive Image'), upload_to='product_onepage')
    active_image = models.ImageField(_(u'Active Image'), upload_to='product_onepage', blank=True)
    weighting = models.IntegerField(_(u'Weighting'), max_length=10, default=0)

    def __unicode__(self):
        return '%s' % (self.admin_name)


class Spec(AbstractCMS):
    """
    Specifications content
    """
    ALIGNMENT_CHOICES = settings.ONEPAGE_SPEC_ALIGNMENT_CHOICES
    
    alignment = models.CharField(_(u'Text Alignment'), max_length=20, choices=settings.ONEPAGE_SPEC_ALIGNMENT_CHOICES, default='left')
    image = models.ImageField(_(u'Image'), upload_to='product_onepage', blank=True)
    description = HTMLField(_(u'Text'), blank=True)
    template = models.CharField(_('template'), choices=settings.ONEPAGE_SPEC_TEMPLATE_CHOICES, default=ONEPAGE_SPEC_DEFAULT_TEMPLATE, max_length=100, blank=False)

    def __unicode__(self):
        return 'Spec %s' % (self.title)


class Blurb(AbstractCMS):
    """
    Blurb content for some feature/production introduction
    """
    ALIGNMENT_CHOICES = settings.ONEPAGE_BLURB_ALIGNMENT_CHOICES
    
    background = models.ImageField(_(u'Background'), upload_to='product_onepage')
    mobile = models.ImageField(_(u'Mobile'), upload_to='product_onepage', blank=True)
    logo = models.ImageField(_(u'Logo'), upload_to='product_onepage', blank=True)
    description = HTMLField(_(u'Text'))
    button = models.CharField(_(u'Button'), max_length=200, blank=True)
    url = models.URLField(_(u'URL'), max_length=200, blank=True)
    alignment = models.CharField(_(u'Text Alignment'), max_length=20, choices=settings.ONEPAGE_BLURB_ALIGNMENT_CHOICES, default='centered')
    template = models.CharField(_('template'), choices=settings.ONEPAGE_BLURB_TEMPLATE_CHOICES, default=ONEPAGE_BLURB_DEFAULT_TEMPLATE, max_length=100, blank=False)

    def __unicode__(self):
        return 'Blurb %s' % (self.title)


class Overview(AbstractCMS):
    """
    Overview container for some badges
    """
    badges = models.ManyToManyField('OverviewBadge', verbose_name=_(u'badges'))
    template = models.CharField(_('template'), choices=settings.ONEPAGE_OVERVIEW_TEMPLATE_CHOICES, default=ONEPAGE_OVERVIEW_DEFAULT_TEMPLATE, max_length=100, blank=False)

    def copy_relations(self, oldinstance):
        self.badges = oldinstance.badges.all()

    def __unicode__(self):
        return 'Overview %s' % (self.title)


class OverviewBadge(AbstractChildModel):
    """
    Badge item for Overviews
    """
    image = models.ImageField(_(u'Image'), upload_to='product_onepage')
    text = HTMLField(_(u'Text'))
    weighting = models.IntegerField(_(u'Weighting'), max_length=10, default=0)

    def __unicode__(self):
        return '%s' % (self.admin_name)


class AbstractPackaging(AbstractCMS):
    """
    Product packaging
    """
    colors = models.ManyToManyField('PackagingColor', verbose_name=_(u'colors'))
    logo = models.ImageField(_(u'Logo'), upload_to='product_onepage')
    description = HTMLField(_(u'Description'))
    shop_url = models.URLField(_(u'Shop URL'), max_length=200, blank=True)
    shop_availability = models.BooleanField(_(u'Has shop'))
    news_availability = models.BooleanField(_(u'Has News'))
    template = models.CharField(_('template'), choices=settings.ONEPAGE_PACK_TEMPLATE_CHOICES, default=ONEPAGE_PACK_DEFAULT_TEMPLATE, max_length=100, blank=False)

    def __unicode__(self):
        return 'Packaging %s' % (self.title)

    def copy_relations(self, oldinstance):
        self.colors = oldinstance.colors.all()

    class Meta:
        abstract = True

# Packaging plugin fields is conditionnated to the mcrm app
try:
    from project.mcrm.models import Category
except ImportError:
    class Packaging(AbstractPackaging):
        news_slug = models.CharField(_(u'News Slug'), max_length=50, blank=True)
else:
    class Packaging(AbstractPackaging):
        news_slug = models.ForeignKey(Category, blank=True)


class PackagingColor(AbstractChildModel):
    """
    Color item for Packagings
    """
    package = models.ImageField(_(u'Package'), upload_to='product_onepage')
    hexa = ColorPickerField(_(u'Hexa'), blank=True)
    icon = models.ImageField(_(u'Icon'), upload_to='product_onepage', blank=True)
    weighting = models.IntegerField(_(u'Weighting'), max_length=10, default=0)

    def __unicode__(self):
        return '%s' % (self.admin_name)


class AbstractSubscribe(AbstractCMS):
    """
    Subscribe element to contain a subscription form
    """
    message = HTMLField(_(u'Text'))
    template = models.CharField(_('template'), choices=settings.ONEPAGE_SUBSCRIBE_TEMPLATE_CHOICES, default=ONEPAGE_SUBSCRIBE_DEFAULT_TEMPLATE, max_length=100, blank=False)

    def __unicode__(self):
        return 'Subscribe %s' % (self.title)

    class Meta:
        abstract = True

# Subscribe plugin fields is conditionnated to the mcrm app
try:
    from project.mcrm.models import Category
except ImportError:
    class Subscribe(AbstractSubscribe):
        subscribe_to = models.CharField(_(u'Subscribe to'), max_length=50, blank=True)
else:
    class Subscribe(AbstractSubscribe):
        subscribe_to = models.ForeignKey(Category, blank=True)


class VideoGroup(AbstractCMS):
    """
    Video group container
    """
    files = models.ManyToManyField('VideoGroupFile', verbose_name=_(u'files'))
    background = models.ImageField(_(u'Background'), upload_to='product_onepage')
    template = models.CharField(_('template'), choices=settings.ONEPAGE_VIDEO_TEMPLATE_CHOICES, default=ONEPAGE_VIDEO_DEFAULT_TEMPLATE, max_length=100, blank=False)

    def copy_relations(self, oldinstance):
        self.files = oldinstance.files.all()

    def __unicode__(self):
        return 'VideoGroup %s' % (self.title)

class VideoGroupFile(AbstractChildModel):
    """
    Video element for VideoGroups
    """
    title = models.CharField(_(u'Title'), max_length=200)
    url = models.URLField(_(u'URL'), max_length=200)
    image = models.ImageField(_(u'Image'), upload_to='product_onepage', blank=True)
    weighting = models.IntegerField(_(u'Weighting'), max_length=10, default=0)

    def __unicode__(self):
        return '%s' % (self.admin_name)


class TwentyTwenty(AbstractCMS):
    """
    TwentyTwenty content to use the TwentyTwenty library that merge two images 
    in divided slider to visually compare them
    """
    left_legend = models.CharField(_(u'Left Legend'), max_length=200, blank=True)
    left_image = models.ImageField(_(u'Left Image'), upload_to='product_onepage')
    right_legend = models.CharField(_(u'Right Legend'), max_length=200, blank=True)
    right_image = models.ImageField(_(u'Right Image'), upload_to='product_onepage')
    description = HTMLField(_(u'Text'))
    template = models.CharField(_('template'), choices=settings.ONEPAGE_TWENTYTWENTY_TEMPLATE_CHOICES, default=ONEPAGE_TWENTYTWENTY_DEFAULT_TEMPLATE, max_length=100, blank=False)

    def __unicode__(self):
        return 'TwentyTwenty %s' % (self.title)
