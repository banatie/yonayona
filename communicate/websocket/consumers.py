import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth import get_user_model

from ..models import Message
from ..models import Conversation


class CommunicateConsumer(WebsocketConsumer):
    def connect(self):
        self.conversation_id = self.scope['url_route']['kwargs']['conversation_id']
        self.group_name = 'conversation_{group_name}'.format(group_name=self.conversation_id)

        # Join the group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_node):
        # Leave the conversation
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def receive(self, text_data):
        # receive message from websocket
        text_data_json = json.loads(text_data)
        username = text_data_json['username']
        message = text_data_json['message']
        try:
            command = text_data_json['command']
        except KeyError:
            command = ''

        # save to db
        user = get_user_model().objects.get(username=username)
        #user = users[0]
        conversation = Conversation.objects.get(id=self.conversation_id)

        Message(user_from=user, conversation_id=conversation, text=message).save()   

        # send messsage to group
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type' : 'conversation_message',
                'username': username,
                'message' : message,
                'command' : command
            }
        )

    def conversation_message(self, event):
        # receive message from group
        username = event['username']
        message = event['message']
        command = event['command']

        # send message to websocket
        self.send(text_data=json.dumps({
            'username': username,
            'message' : message,
            'command' : command
        }))
        