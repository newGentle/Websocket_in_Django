from django.forms.models import ModelForm
from .models import Rooms, UsersProfile
from django.contrib.auth.models import User


class RoomForm(ModelForm):
    class Meta:
        model = Rooms
        fields = ('name',)


class ProfileForm(ModelForm):
    class Meta:
        model = UsersProfile
        fields = ('avatar',)