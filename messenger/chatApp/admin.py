from django.contrib import admin

# Register your models here.

from .models import Rooms, Messages, UsersProfile

admin.site.register(Rooms)
admin.site.register(Messages)
admin.site.register(UsersProfile)