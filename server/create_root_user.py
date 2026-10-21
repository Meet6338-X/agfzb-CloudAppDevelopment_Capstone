"""Create the `root` super user that the peer reviewer uses to log in."""
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangobackend.settings")
django.setup()

from django.contrib.auth.models import User  # noqa: E402  pylint: disable=wrong-import-position

if not User.objects.filter(username="root").exists():
    User.objects.create_superuser("root", "root@bestcars.com", "root")
    print("Superuser 'root' created successfully.")
else:
    print("Superuser 'root' already exists.")
