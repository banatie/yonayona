from django.shortcuts import render
from django.http import HttpResponse


def view_conversation(request):
    context = {}
    return render(request, 'communicate/user.html', context)
def delete_conversation(request):
    context = {}
    return render(request, 'communicate/user.html', context)
