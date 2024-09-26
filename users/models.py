from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    username = models.CharField(max_length=30, blank=True, null=True) # I had to create this username key here in other to make it null
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    is_admin = models.BooleanField(default=False)  # Boolean field for admin status

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email



