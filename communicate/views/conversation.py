from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from ..models import Conversation
from ..utils import conversation_queries, availability_utils
from ..websocket import server_utils

def start_conversation(request):
    if not request.user.is_authenticated or not availability_utils.is_available():
        return HttpResponseRedirect(reverse('communicate:index'))

    conversations = Conversation.objects.filter(is_active=True, users__in=[request.user])

    if len(conversations) > 0:
        # already in active conversation
        pass
    else:
        conversations = Conversation.objects.filter(is_active=True)
        for conversation in conversations:
            if len(conversation.users.all()) == 1:
                # opened active conversation exists
                conversation.users.add(request.user)
                conversation.save()

                # send start command
                server_utils.send_command(conversation_id=conversation.id, command='start')

                return HttpResponseRedirect(reverse('communicate:index'))
        else:
            # no opened active conversation
            conversation = Conversation.objects.create()
            conversation.users.add(request.user)
            conversation.save()

    return HttpResponseRedirect(reverse('communicate:index'))

def cancel_conversation(request, conversation_id):
    try:
        # find unmatched conversation
        conversation = Conversation.objects.get(id=conversation_id)
    except Conversation.DoesNotExist:
        return HttpResponseRedirect(reverse('communicate:index'))

    # delete
    conversation.delete()
    return HttpResponseRedirect(reverse('communicate:index'))

def end_conversation(request, conversation_id):
    try:
        # update conversation
        conversation = Conversation.objects.get(id=conversation_id, is_active=True)
    except Conversation.DoesNotExist:
        return HttpResponseRedirect(reverse('communicate:index'))

    conversation.is_active = False
    conversation.save()

    # send end command
    server_utils.send_command(conversation_id=conversation_id, command="end")

    return HttpResponseRedirect(reverse('communicate:index'))

def view_conversation(request, conversation_id):
    try:
        conversation = Conversation.objects.get(pk=conversation_id)
    except Conversation.DoesNotExist:
        return HttpResponseRedirect(reverse('communicate:index'))

    context = {}
    # send message history
    messages = conversation_queries.get_message_history(conversation_id)
    context['messages_to_view'] = messages

    # send inactive conversations
    conversations = conversation_queries.get_inactive_conversations(user=request.user)
    context['history_conversations'] = conversations
    return render(request, 'communicate/index.html', context)

def delete_conversation(request, conversation_id):
    try:
        # update conversation
        conversation = Conversation.objects.get(pk=conversation_id)
    except Conversation.DoesNotExist:
        return HttpResponseRedirect(reverse('communicate:index'))

    if request.user not in conversation.users_deleted.all():
        conversation.users_deleted.add(request.user)

        for user in conversation.users.all():
            if user in conversation.users_deleted.all():
                continue
            else:
                # not all users deleted
                conversation.save()
                break
        else:
            # all users deleted
            conversation.delete()
    return HttpResponseRedirect(reverse('communicate:index'))
