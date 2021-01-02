from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

from ..models import Conversation

def index(request):
    context = {}
    if request.user.is_authenticated:
        # send active conversation_id
        conversations = Conversation.objects.filter(is_active=True, users__in=[request.user])
        if len(conversations) == 1:
            conversation_id = conversations[0].id
            context = {'active_conversation_id' : conversation_id}

        # send inactive conversations
        inactive_conversations = Conversation.objects.filter(Q(is_active=False) & Q(users__in=[request.user]) & ~Q(users_deleted__in=[request.user]))
        if len(inactive_conversations) > 0:
            # format
            history_conversations = []
            for conversation in reversed(inactive_conversations):
                date = conversation.datetime_start.strftime('%Y-%m-%d')
                duration = str(conversation.datetime_end - conversation.datetime_start)
                duration = duration.split('.')[0]
                history_conversations.append({
                    'id' : conversation.id,
                    'date' : date,
                    'duration' : duration
                })
            context['history_conversations'] = history_conversations

    return render(request, 'communicate/index.html', context)

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
        # get parameters
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
        except KeyError:
            context = {'error_message' : 'Some form item is not found'}
            return render(request, 'communicate/signup.html', context)

        # no duplicate user
        user = None
        try:
            user = User.objects.get(username=email)
        except User.DoesNotExist:
            pass
        if user is not None:
            context = {'error_message' : 'The Email is already taken'}
            return render(request, 'communicate/signup.html', context)
        else:
            # create user and login
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=email, email=email, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('communicate:index'))

def user_login(request):
    # GET
    if request.method == 'GET':
        return render(request, 'communicate/index.html', {})

    # POST
    if request.method == 'POST':
        if request.user.is_authenticated:
            return render(request, 'communicate/index.html', {})
        else:
            # get parameters
            try:
                email = request.POST['email']
                password = request.POST['password']
            except KeyError:
                context = {'error_message' : 'Invalid Login Information'}
                return render(request, 'communicate/index.html', context)

            # authenticate
            user = authenticate(request, username=email, password=password)

            # login
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('communicate:index'))
            else:
                # user exists
                context = {'error_message' : 'Invalid Login Information'}
                return render(request, 'communicate/index.html', context)

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect(reverse('communicate:index'))

def report_user(request):
    # Add Welcome Message
    context = {}
    return render(request, 'communicate/index.html', context)
