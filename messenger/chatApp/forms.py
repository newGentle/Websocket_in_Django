from django.forms.models import ModelForm
from .models import Rooms
class RoomForm(ModelForm):
    class Meta:
        model = Rooms
        fields = ('name',)
        