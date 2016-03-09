from .base import *
import dj_database_url
# Added for Heroku

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['www.portfolio270.xyz']

# eMail Settings
DEFAULT_FROM_EMAIL = 'Christopher Lee <admin@principalmvl.com>'
EMAIL_HOST = '#.1and1.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'admin@principalmvl.com'
EMAIL_HOST_PASSWORD = '#'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'equity/static')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
