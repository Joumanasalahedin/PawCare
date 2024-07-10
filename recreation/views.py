from django.shortcuts import render
from .models import Recreation
from django.db.models import Q


def rec_search(request):
    activities = Recreation.objects.all()
    return render(request, 'rec_search.html', {'activities': activities})


def rec_results(request):
    search_query = request.GET.get('search', '')
    location_query = request.GET.get('location', '')

    query = Q()

    if search_query:
        category_matches = [
            value for value, display in Recreation.CATEGORY_CHOICES if search_query in display.lower()
        ]

        query &= (Q(name__icontains=search_query) |
                  Q(category__in=category_matches) |
                  Q(category__icontains=search_query))
    if location_query:
        query &= (Q(city__icontains=location_query) |
                  Q(state__icontains=location_query) |
                  Q(PLZ__icontains=location_query))

    if not search_query and not location_query:
        results = Recreation.objects.all().order_by('city')
    else:
        results = Recreation.objects.filter(query).order_by(
            'city') if query else Recreation.objects.none()

    return render(request, 'rec_results.html', {'results': results})
