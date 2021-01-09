from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Message, Conversation


admin.site.register(User, UserAdmin)
admin.site.register(Message)
admin.site.register(Conversation)