from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
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

class Rank(models.Model):
    # 6
    name = models.CharField(max_length=50, unique=True)
    rank_types = (('OR','Other Rank'),('NC','Non Commisioned Officer'),('OF','Officer'))
    abbreviation = models.CharField(max_length=50, blank=True)
    rank_class = models.CharField(max_length=2, blank=True, choices=rank_types,default='Other Rank')

    def __str__(self):
        return self.Name


class PowCamp(models.Model):
    name = models.CharField(max_length=255, unique=True, default='')
    nearest_city = models.CharField(max_length=255, unique=False, default='')
    notes = models.CharField(max_length=255, unique=False, default='')
    country = models.ForeignKey('Country', to_field='country_number', on_delete=models.CASCADE, related_name='powcamps')
    wartime_country = models.CharField(max_length=255, unique=False, default='')
    latitude = models.CharField(max_length=255, unique=False, default='')
    longitude = models.CharField(max_length=255, unique=False, default='')

    def __str__(self):
        return self.name


class Theatre(models.Model):
    # 11
    name = models.CharField(max_length=255, unique=True, default='')
    def __str__(self):
        return self.name

class Soldier(models.Model):
    # 10
    surname = models.CharField(max_length=255, unique=False, default='')
    initials = models.CharField(max_length=255, unique=False, default='')
    army_number = models.CharField(max_length=255, unique=False, default='')
    rank = models.ForeignKey('Rank', on_delete=models.CASCADE)
    notes = models.CharField(max_length=255, unique=False, default='')

    def __str__(self):
        return self.surname

class SoldierImprisonment(models.Model):
    # 9
    soldier = models.ForeignKey('Soldier', on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    pow_number = models.CharField(max_length=255, unique=False, default='')
    pow_camp = models.ForeignKey('PowCamp', on_delete=models.CASCADE)
    dateFrom = models.DateField() # dateFrom
    dateTo = models.DateField() # dateTo
    notes = models.CharField(max_length=255, unique=False, default='')


class SoldierDecoration(models.Model):
    # 8
    name =  models.CharField(max_length=255, unique=True, default='')
    notes = models.CharField(max_length=255, unique=False, default='')
    country_id = models.ForeignKey('Country', on_delete=models.CASCADE)
    details_link = models.CharField(max_length=255, unique=False, default='')
    abbreviation = models.CharField(max_length=255, unique=False, default='')

class Company(models.Model):
    # 2
    name = models.CharField(max_length=255, unique=True, default='')
    notes = models.CharField(max_length=255, unique=False, default='')

    def __str__(self):
        return self.name
        

class Cemetery(models.Model):
    # 1
    name = models.CharField(max_length=255, unique=True, default='')
    country = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='cemeteries')
    latitude = models.CharField(max_length=255, unique=False, default='') # latitude
    longitude = models.CharField(max_length=255, unique=False, default='') # longitude

    def __str__(self):
        return self.name


class Decoration(models.Model):
    # 4
    name = models.CharField(max_length=255, unique=True, default='')
    notes  = models.CharField(max_length=255, unique=False, default='')
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    details_link = models.CharField(max_length=255, unique=False, default='')
    abbreviation = models.CharField(max_length=255, unique=False, default='')

    def __str__(self):
        return self.Name

class Country(models.Model):
    # 3
    name = models.CharField(max_length=255, unique=True, default='')
    alpha2 = models.CharField(max_length=2, unique=True, default='')
    alpha3 = models.CharField(max_length=3, unique=True, default='')
    country_number = models.CharField(max_length=3, unique=True)
    flag = models.CharField(max_length=255,  default='')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('countries', args=[str(self.id)])