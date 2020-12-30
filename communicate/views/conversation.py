from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from ..models import Conversation


def start_conversation(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('communicate:index'))

    conversations = None
    try:
        conversations = Conversation.objects.filter(is_active=True, users__in=request.user)
    except:
        pass

    if conversations is None:
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
