from django.contrib import admin
from .models import Vet


@admin.register(Vet)
class VetAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'name',
                    'created_at', 'is_active', 'is_staff')
    search_fields = ('username', 'name', 'email')
