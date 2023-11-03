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

class Rank(models.Model):
    # 6
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    rankTypes = (('OR','Other Rank'),('NC','Non Commisioned Officer'),('OF','Officer'))
    abbreviation = models.CharField(max_length=50, blank=True)
    rankClass = models.CharField(max_length=2, blank=True, choices=rankTypes,default='Other Rank')

    def __str__(self):
        return self.Name


class PowCamp(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, default='')
    nearestCity = models.CharField(max_length=255, unique=False, default='')
    notes = models.CharField(max_length=255, unique=False, default='')
    wartimeCountry = models.ForeignKey('Country', on_delete=models.CASCADE)
    presentCountry = models.CharField(max_length=255, unique=False, default='')
    latitude = models.FloatField() # latitude
    longitude = models.FloatField() # longitude

    def __str__(self):
        return self.name


class Theatre(models.Model):
    # 11
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, default='')
    def __str__(self):
        return self.name

class Soldier(models.Model):
    # 10
    id = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=255, unique=False, default='')
    initials = models.CharField(max_length=255, unique=False, default='')
    army_number = models.CharField(max_length=255, unique=False, default='')
    rank_id = models.ForeignKey('Rank', on_delete=models.CASCADE)
    notes = models.CharField(max_length=255, unique=False, default='')

    def __str__(self):
        return self.surname

class SoldierImprisonment(models.Model):
    # 9
    id = models.IntegerField(primary_key=True)
    soldier_id = models.ForeignKey('Soldier', on_delete=models.CASCADE)
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE)
    powNumber = models.CharField(max_length=255, unique=False, default='')
    powCamp_id = models.ForeignKey('PowCamp', on_delete=models.CASCADE)
    dateFrom = models.DateField() # dateFrom
    dateTo = models.DateField() # dateTo
    notes = models.CharField(max_length=255, unique=False, default='')


class SoldierDecoration(models.Model):
    # 8
    id = models.IntegerField(primary_key=True)
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
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, default='')
    country = models.ForeignKey('Country', to_field='CountryNumber', on_delete=models.CASCADE)
    latitude = models.CharField(max_length=255, unique=False, default='') # latitude
    longitude = models.CharField(max_length=255, unique=False, default='') # longitude

    def __str__(self):
        return self.name


class Decoration(models.Model):
    # 4
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, default='')
    notes = models.CharField(max_length=255, unique=False, default='')
    country_id = models.ForeignKey('Country', on_delete=models.CASCADE)
    details_link = models.CharField(max_length=255, unique=False, default='')
    abbreviation = models.CharField(max_length=255, unique=False, default='')

    def __str__(self):
        return self.Name

class Country(models.Model):
    # 3
    name = models.CharField(max_length=255, unique=True, default='')
    Alpha2 = models.CharField(max_length=2, unique=True, default='')
    Alpha3 = models.CharField(max_length=3, unique=True, default='')
    CountryNumber = models.CharField(max_length=3, unique=True, default='')
    Flag = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name