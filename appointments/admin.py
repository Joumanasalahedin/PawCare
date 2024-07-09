from django.contrib import admin
from .models import Appointments


@admin.register(Appointments)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('owner_id', 'vet_id', 'date', 'time')
    search_fields = ('owner_id', 'vet_id')
