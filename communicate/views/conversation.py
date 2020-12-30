from django.shortcuts import render
from django.http import HttpResponse


def view_conversation(request):
    return HttpResponse('view_conversation view by Eiji')
def delete_conversation(request):
    return HttpResponse('delete_conversation view by Eiji')
