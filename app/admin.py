from django.contrib import admin
from django.views.generic import edit
from app.models import *

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ["name"]

    list_per_page = 15


@admin.register(Provider)
class UnitAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active"]
    list_per_page = 15


@admin.register(Products)
class UnitAdmin(admin.ModelAdmin):
    list_editable = [
        "is_active"
    ]
    
    list_display = [
        "name",
        "key",
        "provider",
        "price",
        "unit",
        "is_active"
    ]

    list_per_page = 45