from django.urls import path
from .views import book_appointment

app_name = 'appointments'

urlpatterns = [
    path('book/', book_appointment, name='book_appointment'),
]
