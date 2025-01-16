"""
ASGI config for myproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing  # Import the chat app's routing

# Set the default settings module for the 'django' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Define the ASGI application to handle both HTTP and WebSocket protocols
application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Standard HTTP request handling (for Django's normal views)
    
    # WebSocket handling
    "websocket": AuthMiddlewareStack(  # This ensures that the WebSocket connection is authenticated
        URLRouter(  # This allows us to define the routing for WebSocket connections
            chat.routing.websocket_urlpatterns  # Use the WebSocket URL routing from the 'chat' app
        )
    ),
})
