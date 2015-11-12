"""
Django settings for IdeaMap project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(a5m#2z6wou!y!8tt_pc5heuk#kf_ah!5-q5pmob#&@x%oq9l%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'rest_framework',
    'rest_framework_gis',
    'require',
    'djcelery',
    'DataViewer',
    'Core',
    'REST_API',
    'Analyzer',
    'Streamer',
)

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

ROOT_URLCONF = 'IdeaMap.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'IdeaMap.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'leet_tweets',
        'USER': 'tweet_is_leet',
        'PASSWORD': 'leet_is_tweet',
        'HOST': 'localhost',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Sets the default login redirect url
LOGIN_REDIRECT_URL = '/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/IdeaMap'
STATICFILES_STORAGE = 'require.storage.OptimizedStaticFilesStorage'
STATICFILES_DIRS = [
    "DataViewer/static/DataViewer/"
]

# Rest Framework Config
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser'
    ]
}

# Require Config
# The baseUrl to pass to the r.js optimizer, relative to STATIC_ROOT.
REQUIRE_BASE_URL = "js"

# The name of a build profile to use for your project, relative to REQUIRE_BASE_URL.
# A sensible value would be 'app.build.js'. Leave blank to use the built-in default build profile.
# Set to False to disable running the default profile (e.g. if only using it to build Standalone
# Modules)
REQUIRE_BUILD_PROFILE = 'app.build.js'

# The name of the require.js script used by your project, relative to REQUIRE_BASE_URL.
REQUIRE_JS = "third-party/require.js"

# A dictionary of standalone modules to build with almond.js.
# See the section on Standalone Modules, below.
REQUIRE_STANDALONE_MODULES = {}

# Whether to run django-require in debug mode.
REQUIRE_DEBUG = DEBUG

# A tuple of files to exclude from the compilation result of r.js.
REQUIRE_EXCLUDE = ("build.txt",)

# The execution environment in which to run r.js: auto, node or rhino.
# auto will autodetect the environment and make use of node if available and rhino if not.
# It can also be a path to a custom class that subclasses require.environments.Environment and defines some "args" function that returns a list with the command arguments to execute.
REQUIRE_ENVIRONMENT = "auto"

# Celery Configuration
BROKER_URL = "amqp://tweet_is_leet:leet_is_tweet@localhost//"
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'
CELERY_POOL_RESTARTS = True
CELERYD_CONCURRENCY = 16

# Analyzer Config
ANALYZER_CACHE_DIR = "/tmp/IdeaMap"
ANALYZER_DATA_DIR = "Analyzer/data"

# Streamer Config
STREAMER_ACCESS_TOKEN = "4010739394-F156dCIH53L1pfstMxF7PlqkmfDJEZJScb0qGAv"
STREAMER_ACCESS_TOKEN_SECRET = "7ZynMAw4hsnmyFfifGl9z8omFKqBRDbCcbhO1rgiqQW51"
STREAMER_CONSUMER_KEY = "NhwzdxzKaBRemgIpnnuZFmyNd"
STREAMER_CONSUMER_SECRET = "EB6OJaK5IGbfXPjMKsk1nRY9GxdgHuEsGZDAKVh0VJubp9iSFO"
STREAMER_LOCATION = [
    -137.8, 21.4,
    -66.5, 51.6
]
