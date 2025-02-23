import os
from pathlib import Path
from .settings import *
from .settings import BASE_DIR



ALLOWED_HOSTS = ['gumption-dev-hmbferejfsd2c8ct.canadacentral-01.azurewebsites.net', 'gumptionrpg.com', '']
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME'],'https://gumptionrpg.com']
DEBUG = True
SECRET_KEY = os.environ['MY_SECRET_KEY']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home_page.apps.HomePageConfig',
    'create.apps.CreateConfig',
    'guides.apps.GuidesConfig',
    'homebrew.apps.HomebrewConfig',

]

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
params = {pair.split('=')[0]:pair.split('=')[1] for pair in connection_string.split(' ')}

DATABASES =  {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': params['dbname'],
        'HOST':params['host'],
        'USER':params['user'],
        'PASSWORD':params['password'],
    }
}