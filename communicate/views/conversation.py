from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from ..models import Conversation


def start_conversation(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('communicate:index'))

    conversations = Conversation.objects.filter(is_active=True, users__username=request.user.username)

    if len(conversations) > 0:
        # already in active conversation
        pass
    else:
        conversations = Conversation.objects.filter(is_active=True)
        for conversation in conversations:
            if len(conversation.users) == 1:
                # opened active conversation exists
                conversation.users.add(request.user)
                conversation.save()
                return HttpResponseRedirect(reverse('communicate:index'))

        # no opened active conversation
        conversation = Conversation.objects.create()
        conversation.users.add(request.user)
        conversation.save()

    return HttpResponseRedirect(reverse('communicate:index'))

def view_conversation(request):
    context = {}
    return render(request, 'communicate/index.html', context)
def delete_conversation(request):
    context = {}
    return render(request, 'communicate/index.html', context)
