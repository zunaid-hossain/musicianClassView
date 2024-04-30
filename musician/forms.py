from django import forms
from .models import musician 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class musicianForm(forms.ModelForm):
    class Meta:
        model=musician
        fields='__all__'


class registerForm(UserCreationForm):

    class Meta:
        model =  User
        fields = ['username' , 'first_name', 'last_name', 'email']