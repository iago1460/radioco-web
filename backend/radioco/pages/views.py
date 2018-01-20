import os

from django.conf import settings
from django.urls import reverse
from django.utils.translation import activate, deactivate
from django.views.generic import TemplateView, RedirectView

from radioco.main.views import load_yaml_item
from radioco.main.yaml import load_yaml


class YamlView(TemplateView):
    page_path = None

    def __init__(self, *args, **kwargs):
        self.extra_context = YamlView._load_yaml(kwargs['page_path'])
        self.template_name = self.extra_context['template']
        super(YamlView, self).__init__(*args, **kwargs)

    @staticmethod
    def _load_yaml(page_path):
        data = load_yaml(os.path.join(settings.YAML_VIEWS_PATH, page_path, 'context.yml'))
        expanded_data = {key: load_yaml_item(value) for key, value in data.items()}
        expanded_data['template'] = data['template']
        return expanded_data


class ArticleView(TemplateView):
    template_name = 'main/article_base.html'
    article_data = None

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        context.update(self.article_data)
        return context


class TranslateRedirectView(RedirectView):
    """Provide a redirect on any GET request."""
    language = None

    def get_redirect_url(self, *args, **kwargs):
        """
        Return the URL redirect to. Keyword arguments from the URL pattern
        match generating the redirect request are provided as kwargs to this
        method.
        """
        if self.language:
            activate(self.language)
        url = reverse(self.pattern_name, args=args, kwargs=kwargs)
        if self.language:
            deactivate()

        args = self.request.META.get('QUERY_STRING', '')
        if args and self.query_string:
            url = "%s?%s" % (url, args)
        return url
