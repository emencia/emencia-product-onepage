from django.contrib import admin

from .models import (
    Tab,
    Spec,
    Blurb,
    TabIcon,
    Overview,
    Packaging,
    Subscribe,
    VideoGroup,
    TwentyTwenty,
    OverviewBadge,
    PackagingColor,
    VideoGroupFile,
)


class AbstractChildModelAdmin(admin.ModelAdmin):
    search_fields = ('admin_name', 'id')
    list_display = ('admin_name', 'id', 'modify')

    class Meta:
        abstract = True


class AbstractCMSModelAdmin(admin.ModelAdmin):
    search_fields = ('admin_name', 'id')
    list_display = ('title', 'id', 'modify')

    class Meta:
        abstract = True


class TabAdmin(AbstractCMSModelAdmin):
    raw_id_fields = ('icons',)


class OverviewAdmin(AbstractCMSModelAdmin):
    raw_id_fields = ('badges',)


class PackagingAdmin(AbstractCMSModelAdmin):
    raw_id_fields = ('colors',)


class VideoGroupAdmin(AbstractCMSModelAdmin):
    raw_id_fields = ('files',)


admin.site.register(Tab, TabAdmin)
admin.site.register(Overview, OverviewAdmin)
admin.site.register(Packaging, PackagingAdmin)
admin.site.register(VideoGroup, VideoGroupAdmin)
admin.site.register(Spec, AbstractCMSModelAdmin)
admin.site.register(Blurb, AbstractCMSModelAdmin)
admin.site.register(Subscribe, AbstractCMSModelAdmin)
admin.site.register(TabIcon, AbstractChildModelAdmin)
admin.site.register(TwentyTwenty, AbstractCMSModelAdmin)
admin.site.register(OverviewBadge, AbstractChildModelAdmin)
admin.site.register(PackagingColor, AbstractChildModelAdmin)
admin.site.register(VideoGroupFile, AbstractChildModelAdmin)
