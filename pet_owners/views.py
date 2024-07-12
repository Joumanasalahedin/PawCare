# pet_owners/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import PetOwnerCreationForm, PetOwnerLoginForm, PetForm
from .models import PetOwner, Pet


def register_owner(request):
    if request.method == 'POST':
        form = PetOwnerCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()

            # Authenticate the user
            user = authenticate(
                username=form.cleaned_data['username'], password=form.cleaned_data['password1'])

            if user is not None:
                login(request, user,
                      backend='pet_owners.auth_backends.PetOwnersBackend')
                return redirect('pet_owners:user_dashboard', owner_id=user.id)
            else:
                print("Authentication failed")  # Debug statement
        else:
            print("Form is invalid")  # Debug statement
            print(form.errors)  # Print form errors for debugging
    else:
        form = PetOwnerCreationForm()
    return render(request, 'prl.html', {'form': form, 'login_form': PetOwnerLoginForm()})


def login_owner(request):
    if request.method == 'POST':
        form = PetOwnerLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user,
                      backend='pet_owners.auth_backends.PetOwnersBackend')
                return redirect('pet_owners:user_dashboard', owner_id=user.id)
    else:
        form = PetOwnerLoginForm()
    return render(request, 'prl.html', {'login_form': form, 'form': PetOwnerCreationForm()})


@login_required
def user_dashboard(request, owner_id):
    owner = PetOwner.objects.get(id=owner_id)  # Fetch the PetOwner instance

    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner = owner  # Set the pet owner to the PetOwner instance
            pet.save()
            # Redirect to the same page after saving
            return redirect('pet_owners:user_dashboard', owner_id=owner.id)
    else:
        form = PetForm()

    pets = Pet.objects.filter(owner=owner)  # Filter pets by the owner

    return render(request, 'user_dashboard.html', {'form': form, 'pets': pets, 'owner': owner})

