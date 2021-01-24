"""
WSGI config for silaeder_exchange project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""
'''
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'silaeder_exchange.settings')

application = get_wsgi_application()
'''
'''
import os
import signal

import sys
import traceback

import time
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projectname.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
'''
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "silaeder_exchange.settings")

# This application object is used by the development server
# as well as any WSGI server configured to use this file.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()