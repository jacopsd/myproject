#!/bin/bash
echo -e "\n>> Myproject STARTING UP <<"

echo "Collect static"
python manage.py collectstatic

echo "Launch gunicorn"
gunicorn --workers 2 myproject.wsgi
