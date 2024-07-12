from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import VetCreationForm, VetLoginForm, AppointmentForm, PetForm, PetOwnerCreationForm
from .models import Vet, Appointments
from pet_owners.models import Pet, PetOwner
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils import timezone


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


@login_required
def doctor_dashboard(request, vet_id):
    vet = Vet.objects.get(id=vet_id)
    appointments = Appointments.objects.filter(vet=vet)

    # Calculate total number of pets
    total_pets = Pet.objects.filter(vet=vet).count()

    # Calculate number of appointments for today
    today = timezone.now().date()
    appointments_today = Appointments.objects.filter(
        vet=vet, date=today).count()

    if request.method == 'POST':
        if 'schedule_appointment' in request.POST:
            pet_id = request.POST.get('pet')
            appointment_date = request.POST.get('appointmentDate')
            appointment_time = request.POST.get('appointmentTime')
            reason = request.POST.get('reason')
            pet = Pet.objects.get(id=pet_id)

            appointment = Appointments.objects.create(
                pet=pet,
                vet=vet,
                date=appointment_date,
                time=appointment_time,
                complaints=reason,
            )
            appointment.save()

            return redirect('vets:doctor_dashboard', vet_id=vet.id)

        elif 'add_patient' in request.POST:
            pet_owner_form = PetOwnerCreationForm(request.POST)
            pet_form = PetForm(request.POST)

            if pet_owner_form.is_valid() and pet_form.is_valid():
                pet_owner = pet_owner_form.save(commit=False)
                pet_owner.set_password("Pawcare_temp123")
                pet_owner.save()

                pet = pet_form.save(commit=False)
                pet.name = request.POST.get('pet_name')
                pet.owner = pet_owner
                pet.vet = vet
                pet.save()

                return redirect('vets:doctor_dashboard', vet_id=vet.id)
    else:
        appointment_form = AppointmentForm(vet=vet)
        pet_owner_form = PetOwnerCreationForm()
        pet_form = PetForm()

    pets = Pet.objects.filter(vet=vet).distinct()
    return render(request, 'doctor_dashboard.html', {
        'appointment_form': appointment_form,
        'pet_owner_form': pet_owner_form,
        'pet_form': pet_form,
        'appointments': appointments,
        'pets': pets,
        'vet': vet,
        'total_pets': total_pets,
        'appointments_today': appointments_today,
    })


def vet_search(request):
    vets = Vet.objects.all()
    return render(request, 'vet_search.html', {'vets': vets})


def vet_results(request):
    location_query = request.GET.get('location', '')
    query = Q()

    if location_query:
        query &= (Q(city__icontains=location_query) |
                  Q(state__icontains=location_query) |
                  Q(PLZ__icontains=location_query))

    if not location_query:
        results = Vet.objects.all().order_by('city')
    else:
        results = Vet.objects.filter(query).order_by(
            'city') if query else Vet.objects.none()

    return render(request, 'vet_results.html', {'results': results})


def app_slots(request):
    return render(request, 'app_slots.html')
