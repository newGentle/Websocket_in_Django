from rest_framework import serializers
from .models import Messages, Rooms, UsersProfile
from django.contrib.auth.models import User

class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class UsersProfileSerializer(serializers.ModelSerializer):
    username = UserNameSerializer(many=True, read_only=True)
    class Meta:
        model = UsersProfile
        fields = ('avatar', 'username',)

        
class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ('__all__')


class RoomsSerializer(serializers.ModelSerializer):
    profile = UsersProfileSerializer(many=True, read_only=True)
    class Meta:
        model = Rooms
        fields = ('slug', 'created', 'creator', 'profile','members')
        
