from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UsersProfile, Rooms
from django.conf import settings


@receiver(post_save, sender=User)
def create_userprofile(sender, instance, created, **kwargs):
    if created:
        UsersProfile.objects.create(user = instance)

@receiver(post_save, sender=User)
def save_userprofile(sender, instance, **kwargs):
    if not instance.is_superuser:
        instance.usersprofile.save()

@receiver(post_save, sender=Rooms)
def save_room(sender, instance, **kwargs):
    
    Rooms.objects.get(id=instance.id).members.add(UsersProfile.objects.get(user_id = instance.creator.id))
    
def createProfile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UsersProfile.objects.create(user=kwargs['instance'])
        post_save.connect(createProfile, sender=User)