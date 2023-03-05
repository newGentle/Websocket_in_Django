from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("rooms/", rooms, name='rooms'),
    path("rooms/<slug:slug>", room, name='room'),
    path('api/rooms/', RoomsApiView.as_view(), name='api_rooms'),
    path('api/rooms/<slug:slug>/', RoomApiView.as_view(), name='api_room'),
    path('', index, name='index'),
    path('room_create', room_create, name='room_create')

]
