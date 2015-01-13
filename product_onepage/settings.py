# Dummy gettext
gettext = lambda s: s

# Plugins template choices
ONEPAGE_TAB_TEMPLATE_CHOICES = (
    ("product_onepage/tab.html", gettext("Default")),
)

ONEPAGE_SPEC_TEMPLATE_CHOICES = (
    ("product_onepage/spec.html", gettext("Default")),
)

ONEPAGE_BLURB_TEMPLATE_CHOICES = (
    ("product_onepage/blurb.html", gettext("Default")),
)

ONEPAGE_OVERVIEW_TEMPLATE_CHOICES = (
    ("product_onepage/overview.html", gettext("Default")),
)

ONEPAGE_PACK_TEMPLATE_CHOICES = (
    ("product_onepage/pack.html", gettext("Default")),
)

ONEPAGE_SUBSCRIBE_TEMPLATE_CHOICES = (
    ("product_onepage/subscribe.html", gettext("Default")),
)

ONEPAGE_VIDEO_TEMPLATE_CHOICES = (
    ("product_onepage/video.html", gettext("Default")),
)

ONEPAGE_TWENTYTWENTY_TEMPLATE_CHOICES = (
    ("product_onepage/twentytwenty.html", gettext("Default")),
)

# Plugins templates default choice
ONEPAGE_TAB_DEFAULT_TEMPLATE = ONEPAGE_TAB_TEMPLATE_CHOICES[0][0]
ONEPAGE_SPEC_DEFAULT_TEMPLATE = ONEPAGE_SPEC_TEMPLATE_CHOICES[0][0]
ONEPAGE_BLURB_DEFAULT_TEMPLATE = ONEPAGE_BLURB_TEMPLATE_CHOICES[0][0]
ONEPAGE_OVERVIEW_DEFAULT_TEMPLATE = ONEPAGE_OVERVIEW_TEMPLATE_CHOICES[0][0]
ONEPAGE_PACK_DEFAULT_TEMPLATE = ONEPAGE_PACK_TEMPLATE_CHOICES[0][0]
ONEPAGE_SUBSCRIBE_DEFAULT_TEMPLATE = ONEPAGE_SUBSCRIBE_TEMPLATE_CHOICES[0][0]
ONEPAGE_VIDEO_DEFAULT_TEMPLATE = ONEPAGE_VIDEO_TEMPLATE_CHOICES[0][0]
ONEPAGE_TWENTYTWENTY_DEFAULT_TEMPLATE = ONEPAGE_TWENTYTWENTY_TEMPLATE_CHOICES[0][0]


# Alignement options
ONEPAGE_BLURB_ALIGNMENT_CHOICES = (
    ('1', gettext(u'Extreme Left')),
    ('3', gettext(u'Left')),
    ('centered', gettext(u'Center')),
    ('6', gettext(u'Right')),
    ('8', gettext(u'Extreme Right')),
)

ONEPAGE_SPEC_ALIGNMENT_CHOICES = (
    ('left', _(u'Left')),
    ('right', _(u'Right')),
)
