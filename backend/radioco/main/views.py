# coding=utf-8
import os
from django.template.loader import get_template
from django.templatetags.static import static
from django.utils.translation import gettext_lazy as _


def _render_flag(context):
    return get_template('main/snippets/elements/flag.html').render((context))


FLAG_IMAGE_PATH = 'main/images/flags/'


def render_gl_flag(**kwargs):
    return _render_flag({'title': _('Galician Language'), 'image': FLAG_IMAGE_PATH + 'gl.png'})


def render_es_flag(**kwargs):
    return _render_flag({'title': _('Spanish Language'), 'image': FLAG_IMAGE_PATH + 'es.png'})


def render_de_flag(**kwargs):
    return _render_flag({'title': _('German Language'), 'image': FLAG_IMAGE_PATH + 'de.png'})


def render_en_flag(**kwargs):
    return _render_flag({'title': _('English Language'), 'image': FLAG_IMAGE_PATH + 'gb.png'})


def render_link(**kwargs):
    return get_template('main/snippets/elements/{}.html'.format(kwargs['type'])).render((kwargs))


def process_timeline_resources(resources, resource_path):
    for resource in resources:
        if resource['type'] == 'flag':
            yield globals()['render_{}_flag'.format(resource['language'])]()
        elif resource['type'] == 'splitter':
            yield '|'
        elif resource['type'] in ('link', 'icon_link'):
            if resource['url'].startswith('/'):
                resource['url'] = static(os.path.join(resource_path, resource['url'][1:]))
            yield render_link(**resource)
        else:
            raise NotImplementedError('Resource of type "{}" not implemented'.format(resource['type']))


def load_yaml_item(data):
    images_path = data.get('images_path', '')
    resources_path = data.get('resources_path', '')
    translatable_fields = data.get('translatable_fields', ())
    for value_item in data['items']:
        item = {}
        for key, value in value_item.items():
            if key in translatable_fields:
                item[key] = _(value)
            elif key == 'image':
                item[key] = os.path.join(images_path, value)
            elif key == 'resources':
                item[key] = process_timeline_resources(value, resources_path)
            else:
                item[key] = value
        yield item
