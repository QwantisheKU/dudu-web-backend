from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


class UserModel(AbstractUser):
    username = None
    email = models.EmailField(max_length=128, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
