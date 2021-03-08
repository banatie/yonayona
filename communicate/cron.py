from .utils import availability_utils
from .models import Conversation
from .websocket import server_utils


def end_all_conversation():
    if availability_utils.is_available():
        return

    try:
        # End all conversation
        conversations = Conversation.objects.filter(is_active=True)
    except Conversation.DoesNotExist:
        pass

    for conversation in conversations:
        conversation.is_active = False
        conversation.save()

        # send end command
        server_utils.send_command(conversation_id=conversation.id, command="end")
