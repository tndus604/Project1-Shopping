from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required='TRUE')

    class Meta:
        #if vaild it is going to create a User
        model = User
        fields = ['username', 'email', 'password1', 'password2' ]

