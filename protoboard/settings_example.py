"""

You need to RENAME THIS FILE to settings.py
and put you own settings.



Django settings for protoboard project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)


import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

###CREATE YOUR OWN
SECRET_KEY = 'blahblahblahblahblahblahblahblahblah'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# CHANGE
MEDIA_URL = "https://s3.amazonaws.com/your_bucket/"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
# Application definition

FACEBOOK_APP_ID = "635XXX3532XXXXX"
FACEBOOK_APP_SECRET = "XXXXXX8a1d124f0c1df5c9ZZZZZZ1be0"
FACEBOOK_REDIRECT_URL = "http://localhost:8000/facebook/login/"

EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='mariosky@gmail.com'
EMAIL_HOST_PASSWORD='1234567'
EMAIL_PORT=465
EMAIL_USE_SSL=True
ACCOUNT_ACTIVATION_DAYS=7
REGISTRATION_AUTO_LOGIN = True

#We include our own RegisterForm
INCLUDE_REGISTER_URL=False


MONGO_DB = "127.0.0.1"
# Application definition
AUTHENTICATION_BACKENDS = (
#      'social.backends.google.GooglePlusAuth',
  'activitytree.backends.FacebookBackend',
      'django.contrib.auth.backends.ModelBackend',)

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
    'registration',

	'activitytree'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'protoboard.urls'

WSGI_APPLICATION = 'protoboard.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'protoboard',                      # Or path to database file if using sqlite3.
        'USER': 'django',                      # Not used with sqlite3.
        'PASSWORD': 'le_pass',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
        }
}

from os.path import join
TEMPLATE_DIRS = (
    join(BASE_DIR,  'templates'),
)



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


