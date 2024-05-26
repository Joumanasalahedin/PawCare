from django.shortcuts import render
from .models import Vet


def home(request):
    vets = Vet.objects.all()
    return render(request, 'home.html', {'vets': vets})
