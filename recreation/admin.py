# recreation/admin.py
from django.contrib import admin
from .models import Recreation


@admin.register(Recreation)
class RecreationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'city', 'phone_number')
    search_fields = ('name', 'category', 'city')
