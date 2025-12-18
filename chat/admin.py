from django.contrib import admin

# Register your models here.
from .models import Message,PrivateMessage

admin.site.register(Message)
admin.site.register(PrivateMessage)