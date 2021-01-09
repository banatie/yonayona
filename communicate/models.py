from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    # config
    id_bgm_on = models.BooleanField(default=True)

class Conversation(models.Model):
    is_active = models.BooleanField(default=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, max_length=2, related_name='users')
    users_deleted = models.ManyToManyField(settings.AUTH_USER_MODEL, max_length=2, related_name='users_deleted')
    datetime_start = models.DateTimeField(auto_now_add=True)
    datetime_end = models.DateTimeField(auto_now=True)
    duration_in_sec = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(24*60*60)], default=0)

class Message(models.Model):
    user_from = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.text
