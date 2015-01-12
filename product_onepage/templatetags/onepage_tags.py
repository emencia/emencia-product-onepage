"""Gallery templatetags"""
from django.template import Library
from django.core.exceptions import ObjectDoesNotExist

register = Library()


@register.filter(name='divide')
def divide(dividend, divisor):
    return dividend / divisor


@register.filter(name='get_language')
def get_language(queryset, language):
    try:
        return queryset.get(language=language)
    except ObjectDoesNotExist:
        try:
            return queryset.get(language='en')
        except ObjectDoesNotExist:
            return queryset.all()[0]
