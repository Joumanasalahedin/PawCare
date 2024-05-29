from django.shortcuts import render
from django.db.models import Q
from vets.models import Vet


def home(request):
    vets = Vet.objects.all()
    return render(request, 'home.html', {'vets': vets})


def search(request):
    search_query = request.GET.get('search', '')
    location_query = request.GET.get('location', '')

    query = Q()

    if search_query:
        query &= Q(name__icontains=search_query)

    if location_query:
        query &= (Q(city__icontains=location_query) |
                  Q(state__icontains=location_query) |
                  Q(PLZ__icontains=location_query))

    if not search_query and not location_query:
        results = Vet.objects.all().order_by('city')
    else:
        results = Vet.objects.filter(query).order_by(
            'city') if query else Vet.objects.none()

    return render(request, 'search.html', {'results': results})
