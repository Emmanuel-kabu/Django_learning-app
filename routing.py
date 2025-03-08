from django.urls import path
from .MylearningApp import ChitChatterconsumer

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', ChitChatterconsumer.as_asgi()),
]