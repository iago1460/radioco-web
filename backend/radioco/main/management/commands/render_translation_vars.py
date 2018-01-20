import os
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from radioco.main.yaml import load_yaml


class Command(BaseCommand):
    help = 'Render yaml translatable fields into html to allow django to find it'

    def handle(self, *args, **options):
        for root, dirs, files in os.walk(settings.YAML_VIEWS_PATH, topdown=True):
            for name in files:
                if name.endswith('.yml'):
                    file_path = os.path.join(root, name)
                    folder_name = file_path.split('/')[-2]
                    file_name = name.replace('.yml', '.html')
                    destination = os.path.join(settings.LOCALE_PRERENDER_PATH, folder_name, file_name)
                    create_translation_file(file_path, destination)
                    self.stdout.write(self.style.SUCCESS(f'Successfully processed {name}'.format(name=name)))


def create_directory(destination):
    os.makedirs(os.path.dirname(destination), exist_ok=True)


def create_translation_file(source, destination):
    data = load_yaml(source)
    if isinstance(data, dict) and data.get('translatable_fields') and data.get('items'):
        create_directory(destination)
        translatable_fields = data.get('translatable_fields')
        with open(destination, 'w+') as file_:
            file_.write('{% load i18n %}\n')
            for item in data['items']:
                for key, value in item.items():
                    if key in translatable_fields:
                        file_.write('{% blocktrans %}' + value + '{% endblocktrans %}\n')
