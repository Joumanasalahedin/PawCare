from django.contrib import admin
from .models import Vet, Appointments


@admin.register(Vet)
class VetAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'name',
                    'created_at', 'is_active', 'is_staff')
    search_fields = ('username', 'name', 'email')


@admin.register(Appointments)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('pet_id', 'vet_id', 'date', 'time')
