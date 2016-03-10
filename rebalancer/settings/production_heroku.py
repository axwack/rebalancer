from .base import *
import dj_database_url

print "USING PRODUCTION SETTINGS..."
# STATIC_ROOT = 'staticfiles'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

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
DEFAULT_FROM_EMAIL = 'Christopher Lee <admin@principalmvl.com>'
EMAIL_HOST = '#.1and1.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'admin@principalmvl.com'
EMAIL_HOST_PASSWORD = '#'

# Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (
#    os.path.join(PROJECT_ROOT, 'equity/static'),
# )

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
