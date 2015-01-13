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
    module = "Product"
    name = _(u'Product Tab')
    render_template = settings.ONEPAGE_TAB_DEFAULT_TEMPLATE
    raw_id_fields = ('icons',)

    def render(self, context, instance, placeholder):
        self.render_template = instance.template
        context['object_instance'] = instance
        return context


class SpecPlugin(CMSPluginBase):
    model = Spec
    module = "Product"
    name = _(u'Product Spec')
    render_template = settings.ONEPAGE_SPEC_DEFAULT_TEMPLATE

    def render(self, context, instance, placeholder):
        self.render_template = instance.template
        context['object_instance'] = instance
        return context


class BlurbPlugin(CMSPluginBase):
    model = Blurb
    module = "Product"
    name = _(u'Product Blurb')
    render_template = settings.ONEPAGE_BLURB_DEFAULT_TEMPLATE

    def render(self, context, instance, placeholder):
        self.render_template = instance.template
        context['object_instance'] = instance
        return context

class OverviewPlugin(CMSPluginBase):
    model = Overview
    module = "Product"
    name = _(u'Product Overview')
    render_template = settings.ONEPAGE_OVERVIEW_DEFAULT_TEMPLATE
    raw_id_fields = ('badges',)

    def render(self, context, instance, placeholder):
        self.render_template = instance.template
        context['object_instance'] = instance
        return context


class PackagingPlugin(CMSPluginBase):
    model = Packaging
    module = "Product"
    name = _(u'Product Packaging')
    render_template = settings.ONEPAGE_PACK_DEFAULT_TEMPLATE
    raw_id_fields = ('colors',)

    def render(self, context, instance, placeholder):
        self.render_template = instance.template
        context['object_instance'] = instance
        return context


class SubscribePlugin(CMSPluginBase):
    model = Subscribe
    module = "Product"
    name = _(u'Product Subscribe')
    render_template = settings.ONEPAGE_SUBSCRIBE_DEFAULT_TEMPLATE

    def render(self, context, instance, placeholder):
        self.render_template = instance.template
        context['object_instance'] = instance
        return context

class VideoGroupPlugin(CMSPluginBase):
    model = VideoGroup
    module = "Product"
    name = _(u'Product Video Group')
    render_template = settings.ONEPAGE_VIDEO_DEFAULT_TEMPLATE
    raw_id_fields = ('files',)

    def render(self, context, instance, placeholder):
        self.render_template = instance.template
        context['object_instance'] = instance
        return context


class TwentyTwentyPlugin(CMSPluginBase):
    model = TwentyTwenty
    module = "Product"
    name = _(u'Product Twenty Twenty')
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
