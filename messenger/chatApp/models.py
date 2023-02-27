from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Chat_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default=None)


class Message(models.Model):
    author = models.ForeignKey(Chat_User, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)


class Room(models.Model):
    name = models.CharField(max_length=64)
    created = models.DateField(auto_now_add=True)
    members = models.ManyToManyField(Chat_User)



