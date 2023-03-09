import json
from django.contrib.auth.models import User
from .models import Rooms, Messages, Profile
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

class ChatRoomConsumers(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_room_name = self.scope['url_route']['kwargs']['chat_room_name']
        self.chat_group_name = 'chat_%s' % self.chat_room_name

        await self.channel_layer.group_add(self.chat_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.chat_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        room = text_data_json["room"]

        await self.save_message(username, room, message)
        await self.channel_layer.group_send(
            self.chat_group_name,
            {
                "type": "chatbox_message",
                "message": message,
                "username": username,
                "room": room
            },
        )

    async def chatbox_message(self, event):
        message = event["message"]
        username = event["username"]
        room = event["room"]

        await self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "username": username,
                    "room": room
                }
            )
        )
    @sync_to_async
    def save_message(self, username, room, message):
        username = User.objects.get(username=username)
        room = Rooms.objects.get(id=room)
        profile = Profile.objects.get(user_id=username.id)
        Messages.objects.create(message_sender=profile, room=room, message=message)