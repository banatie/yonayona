from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {}
    if True:
        # Logged in
        return render(request, 'communicate/index.html', context)
    else:
        return render(request, 'communicate/user.html', context)        
def about(request):
    context = {}
    return render(request, 'communicate/about.html', context)
def signup(request):
    context = {}
    return render(request, 'communicate/signup.html', context)
def login(request):
    context = {}
    return render(request, 'communicate/user.html', context)
def logout(request):
    context = {}
    return render(request, 'communicate/index.html', context)
def report_user(request):
    # Add Welcome Message
    context = {}
    return render(request, 'communicate/user.html', context)
