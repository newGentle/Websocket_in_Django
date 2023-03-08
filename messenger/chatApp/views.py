from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .serializers import MessagesSerializer, RoomsSerializer
from django.contrib.auth.decorators import login_required, permission_required
from .models import Messages, Rooms, UsersProfile, RoomsMembers
from .forms import RoomForm, ProfileForm, EditProfileForm
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



class RoomApiView(RetrieveUpdateDestroyAPIView):
    # queryset = Rooms.objects.all()
    # serializer_class = RoomsSerializer
    def get(self, request, slug):
        room = Rooms.objects.get(slug=slug)
        return Response({'room': RoomsSerializer(room).data})


def index(request):
    rooms = Rooms.objects.all().count()
    users = UsersProfile.objects.all().count()
    return render(request, template_name='index.html', context={'chat_rooms_count': rooms, 'users_count': users})

@login_required
def room(request, slug):
    room = Rooms.objects.get(slug=slug)
    return render(request, template_name='room.html', context={'chat_room': room})

@login_required(login_url='/accounts/login/')
def rooms(request):
    rooms = Rooms.objects.all()
    return render(request, template_name='rooms.html', context={'chat_rooms': rooms})

@login_required
def room_create(request):
    form = RoomForm
    return render(request, template_name='room_create.html', context={'form': form})

@login_required
def profile(request):
    
    if request.method == 'POST':
        user_form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.usersprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form = user_form.save()
            profile_form = profile_form.save(commit=False)
            profile_form.user = user_form
            profile_form.save()
            return redirect('/')
    else:
        user_form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.usersprofile)
        args = {}
        args['user_form'] = user_form
        args['profile_form'] = profile_form
        return render(request, template_name='profile.html', context=args)
    