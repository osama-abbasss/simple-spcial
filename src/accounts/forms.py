from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from . import models

class UserCreateForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2' ]


class ProfileFrorm(forms.ModelForm):

    class Meta:
        model  = models.Profile
        fields = ['PROImg', 'PROGender', 'PROCountry', 'PROAddress']
