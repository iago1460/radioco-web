"""
Django settings for django project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os


def str_to_bool(text):
    return str(text).lower() not in ('none', 'false', 'no', '0')


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_DIR = BASE_DIR


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'afddnzczb^tmq9pf9sst6k((4&4h-6)h+_6ku(ww%!hkrsjp5i)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = str_to_bool(os.environ.get('DEBUG'))
if not DEBUG:
    ALLOWED_HOSTS = ['.radioco.org', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'radioco.main'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'radioco.main.middleware.HTMLMinifyMiddleware',
]

ROOT_URLCONF = 'radioco.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': (
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ),
        },
    },
]

WSGI_APPLICATION = 'radioco.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Logging https://docs.djangoproject.com/en/2.0/topics/logging/

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}


# Available Languages
gettext_noop = lambda s: s
LANGUAGES = (
    ('es', gettext_noop('Spanish')),
    ('en', gettext_noop('English')),
)


LOCALE_PATHS = (
    os.path.join(SITE_DIR, 'locale'),
)

LOCALE_PRERENDER_PATH = os.path.join(BASE_DIR, 'radioco/main/templates/tmp_translations/')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(SITE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(SITE_DIR, 'media')

# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder'
# )

# STATICFILES_DIRS = (
#     ("main", os.path.join(SITE_DIR, 'radioco/main/static/main')),
# )

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}




YAML_VIEWS_PATH = os.path.join(BASE_DIR, 'radioco/pages/views/')

# Import local settings
try:
    from .local_settings import *
except ImportError:
    pass


if not DEBUG:
    # Enabling cache
    MIDDLEWARE = [
        'django.middleware.cache.UpdateCacheMiddleware', # First
        *MIDDLEWARE,
        'django.middleware.cache.FetchFromCacheMiddleware' # Last
    ]
    CACHE_MIDDLEWARE_SECONDS = 60 * 60 * 24  # 1 day
    TEMPLATES[0]['OPTIONS']['loaders'] = [('django.template.loaders.cached.Loader', TEMPLATES[0]['OPTIONS']['loaders'])]
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'unique-snowflake',
        }
    }