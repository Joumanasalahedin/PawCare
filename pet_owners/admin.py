from django.contrib import admin
from .models import PetOwner


@admin.register(PetOwner)
class PetOwnerAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'email',
                    'created_at', 'is_active', 'is_staff')
    search_fields = ('username', 'name', 'email')
