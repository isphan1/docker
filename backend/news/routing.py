from django.urls import re_path
from . import consumers

ws_urlPatterns=[
    re_path(r'ws/celery/$',consumers.CeleryConsumer.as_asgi()),
]