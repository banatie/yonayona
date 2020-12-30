from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('index view by Eiji')
def signup(request):
    return HttpResponse('signup view by Eiji')
def login(request):
    return HttpResponse('login view by Eiji')
def logout(request):
    return HttpResponse('logout view by Eiji')
def report_user(request):
    return HttpResponse('report_user view by Eiji')
