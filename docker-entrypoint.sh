#!/bin/bash

# Run Django migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Execute the CMD command
exec "$@"

