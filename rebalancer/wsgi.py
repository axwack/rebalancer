"""
WSGI config for rebalancer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
import sys, logging

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rebalancer.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)  # added for Heroku
application.logger.addHandler(logging.StreamHandler(sys.stdout))
application.logger.setLevel(logging.ERROR)

try:
    from dj_static import Cling
    application = Cling(get_wsgi_application())
except:
    pass

