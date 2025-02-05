import os
from .settings import *
from .settings import BASE_DIR



ALLOWED_HOSTS = ['gumption-dev-hmbferejfsd2c8ct.canadacentral-01.azurewebsites.net']
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']]
DEBUG = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

connection_string = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
params = {pair.split('='):pair.split('=')[1] for pair in connection_string.split(' ')}

DATABASES =  {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': params['dbname'],
        'HOST':params['host'],
        'USER':params['user'],
        'PASSWORD':params['password'],
    }
}