from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from chatApp import consumers
from django.core.asgi import get_asgi_application

websocket_urlpatterns=[
                    path(
                        "ws/<str:chat_room_name>)", consumers.ChatRoomConsumers.as_asgi()
                    ),
                ]

application = ProtocolTypeRouter( 
    {
        'http': get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
               websocket_urlpatterns
            )
        ),
    }
)