#!/bin/bash -x

python3 manage.py collectstatic --no-input
uwsgi --http 0.0.0.0:8000 --ini ../docker/django/scripts/uwsgi.ini