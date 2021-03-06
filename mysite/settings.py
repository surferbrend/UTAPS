"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os, datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DUO_LOGIN_URL = '/duo_login'

# Duo configuration.


DUO_IKEY = ''
DUO_SKEY = ''
DUO_AKEY = ''
DUO_HOST = ''


ALLOWED_HOSTS = ['*','utah.edu']
REGISTRATION_EMAIL_HTML = False
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ""
EMAIL_PORT = 25
EMAIL_USE_TLS = True


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!





# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  
TEMPLATES_DEBUG = False 


#ALLOWED_HOSTS = ['*',u'surferbrend.pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_filters',
    'rest_framework',
    'rest_framework_gis',
    'crispy_forms',
    'registration',
#    'forms_builder.forms',
#    'oidc_auth',
#    'oauth2_provider',
    'djangosecure',
    'webfront'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
#    'django.contrib.sites.middleware.CurrentSiteMiddleware',
#    'django.contrib.sites.requests',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.auth.middleware.SessionAuthenticationMiddleware'    
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

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


REST_FRAMEWORK = {
# Use Django's standard `django.contrib.auth` permissions,
# or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
#      'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
      'rest_framework.permissions.IsAuthenticated'
                                  ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
      'rest_framework.authentication.SessionAuthentication',
      'rest_framework.authentication.BasicAuthentication',
      'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
                                                        ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
#    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2000,
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
# 'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer',)

                                       }

JWT_AUTH = {
            'JWT_ENCODE_HANDLER':
                'rest_framework_jwt.utils.jwt_encode_handler',

            'JWT_DECODE_HANDLER':
                'rest_framework_jwt.utils.jwt_decode_handler',

            'JWT_PAYLOAD_HANDLER':
                'rest_framework_jwt.utils.jwt_payload_handler',

            'JWT_PAYLOAD_GET_USER_ID_HANDLER':
                'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

            'JWT_RESPONSE_PAYLOAD_HANDLER':
                'rest_framework_jwt.utils.jwt_response_payload_handler',

            'JWT_SECRET_KEY': SECRET_KEY,
            'JWT_ALGORITHM': 'HS256',
            'JWT_VERIFY': True,
            'JWT_VERIFY_EXPIRATION': True,
            'JWT_LEEWAY': 0,
            'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
            'JWT_AUDIENCE': None,
            'JWT_ISSUER': None,
            'JWT_ALLOW_REFRESH': False,
            'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
            'JWT_AUTH_HEADER_PREFIX': 'JWT',
                                                                                            }


WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}


os.environ['TDSVER'] = '8.0'
SECRET_KEY = ''

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

STATIC_URL = '/static/'
STATICFILES_DIRS = [
            os.path.join(BASE_DIR, "static"),
]
#            '/static/',]
# default static files settings for PythonAnywhere.
# see https://help.pythonanywhere.com/pages/DjangoStaticFiles for more info
MEDIA_ROOT = u'/var/www/html/mysite/mysite/media'
MEDIA_URL = '/media/'
STATIC_ROOT = u'/var/www/html/mysite/mysite/static/admin'
#STATIC_ROOT = os.path.join(BASE_DIR, "static")

LOGIN_REDIRECT_URL = 'duo_login'
LOGIN_REDIRECT_URL_DUO = '/accounts/profile'


CRISPY_TEMPLATE_PACK = 'bootstrap3'
#ACCOUNT_ACTIVATION_DAYS = 30
#REGISTRATION_AUTO_LOGIN = False
SITE_ID=1
#CSRF_COOKIE_SECURE = True
