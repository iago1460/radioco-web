#!/bin/bash -x

uwsgi --http 0.0.0.0:8000 --module web.wsgi --master --processes 2 --threads 1