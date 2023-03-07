from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from .serializers import MessagesSerializer, RoomsSerializer
# from rest_framework.decorators import 
from .models import Messages, Rooms, UsersProfile
from .forms import RoomForm
from django.contrib.auth.models import User, AnonymousUser


# Create your views here.

# class MessagesApiView(ListAPIView):
#     def get(self, request):
#         msg = Messages.objects.all()
#         return render(request, template_name='index.html',context={'msg': MessagesSerializer(msg, many=True).data})

#     def post(self, request):
#         serializer = MessagesSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return render(request, template_name="index.html" )

#     def put(self, response):
#         pass

class RoomsApiView(ListCreateAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer


class RoomApiView(APIView):
    def get(self, request, slug):
        room = Rooms.objects.get(slug=slug)
        return Response({'room': RoomsSerializer(room).data})

def index(request):
    rooms = Rooms.objects.all().count()
    users = UsersProfile.objects.all().count()
    return render(request, template_name='index.html', context={'chat_rooms_count': rooms, 'users_count': users})

# @login_required
def room(request, slug):
    room = Rooms.objects.get(slug=slug)
    return render(request, template_name='room.html', context={'chat_room': room})


def rooms(request):
    rooms = Rooms.objects.all()
    return render(request, template_name='rooms.html', context={'chat_rooms': rooms})

def room_create(request):
    form = RoomForm
    return render(request, template_name='room_create.html', context={'form': form})