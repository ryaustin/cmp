from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Country(models.Model):
    name = models.CharField(max_length=50)
    old_id = models.IntegerField(null=True, blank=True)
    alpha2  = models.CharField(max_length=2, null=False, blank=False)
    alpha3  = models.CharField(max_length=3, null=False, blank=False)

    def __str__(self):
        return self.name

