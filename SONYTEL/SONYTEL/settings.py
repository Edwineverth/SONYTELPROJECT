"""
Django settings for SONYTEL project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*y!4_dhua1k7sg^_9f!3b548*jis^+gl)j)rpdb+q8o9))(7#_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
#SE  TIENE QUE INSTALAR EL UNPATH CON PIP ANTES DE USAR ESTOS METODOS
from unipath import Path 
RUTA_PROYECTO= Path(__file__).ancestor(2)

MEDIA_ROOT =RUTA_PROYECTO.child('media')
#SE HACE REFERENCIA AL ALMACEN DE CARPETAS MEDIA
MEDIA_URL='http://127.0.0.1:8000/media/'
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'aplicacion',
    'bootstrap3',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'SONYTEL.urls'

WSGI_APPLICATION = 'SONYTEL.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

#SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'SONYTELELECTRONIC',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-EC'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=(
    RUTA_PROYECTO.child('static')),
TEMPLATE_DIRS=(
    RUTA_PROYECTO.child('templates')),