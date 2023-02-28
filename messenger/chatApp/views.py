from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MessageSerializer, RoomSerializer
from .models import Message, Room
# Create your views here.

class MessageApiView(APIView):
    def get(self, request):
        msg = Message.objects.all()
        return Response({'messages': MessageSerializer(msg, many=True).data})

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer)
        return Response(serializer.data)

    def put(self, response):
        pass

class RoomApiView(APIView):
    def get(self, request):
        room = Room.objects.all().order_by('-created')
        return Response({'rooms': RoomSerializer(room, many=True).data})
