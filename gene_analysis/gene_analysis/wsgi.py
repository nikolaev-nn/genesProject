"""
WSGI config for gene_analysis project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append('/usr/lib/python3.8/site-packages')
sys.path.append('/usr/lib/python3.9')
sys.path.append('/home/django/genesProject/venv/lib/python3.9/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gene_analysis.settings')

application = get_wsgi_application()
