from django.contrib import admin
from .models import PetOwner, Pet


@admin.register(PetOwner)
class PetOwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'name', 'email',
                    'created_at', 'is_active', 'is_staff')
    search_fields = ('username', 'name', 'email')


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('owner_id', 'name', 'breed')
    search_fields = ('owner', 'name', 'breed')
