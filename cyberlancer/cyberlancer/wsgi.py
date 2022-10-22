"""
WSGI config for cyberlancer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cyberlancer.settings')

application = get_wsgi_application()


"""
import os 
import sys 

## assuming your django settings file is at '/home/drakeredwind01/cyberlancer'
## and your manage.py is at 
path= '/home/drakeredwind01/cyberlancer'
if path not in sys.path:
    sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'cyberlancer.settings'

## then, for django >=1.5:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
## or, for older django <= 1.4
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler
"""