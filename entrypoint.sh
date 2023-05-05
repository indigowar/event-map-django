#!/bin/bash
python manage.py migrate
#./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')"

python manage.py runserver 0.0.0.0:10000
