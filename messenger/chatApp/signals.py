from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UsersProfile
from django.conf import settings


@receiver(post_save, sender=User)
def create_userprofile(sender, instance, created, **kwargs):
    if created:
        UsersProfile.objects.create(user = instance)

@receiver(post_save, sender=User)
def save_userprofile(sender, instance, **kwargs):
    if not instance.is_superuser:
        instance.usersprofile.save()

