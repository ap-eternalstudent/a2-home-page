import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.join(BASE_DIR, os.pardir)


SECRET_KEY = '-rygel@f6=e)cais%tg)7-#o_-jl7pev0r@+1#)6sb06xh_*sl'


DEBUG = True
DEFAULT_FROM_EMAIL = 'info@wearea2.com'

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '0.0.0.0',
    '.elasticbeanstalk.com',
    '.wearea2.com',
    'wearea2.com',
]


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'snowpenguin.django.recaptcha2',
    'django_mailgun',
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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'a2/components/pages/templates'
        ],
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

ROOT_URLCONF = 'a2.urls'
WSGI_APPLICATION = 'a2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Messages
# https://docs.djangoproject.com/en/2.1/ref/contrib/messages/

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'


# Email
# https://docs.djangoproject.com/en/2.1/topics/email/

EMAIL_BACKEND = 'django_mailgun.MailgunBackend'


# reCaptha
# https://github.com/kbytesys/django-recaptcha2

RECAPTCHA_PUBLIC_KEY = '6LfM7okUAAAAADM5FYDvASf2knv6PoNLlzsfUcS3'
RECAPTCHA_PRIVATE_KEY = '6LfM7okUAAAAAO0ZfcG7pdwptw71k80veD7mqZJx'


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'public/static')
    
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'a2/static'),
]


# Mailgun
# https://pypi.org/project/django-mailgun/

MAILGUN_ACCESS_KEY = 'd12c18559b84d915c70ba2081ee270a1-985b58f4-6fec4d4b'
MAILGUN_SERVER_NAME = 'https://api.mailgun.net/v3/mg.wearea2.com'
