from django import forms
from .models import Rooms, Profile
from django.contrib.auth.models import User


class RoomForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = ('__all__')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar',)