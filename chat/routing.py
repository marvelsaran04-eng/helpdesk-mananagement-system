# routing.py

from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/chat/', ChatConsumer.as_asgi()),
    
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns),
})
