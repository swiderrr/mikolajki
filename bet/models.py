from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    wylosowany = models.CharField(max_length=25, blank=True,unique=True, null=True)
    czy_wylosowany = models.BooleanField(default=False)

    def __str__(self):
        return self.username