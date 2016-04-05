from .base import *
import os

print "USING DEVELOPMENT SETTINGS....."

DEBUG = True

ALLOWED_HOSTS = ['localhost']

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

print 'STATIC_ROOT(DEV): %s' % STATIC_ROOT

if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'rebalancerDB',
            'USER': 'vincentlee',
            'PASSWORD': '708husch',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
        },
    },
}

# eMail Settings
DEFAULT_FROM_EMAIL = 'Christopher Lee <vincent.lee@portfolio270.xyz>'
EMAIL_HOST = 'smtp.postmarkapp.com'
EMAIL_PORT = 2525
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '9aeb6e3e-b988-4f35-8ffc-2442270d913d'
EMAIL_HOST_PASSWORD = '9aeb6e3e-b988-4f35-8ffc-2442270d913d'

# Redis configurations for Celery
# CELERY STUFF
BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/New_York'
