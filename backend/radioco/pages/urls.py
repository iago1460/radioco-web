"""django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.urls import path
from django.utils.text import slugify

from radioco.main.yaml import load_yaml
from radioco.pages.views import YamlView, ArticleView, TranslateRedirectView


urlpatterns = i18n_patterns(
    path('', YamlView.as_view(page_path='index'), name='index'),
    path('installation/', YamlView.as_view(page_path='installation'), name='installation'),
    path('about/', YamlView.as_view(page_path='about'), name='about'),
)


articles = load_yaml(os.path.join(settings.YAML_VIEWS_PATH, 'articles.yml'))
for article in articles:
    urlpatterns.append(
        path(
            '{language}/{url}/'.format(language=article['language'], url=article['url']),
            ArticleView.as_view(article_data=article),
            name=article.get('slug') or slugify(article['url'])
        )
    )


redirects = load_yaml(os.path.join(settings.YAML_VIEWS_PATH, 'redirects.yml'))
for redirect in redirects:
    urlpatterns.append(
        path(
            redirect['from'],
            TranslateRedirectView.as_view(
                permanent=True,
                pattern_name=redirect['to'],
                language=redirect.get('language')
            )
        )
    )
