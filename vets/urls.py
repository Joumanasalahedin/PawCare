from django.urls import path
from .views import doctor_dashboard, doc_register_login, password_reset

urlpatterns = [
    path('dashboard', doctor_dashboard, name='doctor_dashboard'),
    path('signin-register', doc_register_login, name='doc_register_login'),
    path('password_reset', password_reset, name='password_reset'),
]
