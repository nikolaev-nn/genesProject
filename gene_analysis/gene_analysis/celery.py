import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gene_analysis.settings')

app = Celery('gene_analysis')
app.config_from_object('django.conf:settings', namespace='CELERY')
