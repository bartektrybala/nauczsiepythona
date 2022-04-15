#!/bin/bash

python manage.py migrate --no-input

gunicorn apka_wstepna.wsgi:application --bind 0.0.0.0:8000


