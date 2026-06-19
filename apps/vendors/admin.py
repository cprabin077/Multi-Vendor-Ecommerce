from django.contrib import admin
from .models import Vendor


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = (
        "store_name",
        "user",
        "email",
        "phone_number",
        "is_verified",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_verified",
        "is_active",
        "created_at",
    )

    search_fields = (
        "store_name",
        "user__username",
        "user__email",
        "email",
        "phone_number",
    )

    list_editable = (
        "is_verified",
        "is_active",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Vendor Information",
            {
                "fields": (
                    "user",
                    "store_name",
                    "store_description",
                    "store_logo",
                )
            },
        ),
        (
            "Contact Information",
            {
                "fields": (
                    "email",
                    "phone_number",
                    "address",
                )
            },
        ),
        (
            "Status",
            {
                "fields": (
                    "is_verified",
                    "is_active",
                )
            },
        ),
        (
            "Timestamps",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )
