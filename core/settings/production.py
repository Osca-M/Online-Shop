from .base import *

DEBUG = os.getenv('DEBUG', True)
ALLOWED_HOSTS = ['*']
from decouple import config

# Site admins

ADMINS = (
    ('Osca Mwongera', 'oscamwongera@gmail.com')
)
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('PROD_DB_NAME'),
        'USER': config('PROD_DB_USER'),
        'PASSWORD': config('PROD_DB_PASSWORD'),
        'HOST': config('PROD_DB_HOST'),
        'PORT': config('PROD_DB_PORT')
    }
}
