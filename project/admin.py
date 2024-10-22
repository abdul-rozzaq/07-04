from django.contrib import admin
from .models import Profile, Theme, Message

admin.site.register(Theme)
admin.site.register(Message)
admin.site.register(Profile)
