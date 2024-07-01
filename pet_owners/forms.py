from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import PetOwner


class PetOwnerCreationForm(UserCreationForm):
    class Meta:
        model = PetOwner
        fields = ('username', 'email', 'password1', 'password2')


class PetOwnerLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label=("Password"), strip=False, widget=forms.PasswordInput)
