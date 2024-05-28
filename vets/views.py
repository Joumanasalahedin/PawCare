from django.shortcuts import render, get_object_or_404
from .models import Vet


def doc_register_login(request):
    return render(request, 'drl.html')


def password_reset(request):
    return render(request, 'pass_reset.html')


def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html')
