from .base import *
import dj_database_url, os

DEBUG = False


print "USING PRODUCTION SETTINGS..."
# STATIC_ROOT = ''
STATIC_ROOT = os.path.join(PROJECT_PATH, 'staticfiles')

print "Heroku [STATIC_ROOT]: %s" % (STATIC_ROOT)

STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles'),
)

print "Heroku [STATICFILES_DIRS]: %s" % (STATICFILES_DIRS)

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['www.portfolio270.xyz', '*.herokuapp.com']

# eMail Settings
DEFAULT_FROM_EMAIL = 'Christopher Lee <vincent.lee@portfolio270.xyz>'
EMAIL_HOST = 'smtp.postmarkapp.com'
EMAIL_PORT = 2525
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '9aeb6e3e-b988-4f35-8ffc-2442270d913d'
EMAIL_HOST_PASSWORD = '9aeb6e3e-b988-4f35-8ffc-2442270d913d'

# Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (
#    os.path.join(PROJECT_ROOT, 'equity/static'),
# )

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

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

# Redis configurations for Celery
# CELERY STUFF
BROKER_URL = 'redis://ec2-54-83-207-91.compute-1.amazonaws.com:12619'
CELERY_RESULT_BACKEND = 'redis://ec2-54-83-207-91.compute-1.amazonaws.com:12619'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/New_York'
