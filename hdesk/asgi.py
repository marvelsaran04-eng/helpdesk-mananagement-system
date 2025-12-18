"""
ASGI config for hdesk project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hdesk.settings')

# Get the default ASGI application
django_asgi_app = get_asgi_application()

# Define the WebSocket routing
application = ProtocolTypeRouter({
    'http': django_asgi_app,  # Default HTTP routing
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns 
            
        )
    ),
})
