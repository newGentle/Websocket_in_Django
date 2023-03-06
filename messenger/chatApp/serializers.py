from rest_framework import serializers
from .models import Messages, Rooms, UsersProfile


class UsersProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersProfile
        fields = ('__all__')

        
class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ('__all__')


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ('__all__')
        
