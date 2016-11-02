# - *- coding: utf-8 - *-

"""
Django settings for SonidosLibres project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
from pathlib import Path
from django.core.urlresolvers import reverse_lazy
import os

# Utilities
PROJECT_PACKAGE = Path(__file__).resolve().parent.parent

# The full path to the repository root.
BASE_DIR = PROJECT_PACKAGE.parent
PROJECT_ROOT = PROJECT_PACKAGE  # os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y8h#o^ssafs5a80^p99t4!*ridemch6+12m^h9ch+fa)=zm9bs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'contenido.apps.ContenidoConfig',
    'usuarios',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'social.apps.django_app.default',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SonidosLibres.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(PROJECT_PACKAGE.joinpath('templates'))],  # [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Python Social Auth Context Processors
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
                'SonidosLibres.templatetags.extras.admin_media'
            ],
        },
    },
]

WSGI_APPLICATION = 'SonidosLibres.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

# Nombre de la carpeta que crea
STATIC_ROOT = str(PROJECT_ROOT.joinpath('staticfiles'))  # os.path.join(PROJECT_ROOT, 'staticfiles')

# Ruta que apunta los archivos en el front
STATIC_URL = '/static/'

# Carpeta donde se encuentran los archivos estáticos
STATICFILES_DIRS = (
    str(PROJECT_ROOT.joinpath('static')),
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

DATABASES = {
    'default': {}
}

LOGIN_REDIRECT_URL = reverse_lazy('homepage')
LOGOUT_REDIRECT_URL = reverse_lazy('login')

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
}

AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
AWS_SECRET_KEY = os.environ['AWS_SECRET_KEY']
AWS_ACCESS_SECRET_KEY = os.environ['AWS_ACCESS_SECRET_KEY']
MEDIA_URL = "https://%s.s3.amazonaws.com/" % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = ''

EMAIL_BACKEND = "sgbackend.SendGridBackend"
SENDGRID_API_KEY = os.environ['SENDGRID_API_KEY']


AUTHENTICATION_BACKENDS = (
    # Facebook
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    # Django
    'django.contrib.auth.backends.ModelBackend',
)


SOCIAL_AUTH_FACEBOOK_KEY = os.environ['FACEBOOK_KEY']
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ['FACEBOOK_SECRET']
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id,name,email',
}


SOCIAL_AUTH_LOGIN_REDIRECT_URL = "/"

SOCIAL_AUTH_RAISE_EXCEPTIONS = False
