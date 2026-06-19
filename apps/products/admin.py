from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "vendor",
        "category",
        "price",
        "stock",
        "status",
    )

    list_filter = (
        "category",
        "vendor",
        "status",
    )

    search_fields = (
        "name",
        "description",
    )

    prepopulated_fields = {"slug": ("name",)}
