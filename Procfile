web: gunicorn rebalancer.wsgi --log-file -
worker: celery -A proj worker -l info