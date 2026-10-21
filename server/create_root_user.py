"""Create the `root` super user that the peer reviewer uses to log in.

The script is idempotent, it can be run every time the application starts.
It also makes sure that the demo application user `shahm` exists so that the
logged in screens of the submission can be reproduced at any time.
"""
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

if not User.objects.filter(username="shahm").exists():
    user = User.objects.create_user("shahm", "shahm.dar@example.com", "Shahm@2024")
    user.first_name = "Shahm"
    user.last_name = "Dar"
    user.save()
    print("User 'shahm' created successfully.")
else:
    print("User 'shahm' already exists.")
