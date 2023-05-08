from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form_input'}))
    email = forms.EmailField(label='Электронный адрес', widget=forms.EmailInput(attrs={'class':'form_input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form_input'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class':'form_input'}))
    class Meta:
        model = User
        fields = ('username','email','password1','password2')



class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form_input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form_input'}))
    