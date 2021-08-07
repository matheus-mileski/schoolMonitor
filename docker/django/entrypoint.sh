#!/bin/bash

cd /api

wait-for-it ${POSTGRES_HOST}:${POSTGRES_PORT} -- echo "Database is ready! Listening on ${POSTGRES_HOST}:${POSTGRES_PORT}"

if [ -f manage.py ]; then
    python manage.py runserver 0.0.0.0:8000
else 
    django-admin startproject ${PROJECT_NAME} . 
fi

