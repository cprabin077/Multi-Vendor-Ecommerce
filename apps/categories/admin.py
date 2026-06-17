from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "created_at", "updated_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("name", "description")
    ordering = ("name",)

    prepopulated_fields = {"slug": ("name",)}

    list_editable = ("is_active",)

    readonly_fields = ("created_at", "updated_at")
