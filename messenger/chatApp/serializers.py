from rest_framework import serializers
from .models import Messages, Rooms, Profile, Members
from django.contrib.auth.models import User
from rest_framework.relations import RelatedField


# class UserNameSerializer(serializers.Serializer):
# #     def to_native(self, value):
        
# #         return value
    
#     # def to_rooms(self, value):
#     #     print(value)
#     #     return value
    # username = RelatedField(source='user.username', read_only=True, many=True)
    # class Meta:
    #     model = User
    #     fields = ('username',)


class UsersProfileSerializer(serializers.ModelSerializer):
    # username = UserNameSerializer(many=True, read_only=True)
    # avatar = RelatedField(source='profile.avatar', read_only=True, many=True)
    class Meta:
        model = Profile
        fields = ('avatar',)
    
        
class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ('__all__')


class RoomsSerializer(serializers.ModelSerializer):
    # room_members = serializers.SerializerMethodField('get_members')
    
    class Meta:
        model = Rooms
        fields = ['name', 'creator']
        
    # def get_members(self, instance):
    #     room_members = instance
    #     return room_members

class MembersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Members
        fields = ('__all__')
        
