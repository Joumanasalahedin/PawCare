from django.urls import path
from .views import doctor_dashboard, register_vet, login_vet, vet_search, vet_results, app_slots

app_name = 'vets'

urlpatterns = [
    path('dashboard/<int:vet_id>/', doctor_dashboard, name='doctor_dashboard'),
    path('register/', register_vet, name='register'),
    path('login/', login_vet, name='login'),
    path('vet_search/', vet_search, name='vet_search'),
    path('vet_results/', vet_results, name='vet_results'),
    path('app_slots/', app_slots, name='app_slots'),
]
