from django.shortcuts import render
from django.http import HttpResponse


def add_message(request):
    context = {}
    return render(request, 'communicate/user.html', context)
