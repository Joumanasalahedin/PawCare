from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Vet, Appointments
from pet_owners.models import Pet, PetOwner


class VetCreationForm(UserCreationForm):
    class Meta:
        model = Vet
        fields = ('username', 'name', 'password1', 'password2')


class VetLoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label=("Password"), strip=False, widget=forms.PasswordInput)


class AppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        vet = kwargs.pop('vet', None)
        super(AppointmentForm, self).__init__(*args, **kwargs)
        if vet:
            self.fields['pet'].queryset = Pet.objects.filter(
                pet_appointments__vet=vet).distinct()

    class Meta:
        model = Appointments
        fields = ['pet', 'date', 'time', 'complaints']


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'breed', 'age', 'gender']


class PetOwnerCreationForm(forms.ModelForm):
    class Meta:
        model = PetOwner
        fields = ['name', 'username', 'email', 'phone_number']
