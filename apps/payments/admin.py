from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order",
        "amount",
        "payment_method",
        "status",
        "created_at",
    )

    list_filter = (
        "payment_method",
        "status",
        "created_at",
    )

    search_fields = (
        "transaction_id",
        "pidx",
        "order__id",
    )

    list_editable = ("status",)

    readonly_fields = (
        "status",
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Order Information",
            {
                "fields": (
                    "order",
                    "amount",
                )
            },
        ),
        (
            "Payment Information",
            {
                "fields": (
                    "payment_method",
                    "status",
                    "transaction_id",
                    "pidx",
                )
            },
        ),
        ("Location Details", {"fields": ("location",)}),
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
