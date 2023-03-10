from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import  RoomsSerializer
from django.contrib.auth.decorators import login_required
from .models import Messages, Rooms, Profile, Members
from .forms import RoomForm, ProfileForm, EditProfileForm
from django.contrib.auth.models import User
from django.conf import settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import BasicAuthentication


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


class RoomsViewSet(ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (BasicAuthentication,)
    

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     print(instance, kwargs)
    #     return Response(self.serializer_class(instance).data)
    

# class RoomsApiView(ListCreateAPIView):
#     queryset = Rooms.objects.all()
#     serializer_class = RoomsSerializer



# class RoomApiView(APIView):
#     # queryset = Rooms.objects.all()
#     # serializer_class = RoomsSerializer
#     def get(self, request, slug):
#         room = Rooms.objects.get(slug=slug)
#         print(RoomsSerializer(room).data)
#         return Response({'room': RoomsSerializer(room).data})


def index(request):
    rooms = Rooms.objects.all().count()
    users = Profile.objects.all().count()
    return render(request, template_name='index.html', context={'chat_rooms_count': rooms, 'users_count': users})

@login_required
def room(request, pk):
    room = Rooms.objects.get(pk=pk)
    members = Members.objects.filter(chatRoom_id = pk)
    messages = Messages.objects.filter(room=room)
    # username = members
    username = []
    avatar = []
    for item in members:
        username += User.objects.filter(id=item.userProfile_id).values('username')
        avatar += Profile.objects.filter(user_id=item.userProfile_id).values('avatar')
    
    profile = zip(username, avatar)
    media_url = settings.MEDIA_URL
    context={
        'chat_room': room, 
        'members': profile, 
        'media': media_url,
        'messages': messages,
        }
    # print('test', members)
    return render(request, template_name='room.html', context=context)

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
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form = user_form.save()
            profile_form = profile_form.save(commit=False)
            profile_form.user = user_form
            profile_form.save()
            return redirect('/')
    else:
        user_form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        args = {}
        args['user_form'] = user_form
        args['profile_form'] = profile_form
        return render(request, template_name='profile.html', context=args)
    