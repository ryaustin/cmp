from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import CustomUser

from .models import Country
from .models import Rank
from .models import Cemetery

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class editCemeteryForm(forms.ModelForm):
    class Meta:
        model = Cemetery 
        fields = "__all__"


class editCountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = "__all__"


class editRankForm(forms.ModelForm):
    class Meta:
        model = Rank
        fields = "__all__"

