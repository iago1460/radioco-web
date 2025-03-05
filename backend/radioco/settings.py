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


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = str_to_bool(os.environ.get('DEBUG'))
if not DEBUG:
    ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", ".radioco.org,localhost,127.0.0.1,[::1]").split(",")

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'corsheaders',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    "compressor",
    "csp",
    'radioco.main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'radioco.main.middleware.HTMLMinifyMiddleware',
    'csp.middleware.CSPMiddleware',
]
from csp.constants import NONE, SELF, UNSAFE_INLINE, UNSAFE_EVAL

CONTENT_SECURITY_POLICY = {
    "EXCLUDE_URL_PREFIXES": ["/excluded-path/"],
    "DIRECTIVES": {
        "default-src": [NONE],
        "script-src": [
            SELF, 
            UNSAFE_INLINE, 
            UNSAFE_EVAL,
            "https://code.jquery.com",
            "https://cdn.jsdelivr.net",
            "https://use.fontawesome.com",
            "https://maxcdn.bootstrapcdn.com",
        ],
        "style-src": [
            SELF, 
            UNSAFE_INLINE,
            "https://fonts.googleapis.com",
            "https://maxcdn.bootstrapcdn.com",
        ],
        "font-src": [
            SELF,
            "https://fonts.gstatic.com",
            "https://maxcdn.bootstrapcdn.com",
            "https://use.fontawesome.com",
        ],
        "img-src": [SELF, "data:"],
    },
}

CORS_ALLOWED_ORIGINS = [
    "https://radioco.org",
    "https://www.radioco.org",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
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

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Compressor settings
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_OUTPUT_DIR = 'MIN'


COMPRESS_STORAGE = 'compressor.storage.BrotliCompressorFileStorage'
WHITENOISE_MAX_AGE = 31536000 
WHITENOISE_MIMETYPES = {
    '.css': 'text/css',
}

# WhiteNoise should come before compressor to serve compressed files
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    }
}

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# STATICFILES_DIRS = (
#     ("main", os.path.join(SITE_DIR, 'radioco/main/static/main')),
# )



YAML_VIEWS_PATH = os.path.join(BASE_DIR, 'radioco/pages/views/')

# Import local settings
# try:
#     from .local_settings import *
# except ImportError:
#     pass


if not DEBUG:
    # Enabling cache
    MIDDLEWARE = [
        # 'django.middleware.cache.UpdateCacheMiddleware', # First
        *MIDDLEWARE,
        # 'django.middleware.cache.FetchFromCacheMiddleware' # Last
    ]
    CACHE_MIDDLEWARE_SECONDS = 60 * 60 * 24  # 1 day
    TEMPLATES[0]['OPTIONS']['loaders'] = [('django.template.loaders.cached.Loader', TEMPLATES[0]['OPTIONS']['loaders'])]
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'unique-snowflake',
        }
    }
    
    # HTTPS settings
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_BROWSER_XSS_FILTER = True
