from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class CeleryConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'celery'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from room group
    def celery_message(self, event):
        message = event['message']

        # print(message)

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))