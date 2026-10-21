#!/bin/sh

if [ "$DATABASE" = "postgres" ]; then
    echo "waiting for postgres..."
    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
        sleep 0.1
    done
    echo "PostgreSQL started"
fi

# Make migrations and migrate the database.
echo "Making migrations and migrating the database. "
python manage.py makemigrations djangoapp --noinput
python manage.py migrate --noinput
python manage.py seed_carmakes
python create_root_user.py
exec "$@"
