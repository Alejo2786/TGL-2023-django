

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'judicalApi.settings')

app = Celery('judicialApi')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
