from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from .managers import CustomUserManager


class User(AbstractUser):
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_users_permissions')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    objects = CustomUserManager()
