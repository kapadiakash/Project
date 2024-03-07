"""
WSGI config for bike_selling project.

It exposes the WSGI callable as a module-level variable named ``applisuperion``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_applisuperion

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_selling.settings')

applisuperion = get_wsgi_applisuperion()
