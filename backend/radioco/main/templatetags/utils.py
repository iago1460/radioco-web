from django import template
from django.urls import translate_url as django_translate_url, reverse
from django.utils import translation

register = template.Library()


@register.simple_tag(takes_context=True)
def translate_url(context, lang_code):
    result_url = django_translate_url(context['request'].path, lang_code)
    if not result_url.startswith('/{}/'.format(lang_code)):
        # url is not available in the requested language
        translation.activate(lang_code)
        result_url = reverse('index')
        translation.deactivate()
    return result_url
