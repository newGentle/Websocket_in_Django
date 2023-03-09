from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Rooms, Members
from django.conf import settings


@receiver(post_save, sender=User)
def create_userprofile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

@receiver(post_save, sender=User)
def save_userprofile(sender, instance, **kwargs):
    if not instance.is_superuser:
        instance.profile.save()

@receiver(post_save, sender=Rooms)
def save_room(sender, instance, **kwargs):
    member = Profile.objects.get(id=instance.creator.id)
    room = Rooms.objects.get(id=instance.id)
    Members.objects.create(chatRoom=room, userProfile=member)
    
def createProfile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])
        post_save.connect(createProfile, sender=User)