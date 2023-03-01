from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MessagesSerializer, RoomsSerializer
from .models import Messages, Rooms
# Create your views here.

class MessagesApiView(APIView):
    def get(self, request):
        msg = Messages.objects.all()
        return render(request, template_name='index.html',context={'msg': MessagesSerializer(msg, many=True).data})

    def post(self, request):
        serializer = MessagesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return render(request, template_name="index.html" )

    def put(self, response):
        pass

class RoomsApiView(APIView):
    def get(self, request):
        rooms = Rooms.objects.all().order_by('-created')
        return render(request, template_name='index.html',context={'rooms': RoomsSerializer(rooms, many=True).data})


class RoomApiView(APIView):
    def get(self,request, slug):
        print(slug)
        room = Rooms.objects.get(slug=slug)
        return render(request, template_name='index.html', content_type={'room': RoomsSerializer(room).data})
