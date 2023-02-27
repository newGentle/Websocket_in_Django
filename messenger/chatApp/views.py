from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MessageSerializer
from .models import Message
# Create your views here.

class MessageApiView(APIView):
    def get(self, request):
        msg = Message.objects.all()
        return Response({'messages': MessageSerializer(msg, many=True).data})
