import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEFAULT_SECRET_KEY = "g*o1@(k*kt@*g4fqwm#%rcyr2-ph0onmx=x_zapw4&oy$1ao@m"
SECRET_KEY = os.getenv('SECRET_KEY', DEFAULT_SECRET_KEY)
DEBUG = True

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django_filters',
    'rest_framework',
    'sil_data_fixtures',
)

LOCAL_APPS = (
    'fhir_valuesets.valuesets',
)
INSTALLED_APPS += LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'fhir_valuesets.configs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = 'fhir_valuesets.configs.wsgi.application'

# Database
DEFAULT_DB = 'postgres://sil:sil@localhost:5432/sil_valuesets'
DATABASES = {
    'default': dj_database_url.config(
        env='DATABASE_URL',
        default=DEFAULT_DB,
        conn_max_age=500)
}

# django-rest framework configs
REST_FRAMEWORK = {
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.AdminRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',
    ),
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
        'fhir_valuesets.valuesets.search.CommonSearchFilter',
    ),
    'PAGE_SIZE': 100,
    'PAGINATE_BY_PARAM': 'page_size',
    'DATETIME_FORMAT': 'iso-8601',
    'DATE_FORMAT': 'iso-8601',
    'TIME_FORMAT': 'iso-8601'
}

# Internationalization
TIME_ZONE = 'Africa/Nairobi'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATICFILES_FINDERS = (
   'django.contrib.staticfiles.finders.FileSystemFinder',
   'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# Issue a http redirect if the request url doesn't have a slash appended
APPEND_SLASH = True

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.getenv('STATIC_ROOT', '')
STATIC_URL = '/static/'
