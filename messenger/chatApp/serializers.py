from rest_framework import serializers
from .models import Messages, Rooms, UsersProfile


class UsersProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersProfile
        fields = ('__all__')
    
    # def to_representation(self, instance):
    #     self.fields['members'] = MembersSerializer(many=True)
    #     return super().to_representation(instance)

        
class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ('__all__')


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ('__all__')
        
