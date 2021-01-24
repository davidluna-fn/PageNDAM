"""
WSGI config for page project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys

sys.path.insert(0, '/home/dflunan/webapps/page/PageNDAM/')
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "page.settings")

application = get_wsgi_application()
