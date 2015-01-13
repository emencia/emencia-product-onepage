from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _

from .models import (
    Tab,
    Spec,
    Blurb,
    Overview,
    Packaging,
    Subscribe,
    VideoGroup,
    TwentyTwenty,
)


class TabPlugin(CMSPluginBase):
    model = Tab
    module = _("Product Onepage")
    name = _(u'Tab')
    render_template = settings.ONEPAGE_TAB_DEFAULT_TEMPLATE
    raw_id_fields = ('icons',)

    def render(self, context, instance, placeholder):
        self.render_template = instance.template
        context['object_instance'] = instance
        return context


class SpecPlugin(CMSPluginBase):
    model = Spec
    module = _("Product Onepage")
    name = _(u'Spec')
    render_template = settings.ONEPAGE_SPEC_DEFAULT_TEMPLATE

    def render(self, context, instance, placeholder):
        self.render_template = instance.template
        context['object_instance'] = instance
        return context


class BlurbPlugin(CMSPluginBase):
    model = Blurb
    module = _("Product Onepage")
    name = _(u'Blurb')
    render_template = settings.ONEPAGE_BLURB_DEFAULT_TEMPLATE

    def render(self, context, instance, placeholder):
        self.render_template = instance.template
        context['object_instance'] = instance
        return context

class OverviewPlugin(CMSPluginBase):
    model = Overview
    module = _("Product Onepage")
    name = _(u'Overview')
    render_template = settings.ONEPAGE_OVERVIEW_DEFAULT_TEMPLATE
    raw_id_fields = ('badges',)

    def render(self, context, instance, placeholder):
        self.render_template = instance.template
        context['object_instance'] = instance
        return context


class PackagingPlugin(CMSPluginBase):
    model = Packaging
    module = _("Product Onepage")
    name = _(u'Packaging')
    render_template = settings.ONEPAGE_PACK_DEFAULT_TEMPLATE
    raw_id_fields = ('colors',)

    def render(self, context, instance, placeholder):
        self.render_template = instance.template
        context['object_instance'] = instance
        return context


class SubscribePlugin(CMSPluginBase):
    model = Subscribe
    module = _("Product Onepage")
    name = _(u'Subscribe')
    render_template = settings.ONEPAGE_SUBSCRIBE_DEFAULT_TEMPLATE

    def render(self, context, instance, placeholder):
        self.render_template = instance.template
        context['object_instance'] = instance
        return context

class VideoGroupPlugin(CMSPluginBase):
    model = VideoGroup
    module = _("Product Onepage")
    name = _(u'Video Group')
    render_template = settings.ONEPAGE_VIDEO_DEFAULT_TEMPLATE
    raw_id_fields = ('files',)

    def render(self, context, instance, placeholder):
        self.render_template = instance.template
        context['object_instance'] = instance
        return context


class TwentyTwentyPlugin(CMSPluginBase):
    model = TwentyTwenty
    module = _("Product Onepage")
    name = _(u'Twenty Twenty')
    render_template = settings.ONEPAGE_TWENTYTWENTY_DEFAULT_TEMPLATE

    def render(self, context, instance, placeholder):
        self.render_template = instance.template
        context['object_instance'] = instance
        return context


plugin_pool.register_plugin(TabPlugin)
plugin_pool.register_plugin(SpecPlugin)
plugin_pool.register_plugin(BlurbPlugin)
plugin_pool.register_plugin(OverviewPlugin)
plugin_pool.register_plugin(SubscribePlugin)
plugin_pool.register_plugin(PackagingPlugin)
plugin_pool.register_plugin(VideoGroupPlugin)
plugin_pool.register_plugin(TwentyTwentyPlugin)
