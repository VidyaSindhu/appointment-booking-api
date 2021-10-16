from typing import Callable
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    # username = None
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=250, null=False)
    address = models.CharField(max_length=250, null=False)
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class StaffSchedule(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, on_delete=CASCADE)
    user_from = models.TimeField(TIME_INPUT_FORMATS = ('%I:%M %p',))
    user_to = models.TimeField(TIME_INPUT_FORMATS = ('%I:%M %p',))