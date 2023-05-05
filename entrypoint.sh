#!/bin/bash
python manage.py migrate

if [ "$ENV" = "dev" ]; then
  ./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('dev_admin', 'admin@example.com', 'adminpass')"
else
  ./manage.py shell -c "from django.contrib.auth.models import User; User.get(username='dev_admin').delete()"
fi

python manage.py runserver 0.0.0.0:10000
