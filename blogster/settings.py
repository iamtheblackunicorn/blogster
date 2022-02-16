# BLOGSTER by Alexander Abraham
# a.k.a. "The Black Unicorn" a.k.a. "Angeldust Duke".
# Licensed under the MIT license.

import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-pp#ws*^)3pc9)5$o#^h1a1miaoy5y%m*68^7%65zm#-xzp@xbp'
DEBUG = True
ALLOWED_HOSTS = ['*']
SITE_VARS = {
  'site_name':'Angeldust Duke',
  'site_pic':'https://angeldustduke.art/assets/images/logo/logo.png',
  'site_css':'https://angeldustduke.art/assets/css/main.css',
  'site_social_banner':'https://angeldustduke.art/assets/images/banner/banner.png',
  'site_description':'Angeldust Duke: a bad b*tch, a creative soul, and eccentric as f*ck.',
  'site_banner_description':'Diavorella, the Angeldust Duke\'s muse.',
  'site_keywords':'developer, code, flutter, dart, rust lang, blogging, art, python, compiler',
  'site_57x57_icon':'https://angeldustduke.art/assets/images/favicons/apple-icon-57x57.png',
  'site_60x60_icon':'https://angeldustduke.art/assets/images/favicons/apple-icon-60x60.png',
  'site_72x72_icon':'https://angeldustduke.art/assets/images/favicons/apple-icon-72x72.png',
  'site_76x76_icon':'https://angeldustduke.art/assets/images/favicons/apple-icon-76x76.png',
  'site_114x114_icon':'https://angeldustduke.art/assets/images/favicons/apple-icon-114x114.png',
  'site_120x120_icon':'https://angeldustduke.art/assets/images/favicons/apple-icon-120x120.png',
  'site_144x144_icon':'https://angeldustduke.art/assets/images/favicons/ms-icon-144x144.png',
  'site_152x152_icon':'https://angeldustduke.art/assets/images/favicons/apple-icon-152x152.png',
  'site_180x180_icon':'https://angeldustduke.art/assets/images/favicons/apple-icon-180x180.png',
  'site_192x192_icon':'https://angeldustduke.art/assets/images/favicons/android-icon-192x192.png',
  'site_32x32_icon':'https://angeldustduke.art/assets/images/favicons/favicon-32x32.png',
  'site_96x96_icon':'https://angeldustduke.art/assets/images/favicons/favicon-96x96.png',
  'site_16x16_icon':'https://angeldustduke.art/assets/images/favicons/favicon-16x16.png'
}
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts.apps.PostsConfig'
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
ROOT_URLCONF = 'blogster.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'blogster.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
