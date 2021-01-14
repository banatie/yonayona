from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def send_command(conversation_id, command):
    # send messsage to group
    group_name = 'conversation_{group_name}'.format(group_name=conversation_id)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type' : 'conversation_message',
            'username': 'master',
            'message' : '',
            'command' : command
        }
    )
