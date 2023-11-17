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
        return self.name


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
    rank = models.ForeignKey('Rank', on_delete=models.CASCADE, related_name='ranks')
    notes = models.CharField(max_length=255, unique=False, default='')

    def __str__(self):
        return self.surname
    
    class Meta:
        ordering = ['surname']

class SoldierImprisonment(models.Model):
    # 9
    soldier = models.ForeignKey('Soldier', on_delete=models.CASCADE)
    legacy_company = models.CharField(max_length=255, unique=False, default='')
    pow_number = models.CharField(max_length=255, unique=False, default='')
    pow_camp = models.ForeignKey('PowCamp', on_delete=models.CASCADE)
    date_from = models.DateField(null=True, blank=True ) 
    date_to = models.DateField(null=True, blank=True)
    legacy_date_from = models.CharField(max_length=255, unique=False, default='')
    legacy_date_to = models.CharField(max_length=255, unique=False, default='')
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