# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

print __file__

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))  # added Heroku

PROJECT_PATH = os.path.join(BASE_DIR, 'equity/templates')

print "Templates in [PROJECT PATH]: %s" % (PROJECT_PATH)

print "Templates in [BASE DIR]: %s" % (BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')jlb!a3nqv!=j5dp#m1hplc$@%sxf#ut^p%d+@f1^f3=(ap&j6'

# Application definition
ALLOWED_HOSTS = []

INSTALLED_APPS = (

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',
    'django.contrib.admin',
    # Third Party
    'crispy_forms',
    'rest_framework',
    'treebeard',

    # MY app
    'equity',
)

# REGISTRARIONT REDUx
ACCOUNT_ACTIVATION_DAYS = 2
REGISTRATION_OPEN = True
REGISTRATION_AUTO_LOGIN = True
INCLUDE_REGISTER_URL = True
LOGIN_URL = '/Accounts/login/'
SITE_ID = 1
LOGIN_REDIRECT_URL = "/index"

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'rebalancer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [PROJECT_PATH],
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

WSGI_APPLICATION = 'rebalancer.wsgi.application'

CRISPY_TEMPLATE_PACK = "bootstrap3"
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
# STATIC_ROOT = os.path.join(BASE_DIR, "..", "www", "static", "staticfiles")
STATIC_ROOT = os.path.join(BASE_DIR, "equity/static")
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files. Added Heroku
# STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'equity/static'),
# )


DATABASES = {
    'default': {}
}

CLASSIFICATION_ROOT = 'Classification'
