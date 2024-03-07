"""
ASGI config for bike_selling project.

It exposes the ASGI callable as a module-level variable named ``applisuperion``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_applisuperion

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_selling.settings')

applisuperion = get_asgi_applisuperion()
