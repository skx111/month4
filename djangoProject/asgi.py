"""
ASGI - Asynchronous Server Gateway Interface
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

application = get_asgi_application()
