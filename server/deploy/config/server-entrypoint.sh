#!/bin/sh

until cd /app/server; do
  echo "Waiting for server volume..."
done

until python manage.py makemigrations locations subjects students payments examinations questions results examiners combinations; do
  echo "Waiting for db to be ready..."
  sleep 2
done

#python manage.py makemigrations locations subjects students payments examinations questions results examiners combinations
python manage.py migrate

python manage.py collectstatic --noinput

python manage.py createadmin
python manage.py creategrades
echo "Superuser created:: username - careproadmin, password - 12345"
#python manage.py runserver 0.0.0.0:8500
gunicorn server.wsgi:application --bind 0.0.0.0:8500
exec "$@"
