from django.shortcuts import render
from django.http import HttpResponse


def start_conversation(request):
    # find opened conversation
    # if no, create a new conversation
    context = {'conversation_id' : '123'}
    return render(request, 'communicate/index.html', context)
def view_conversation(request):
    context = {}
    return render(request, 'communicate/index.html', context)
def delete_conversation(request):
    context = {}
    return render(request, 'communicate/index.html', context)
