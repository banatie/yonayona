from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from ..models import Conversation


def start_conversation(request):
    if not request.user.is_authenticated:
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
                return HttpResponseRedirect(reverse('communicate:index'))

        # no opened active conversation
        conversation = Conversation.objects.create()
        conversation.users.add(request.user)
        conversation.save()

    return HttpResponseRedirect(reverse('communicate:index'))

def end_conversation(request, conversation_id):
    # update conversation
    try:
        conversation = Conversation.objects.get(id=conversation_id, is_active=True)
    except Conversation.DoesNotExist:
        return HttpResponseRedirect(reverse('communicate:index'))

    conversation.is_active = False
    conversation.save()

    return HttpResponseRedirect(reverse('communicate:index'))

def view_conversation(request):
    context = {}
    return render(request, 'communicate/index.html', context)

def delete_conversation(request, conversation_id):
    # update conversation
    try:
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
        else:
            # all users deleted
            conversation.delete()
    return HttpResponseRedirect(reverse('communicate:index'))
