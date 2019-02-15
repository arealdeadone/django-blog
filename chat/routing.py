from django.urls import path
from . import consumers
from channels.routing import URLRouter

websocket_urls = URLRouter([
    path('<str:room_name>/', consumers.ChatConsumer),
    # url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
])
