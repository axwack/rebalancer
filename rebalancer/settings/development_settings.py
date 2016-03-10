from .base import *

print "USING DEVELOPMENT SETTINGS....."

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['localhost:8000']

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
