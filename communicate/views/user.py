from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout

from ..models import Conversation
from ..models import Message
from ..utils import conversation_queries

def index(request):
    context = {}
    if request.user.is_authenticated:
        # send active conversation_id
        conversations = Conversation.objects.filter(is_active=True, users__in=[request.user])
        if len(conversations) == 1:
            conversation = conversations[0]
            conversation_id = conversation.id
            context['active_conversation'] = {
                'id' : conversation_id,
                'user_count' : len(conversation.users.all())
            }

            # send message history
            messages = conversation_queries.get_message_history(conversation_id)
            if len(messages) > 0:
                context['messages_to_communicate'] = messages

        # send inactive conversations
        conversations = conversation_queries.get_inactive_conversations(user=request.user)
        context['history_conversations'] = conversations

    return render(request, 'communicate/index.html', context)

def about(request):
    context = {}
    return render(request, 'communicate/about.html', context)

def user_signup(request):
    if request.user.is_authenticated:
        # Already logged in
        context = {'error_message' : 'すでにログインしています'}
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
            context = {'error_message' : 'ログイン情報が正しくありません'}
            return render(request, 'communicate/signup.html', context)

        # no duplicate user
        user = None
        try:
            user = get_user_model().objects.get(username=email)
        except ObjectDoesNotExist:
            pass
        if user is not None:
            context = {'error_message' : 'メールアドレスがすでに登録されています'}
            return render(request, 'communicate/signup.html', context)
        else:
            # create user and login
            user = get_user_model().objects.create_user(first_name=first_name, last_name=last_name, username=email, email=email, password=password)
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
                context = {'error_message' : 'ログイン情報が正しくありません'}
                return render(request, 'communicate/index.html', context)

            # authenticate
            user = authenticate(request, username=email, password=password)

            # login
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('communicate:index'))
            else:
                # user exists
                context = {'error_message' : 'ログイン情報が正しくありません'}
                return render(request, 'communicate/index.html', context)

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect(reverse('communicate:index'))

def update_user_settings(request):
    if request.user.is_authenticated:
        try:
            user = get_user_model().objects.get(username=request.user.username)
            print(user.is_bgm_on)
            if request.GET['is_bgm_on'] == 'true':
                user.is_bgm_on = True
                print('TRUE')
            else:
                print('FALSE')
                user.is_bgm_on = False
            user.save()
        except:
            return JsonResponse({}, status=400)    
        return JsonResponse({}, status=200)

def report_user(request):
    # Add Welcome Message
    context = {}
    return render(request, 'communicate/index.html', context)
