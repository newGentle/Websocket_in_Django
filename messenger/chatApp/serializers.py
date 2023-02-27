from rest_framework import serializers
from .models import Message, Group

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('__all__')

