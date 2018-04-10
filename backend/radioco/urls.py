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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import URLResolver
from django.urls import path, reverse
from django.views.generic import TemplateView

from radioco.pages.urls import urlpatterns as page_urls

urlpatterns = []
urlpatterns.extend(page_urls)


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'
    i18n = True
    excluded_views = (
        'django.contrib.sitemaps.views.sitemap',
    )
    important_views = (
        'index', 'installation', 'about',
    )

    def _get_items(self):
        for url in urlpatterns:
            if isinstance(url, URLResolver):
                yield from urlpatterns[0].url_patterns
            yield url

    def priority(self, item):
        return 1 if item in self.important_views else 0.8

    def items(self):
        return list(filter(
            lambda x: x is not None and x not in self.excluded_views,
            [getattr(url, 'name', None) for url in self._get_items()])
        )

    def location(self, item):
        return reverse(item)


urlpatterns.extend(
    (
        path(
            'sitemap.xml',
            sitemap,
            {'sitemaps': {'static': StaticViewSitemap}},
            name='django.contrib.sitemaps.views.sitemap'
        ),
        path('robots.txt', TemplateView.as_view(template_name="main/robots.txt", content_type="text/plain"))
    )
)


if settings.DEBUG:
    # Media
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Static
    urlpatterns += staticfiles_urlpatterns()
