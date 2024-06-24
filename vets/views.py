from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import VetCreationForm, VetLoginForm
from .models import Vet
from django.contrib.auth import get_user_model
from .auth_backends import VetBackend


def register_vet(request):
    if request.method == 'POST':
        form = VetCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()

            # Set the backend for the user
            user.backend = 'vets.auth_backends.VetBackend'

            # Authenticate the user
            user = authenticate(
                username=form.cleaned_data['username'], password=form.cleaned_data['password1'], backend=user.backend)

            if user is not None:
                login(request, user, backend='vets.auth_backends.VetBackend')
                return redirect('vets:doctor_dashboard', vet_id=user.id)
    else:
        form = VetCreationForm()
    return render(request, 'drl.html', {'form': form, 'login_form': VetLoginForm()})


def login_vet(request):
    if request.method == 'POST':
        form = VetLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user, backend='vets.auth_backends.VetBackend')
                return redirect('vets:doctor_dashboard', vet_id=user.id)
    else:
        form = VetLoginForm()
    return render(request, 'drl.html', {'login_form': form, 'form': VetCreationForm()})


def password_reset(request):
    return render(request, 'pass_reset.html')


def doctor_dashboard(request, vet_id):
    vet = Vet.objects.get(id=vet_id)
    return render(request, 'doctor_dashboard.html', {'vet': vet})
