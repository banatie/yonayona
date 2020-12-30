from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def index(request):
    # Not Logged In
    #  render to index.html
    # Logged In
    #  render to user.html
    return render(request, 'communicate/index.html', {})

def about(request):
    context = {}
    return render(request, 'communicate/about.html', context)

def user_signup(request):
    if request.user.is_authenticated:
        # Already logged in
        context = {'error_message' : 'User already logged in'}
        return render(request, 'communicate/index.html', context)

    # GET
    if request.method == 'GET':
        return render(request, 'communicate/signup.html', {})
    # POST
    if request.method == 'POST':
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
        except KeyError:
            context = {'error_message' : 'Some form item is not found'}
            return render(request, 'communicate/signup.html', context)
        # valid password
        user = None
        try:
            user = User.objects.get(username=email)
        except User.DoesNotExist:
            pass

        if user is not None:
            context = {'error_message' : 'The Email is already taken'}
            return render(request, 'communicate/signup.html', context)
        else:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=email, email=email, password=password)
            login(request, user)
            return render(request, 'communicate/index.html', {})

def user_login(request):
    # POST
    if request.method == 'POST':
        if not request.user.is_authenticated:
            # not logged in
            try:
                email = request.POST['email']
                password = request.POST['password']
            except KeyError:
                context = {'error_message' : 'Invalid Login Information'}
                return render(request, 'communicate/index.html', context)

            # user exists
            try:
                user = User.objects.get(username=email)
            except User.DoesNotExist:
                context = {'error_message' : 'Invalid Login Information'}
                return render(request, 'communicate/index.html', context)

            login(request, user)
            return render(request, 'communicate/index.html', {})
        else:
            pass

        #  render to index.html
        return render(request, 'communicate/index.html', {})
    # GET
    if request.method == 'GET':
        return render(request, 'communicate/index.html', {})

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, 'communicate/index.html', {})

def report_user(request):
    # Add Welcome Message
    context = {}
    return render(request, 'communicate/index.html', context)
