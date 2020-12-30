from django.shortcuts import render
from django.http import HttpResponse


def add_message(request):
    return HttpResponse('add_message view by Eiji')
