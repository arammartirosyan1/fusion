from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CarParts


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CarPartsAddForm(ModelForm):
    class Meta:
        model = CarParts
        fields = ('photo', 'description', 'value')
