from .base import *

DEBUG = False

from decouple import config

# Site admins

ADMINS = (
    ('Osca Mwongera', 'oscamwongera@gmail.com')
)
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': config('PROD_DB_NAME'),
        'USER': config('PROD_DB_USER'),
        'PASSWORD': config('PROD_DB_PASSWORD'),
        'HOST': config('PROD_DB_HOST'),
        'PORT': config('PROD_DB_PORT')
    }
}

# from .base import *
#
# DEBUG = True
#
# ALLOWED_HOSTS = ['*']
#
# from .base import *
#
# DEBUG = False
#
# ALLOWED_HOSTS = ['192.168.214.91']
#
# DATABASES = {
#         'default': {
#                 'ENGINE': 'django.contrib.gis.db.backends.postgis',
#                 'NAME': 'backend_test',
#                 'USER': 'situma',
#                 'PASSWORD': 'mercury',
#                 'OPTIONS': {
#                     'options': '-c search_path=public'
#                 },
#                 'HOST': '192.168.214.137',
#                 'PORT': '5432',
#                 'TEST': {
#                         'ENGINE': 'django.contrib.gis.db.backends.postgis',
#                         'NAME': 'backend_test',
#                         'USER': 'situma',
#                         'PASSWORD': 'mercury',
#                         'OPTIONS': {
#                             'options': '-c search_path=situma_test'
#                         },
#                 },
#         }
# }

