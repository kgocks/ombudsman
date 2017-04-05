from ombudsman.settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECURE_SSL_REDIRECT = False
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ALLOWED_HOSTS.append("localhost")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ombudsman',
        'USER': 'ben',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
MIDDLEWARE.remove('rollbar.contrib.django.middleware.RollbarNotifierMiddleware')
