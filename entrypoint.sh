#!/bin/sh
python manage.py collectstatic --no-input
python manage.py makemigrations people loss_communications
python manage.py migrate
python manage.py loaddata users
#gunicorn backend_python_wallet.wsgi:application --bind 0.0.0.0:8000 --workers 3 --access-logfile='-'
python manage.py runserver 0.0.0.0:8000
exec "$@"