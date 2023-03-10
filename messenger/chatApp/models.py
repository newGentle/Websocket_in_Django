from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='avatar_img')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.user.username


class Messages(models.Model):
    message_sender = models.ForeignKey(Profile, on_delete=models.CASCADE)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey('Rooms', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Rooms(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    created = models.DateField(auto_now_add=True)
    # members = models.ManyToManyFieldProfile, through='RoomsMembers', blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

    def __str__(self):

        return f'{self.name}'
        

class Members(models.Model):
    userProfile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    chatRoom = models.ForeignKey(Rooms, on_delete=models.CASCADE)
        
