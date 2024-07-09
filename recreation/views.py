from django.shortcuts import render
from .models import Recreation
from django.db.models import Q


def rec_search(request):
    activities = Recreation.objects.all()
    return render(request, 'rec_search.html', {'activities': activities})
