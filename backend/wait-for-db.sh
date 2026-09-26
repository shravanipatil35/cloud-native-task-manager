#!/bin/sh
set -eu

echo "Waiting for postgres..."

while ! nc -z "${DB_HOST:-postgres}" "${DB_PORT:-5432}"; do
  sleep 2
done

echo "PostgreSQL started"

exec gunicorn --bind 0.0.0.0:8888 run:app
