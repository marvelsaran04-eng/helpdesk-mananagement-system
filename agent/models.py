
# models.py

# Create your models here.


from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER = 'user'
    AGENT = 'agent'
    ROLE_CHOICES = (
        (USER, 'User'),
        (AGENT, 'Agent'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=USER)

