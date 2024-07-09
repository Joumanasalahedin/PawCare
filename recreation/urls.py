from django.urls import path
from .views import rec_search

app_name = 'recreation'

urlpatterns = [
    path('rec_search/', rec_search, name='rec_search')
]
