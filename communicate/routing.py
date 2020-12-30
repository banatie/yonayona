from django.urls import re_path

from . import consumers


websocket_urlpatterns = [
    re_path(r'ws/communicate/(?P<username>\w+)/$', consumers.CommunicateConsumer.as_asgi()),
]
