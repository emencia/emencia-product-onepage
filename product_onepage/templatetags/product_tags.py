"""Gallery templatetags"""
from django.template import Library
from django.core.exceptions import ObjectDoesNotExist

register = Library()


@register.filter(name='divide')
def divide(dividend, divisor):
    return dividend / divisor


@register.filter(name='get_language')
def get_language(list, language):
    try:
        return list.get(language=language)
    except ObjectDoesNotExist:
        try:
            return list.get(language='en')
        except ObjectDoesNotExist:
            return list.all()[0]
