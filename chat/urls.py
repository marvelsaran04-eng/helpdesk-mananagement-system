from .routing import websocket_urlpatterns
from channels.routing import ProtocolTypeRouter, URLRouter


application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns),
})