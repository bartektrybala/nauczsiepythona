#!/bin/bash

python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn apka_wstepna.wsgi:application --bind 0.0.0.0:8000


