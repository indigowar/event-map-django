import os


def entrypoint() -> None:
    # migrate database
    os.system("python manage.py migrate")

    # setup dev admin here, if it's dev mode
    if os.getenv('ENV') == 'dev':
        os.system(""
                  "python ./manage.py shell -c "
                  "\"from django.contrib.auth.models import User; User.objects.create_superuser('dev_admin', "
                  "'admin@example.com', 'dev_admin_pass')\"")

    # start the server
    os.system("python manage.py runserver 0.0.0.0:10000")

    pass


if __name__ == '__main__':
    entrypoint()
