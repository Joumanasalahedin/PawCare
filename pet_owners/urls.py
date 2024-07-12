from django.urls import path
from .views import register_owner, login_owner, user_dashboard

app_name = 'pet_owners'

urlpatterns = [
    path('login/', login_owner, name='login'),
    path('register/', register_owner, name='register'),
    path('dashboard/<int:owner_id>/', user_dashboard, name='user_dashboard'),
]
