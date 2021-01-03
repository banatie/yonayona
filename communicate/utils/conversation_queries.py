from django.db.models import Q

from ..models import Conversation
from ..models import Message


def get_inactive_conversations(user):
    history_conversations = []
    inactive_conversations = Conversation.objects.filter(Q(is_active=False) & Q(users__in=[user]) & ~Q(users_deleted__in=[user]))
    if len(inactive_conversations) > 0:
        # format
        for conversation in reversed(inactive_conversations):
            date = conversation.datetime_start.strftime('%Y-%m-%d')
            duration = str(conversation.datetime_end - conversation.datetime_start)
            duration = duration.split('.')[0]
            history_conversations.append({
                'id' : conversation.id,
                'date' : date,
                'duration' : duration
            })
    return history_conversations

def get_message_history(conversation_id):
    return Message.objects.filter(conversation_id=conversation_id).order_by('datetime_created')
