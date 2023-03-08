from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class UsersProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='avatar_img')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Messages(models.Model):
    author = models.ForeignKey(UsersProfile, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey('Rooms', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Rooms(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    created = models.DateField(auto_now_add=True)
    members = models.ManyToManyField(UsersProfile, through='RoomsMembers', blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

    def __str__(self):

        return f'{self.name}'
        

class RoomsMembers(models.Model):
    userProfile = models.ForeignKey(UsersProfile, on_delete=models.CASCADE)
    chatRoom = models.ForeignKey(Rooms, on_delete=models.CASCADE)
        
