"""
Django settings for recommender project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), ".."),
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v5p0x&kg2-r#k60ewihqgr_dqw^w+p10c49@$kwsr6#3qrpx43'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangobower',
    'south',
    'movie_data',
    'movie_names',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'recommender.urls'

WSGI_APPLICATION = 'recommender.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'vagrant',                      # Or path to database file if using sqlite3.
        'USER': 'vagrant',                      # Not used with sqlite3.
        'PASSWORD': 'vagrant',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                    # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                             # Set to empty string for default. Not used with sqlite3.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

STATIC_URL = '/static/'

BOWER_COMPONENTS_ROOT = os.path.join(PROJECT_ROOT, 'components')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)
BOWER_INSTALLED_APPS = (
    'fontawesome',
    # 'messenger', #javascript ajax notification popups
    # 'semantic-ui', #slider checkboxes
    'jquery#1.9',
    'underscore',
    'd3#~3.3.13', #IMPORTANT: v3.3.13 required by nvd3
    'morris.js#0.4.3',
    'flot',
    'nvd3',
    'bootstrap#3.1.1',
    'jquery-ui#1.9.2',
    'datetimepicker#2.2.9',
    "https://github.com/harvesthq/chosen/releases/download/v1.1.0/chosen_v1.1.0.zip", #Chosen for Multi Select,
    "CSS-Filters-Polyfill", #css-filter for Modal
    # "https://github.com/codrops/ModalWindowEffects/archive/master.zip", #Modal windows library
    "https://git.techops.cmich.edu/narot1a/modalwindoweffects/repository/archive.zip?ref=master", #Modal windows library
    # 'tapmantwo-fork-of-jQuery-UI-MultiSelect-Widget#1.4'
    "chosen-bootstrap",
    "https://git.techops.cmich.edu/narot1a/notify/repository/archive.zip?ref=logo",
    "https://git.techops.cmich.edu/narot1a/sb-admin-2/repository/archive.zip?ref=master", #Dashboard template

)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)
