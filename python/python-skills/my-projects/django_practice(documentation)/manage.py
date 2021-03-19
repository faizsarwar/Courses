#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#to run server on other ports ----->>python3 manage.py runserver  8080

# a project can contain multipe apps("website with (e-commerce capability,bloging) Both are considered as two seperate apps in a project ")
## a project can contain multiple apps and an app can be used in multiple projects

#for creating a app---->python3 manage.py startapp polls

# views.py ki file ka matlab kis url pe knsa html page show krna hai user ko har app mai alag hugi(views.py)
#url ka batanay keliye hamain url.py ki file banani paraygii hr app mai khud
