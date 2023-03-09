from django.contrib import admin

# Register your models here.

from .models import Rooms, Messages, Profile, Members

admin.site.register(Rooms)
admin.site.register(Messages)
admin.site.register(Profile)
admin.site.register(Members)