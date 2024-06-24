from django.urls import path
from .views import doctor_dashboard, register_vet, login_vet, password_reset

app_name = 'vets'

urlpatterns = [
    path('dashboard/<int:vet_id>/', doctor_dashboard, name='doctor_dashboard'),
    path('register/', register_vet, name='register'),
    path('login/', login_vet, name='login'),
    path('password_reset', password_reset, name='password_reset'),
]
