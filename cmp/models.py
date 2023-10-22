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
    name_common = models.CharField(max_length=255, unique=False, default='')
    name_official = models.CharField(max_length=255, unique=False, default='')
    tld = models.CharField(max_length=10, unique=False, default='')
    cca2 = models.CharField(max_length=2, unique=True, default='')
    ccn3 = models.CharField(max_length=3, unique=True, default='')
    cca3 = models.CharField(max_length=3, unique=True, default='')
    cioc = models.CharField(max_length=3, unique=False, default='')
    independent = models.BooleanField( default=True)
    status = models.CharField(max_length=255, default='')
    unMember = models.BooleanField(default=True)
    currencies = models.CharField(max_length=255, default='')
    idd_root = models.CharField(max_length=10, default='')
    idd_suffixes = models.CharField(max_length=255, default='')
    capital = models.CharField(max_length=255, default='')
    alt_spellings = models.CharField(max_length=255, default='')
    region = models.CharField(max_length=255, default='')
    subregion = models.CharField(max_length=255, default='')
    languages = models.CharField(max_length=255, default='')
    translations_ces_official = models.CharField(max_length=255, default='')
    translations_ces_common = models.CharField(max_length=255, default='')
    translations_deu_official = models.CharField(max_length=255, default='')
    translations_deu_common = models.CharField(max_length=255, default='')
    translations_est_official = models.CharField(max_length=255, default='')
    translations_est_common = models.CharField(max_length=255, default='')
    translations_fin_official = models.CharField(max_length=255, default='')
    translations_fin_common = models.CharField(max_length=255, default='')
    translations_fra_official = models.CharField(max_length=255, default='')
    translations_fra_common = models.CharField(max_length=255, default='')
    translations_hrv_official = models.CharField(max_length=255, default='')
    translations_hrv_common = models.CharField(max_length=255, default='')
    translations_hun_official = models.CharField(max_length=255, default='')
    translations_hun_common = models.CharField(max_length=255, default='')
    translations_ita_official = models.CharField(max_length=255, default='')
    translations_ita_common = models.CharField(max_length=255, default='')
    translations_jpn_official = models.CharField(max_length=255, default='')
    translations_jpn_common = models.CharField(max_length=255, default='')
    translations_kor_official = models.CharField(max_length=255, default='')
    translations_kor_common = models.CharField(max_length=255, default='')
    translations_nld_official = models.CharField(max_length=255, default='')
    translations_nld_common = models.CharField(max_length=255, default='')
    translations_per_official = models.CharField(max_length=255, default='')
    translations_per_common = models.CharField(max_length=255, default='')
    translations_pol_official = models.CharField(max_length=255, default='')
    translations_pol_common = models.CharField(max_length=255, default='')
    translations_por_official = models.CharField(max_length=255, default='')
    translations_por_common = models.CharField(max_length=255, default='')
    translations_rus_official = models.CharField(max_length=255, default='')
    translations_rus_common = models.CharField(max_length=255, default='')
    translations_slk_official = models.CharField(max_length=255, default='')
    translations_slk_common = models.CharField(max_length=255, default='')
    translations_spa_official = models.CharField(max_length=255, default='')
    translations_spa_common = models.CharField(max_length=255, default='')
    translations_swe_official = models.CharField(max_length=255, default='')
    translations_swe_common = models.CharField(max_length=255, default='')
    translations_urd_official = models.CharField(max_length=255, default='')
    translations_urd_common = models.CharField(max_length=255, default='')
    translations_zho_official = models.CharField(max_length=255, default='')
    translations_zho_common = models.CharField(max_length=255, default='')
    latlng = models.CharField(max_length=255, default='')
    landlocked = models.BooleanField(default=False)
    borders = models.CharField(max_length=255, default='')
    area = models.FloatField(default=0.0)
    flag = models.CharField(max_length=255, default='')
    demonyms_eng_f = models.CharField(max_length=255, default='')
    demonyms_eng_m = models.CharField(max_length=255, default='')
    demonyms_fra_f = models.CharField(max_length=255, default='')
    demonyms_fra_m = models.CharField(max_length=255, default='')
    callingCodes = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name_common