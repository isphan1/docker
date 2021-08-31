from __future__ import absolute_import, unicode_literals

from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import random, math

@shared_task
def get_auto_number():

    number = random.randint(1,999999)
    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        "celery", {
            'type': 'celery_message',
            'message':number
        }
    )