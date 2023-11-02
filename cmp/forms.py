from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import CustomUser
from .models import Country
from .models import Rank

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class editCountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = "__all__"

class editRankForm(forms.ModelForm):
    class Meta:
        model = Rank
        fields = "__all__"

