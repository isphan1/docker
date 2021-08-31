from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get-auto-number-every-3-seconds': {
        'task': 'news.tasks.get_auto_number',
        'schedule': 3.0,
        'args': ()
    },
}

app.conf.timezone = 'UTC'

app.autodiscover_tasks()