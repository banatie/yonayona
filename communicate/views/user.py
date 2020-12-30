from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # Not Logged In
    #  render to index.html
    # Logged In
    #  render to user.html
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
    # GET
    #  render to signup.html
    # POST
    # valid email
    # valid password
    #  render to user.html
    context = {}
    if True:
        # Validated
        return render(request, 'communicate/user.html', context)
    else:
        return render(request, 'communicate/signup.html', context)
def login(request):
    # POST
    # not logged in
    # user exists
    #  render to user.html
    # GET
    #  render to index view
    context = {}
    return render(request, 'communicate/user.html', context)
def logout(request):
    # logged in
    # logout
    #  render to index.html
    context = {}
    return render(request, 'communicate/index.html', context)
def report_user(request):
    # Add Welcome Message
    context = {}
    return render(request, 'communicate/user.html', context)
