from django.shortcuts import render, get_object_or_404
from .models import Vet


def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html')
