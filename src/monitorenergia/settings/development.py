import os
from monitorenergia.settings.base import *

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DB_HOST = os.environ.get('POSTGRES_PASSWORD')
DB_PORT = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_NAME = os.environ.get('POSTGRES_NAME')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': POSTGRES_NAME,
        'USER': POSTGRES_USER,
        'PASSWORD': POSTGRES_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT
    }
}

ALLOWED_HOSTS = ['localhost']
