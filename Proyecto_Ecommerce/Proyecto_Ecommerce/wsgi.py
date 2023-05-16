"""
WSGI config for Proyecto_Ecommerce project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append('/Proyecto Ecommerce/Proyecto_Ecommerce')
sys.path.append('/Proyecto Ecommerce/Proyecto_Ecommerce/Proyecto_Ecommerce')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Proyecto_Ecommerce.settings')

application = get_wsgi_application()
