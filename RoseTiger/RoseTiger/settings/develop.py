# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
from .base import *  # NOQA

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

