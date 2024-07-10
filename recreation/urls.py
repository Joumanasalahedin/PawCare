from django.urls import path
from .views import rec_search, rec_results

app_name = 'recreation'

urlpatterns = [
    path('rec_search/', rec_search, name='rec_search'),
    path('rec_results/', rec_results, name='rec_results')
]
