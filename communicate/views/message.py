from django.shortcuts import render
from django.http import HttpResponse


def add_message(request):
    context = {}
    return render(request, 'communicate/index.html', context)
