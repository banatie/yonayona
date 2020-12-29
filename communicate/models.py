from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Message(models.Model):
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_from')
    user_to = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_to')
    datetime_created = models.DateTimeField(auto_now_add=True)
    delete_by_user_from = models.BooleanField(default=False)
    delete_by_user_to = models.BooleanField(default=False)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.text

class Conversation(models.Model):
    users = models.ManyToManyField(User, max_length=2)
    datetime_start = models.DateTimeField(auto_now_add=True)
    datetime_end = models.DateTimeField(auto_now=True)
    duration_in_sec = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(24*60*60)])

    def __str__(self):
        return f'{self.user1} to {self.user2} @ {self.datetime_start} to {self.datetime_end}'
