from .base import *

DEBUG = os.getenv('DEBUG', True)

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
