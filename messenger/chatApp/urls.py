from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'rooms', RoomsViewSet)

urlpatterns = [
    path("rooms/", rooms, name='rooms'),
    path("rooms/<int:pk>/", room, name='room'),
    path('api/v1/', include(router.urls)),
    # path('api/v1/rooms/<int:pk>/', RoomsViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}), name='api_room'),
    path('', index, name='index'),
    path('room_create', room_create, name='room_create'),
    path('profile', profile, name='profile'),
    path('joinToRoom/<int:pk>', joinToRoom, name='joinToRoom'),
    path('outFromRoom/<int:pk>', outFromRoom, name='outFromRoom'),
    

]
