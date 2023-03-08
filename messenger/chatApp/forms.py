from django import forms
from .models import Rooms, UsersProfile
from django.contrib.auth.models import User


class RoomForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = ('name',)


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UsersProfile
        fields = ('avatar',)