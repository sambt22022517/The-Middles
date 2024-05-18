"""
Django settings for allbachelor project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+)&mi89-=v@-7o=qvf-kq+v7)9j9@0r%a#*x!h+^o2ne3e6%^$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
STATICFILES_DIRS =[
    "/Users/akp/PycharmProjects/webdjango/webdjango/static"
]

# Application definition

INSTALLED_APPS = [
    'shop.apps.ShopConfig',
    #'blog',
    # 'shop'
    'webdjango',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'bootstrap_datepicker_plus',
    'markdownx',
    'markdown_deux',
    'zxcvbn_password',
    'profiles',
    # 'social_django',
    'order',
    #'tfidf',

]
# AUTHENTICATION_BACKENDS = [
#     'social_core.backends.google.GoogleOAuth2',
#     'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
#     'social_core.backends.google.GoogleOpenId',  # for Google authentication
#     'social_core.backends.google.GoogleOAuth2',  # for Google authentication
#     'django.contrib.auth.backends.ModelBackend'
# ]
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'webdjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': [os.path.join(BASE_DIR, 'templates')], luc dau de nhu nay, xong de  dung template mac dinh cua admin chuyen thanh nhu duoi 
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'social_django.context_processors.backends',
                # 'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'webdjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'OPTIONS': {
#             'read_default_file': os.path.join(BASE_DIR, 'database.cnf'),
#         },
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'


TIME_ZONE = 'UTC'
USE_TZ = True

USE_I18N = True

#USE_L10N = True




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

#LOGIN_REDIRECT_URL = 'shophome'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# SOCIAL_AUTH_URL_NAMESPACE = 'users:social'
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '911875216013-m2t2lkpavpfaqmfk9ije51la0vgpd7ck.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'fLmXYRvv-pdbHzWDEl7KIL9a'

MEDIA_ROOT= os.path.join(BASE_DIR, 'media/')
MEDIA_URL= "/media/"
LOGIN_REDIRECT_URL = '/shop'

