from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Vet


class VetCreationForm(UserCreationForm):
    class Meta:
        model = Vet
        fields = ('username', 'password1', 'password2', 'name')


class VetLoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label=("Password"), strip=False, widget=forms.PasswordInput)
