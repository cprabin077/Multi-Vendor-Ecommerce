from django.db import models

from apps.orders.models import Order


class PaymentMethods(models.TextChoices):
    COD = "COD", "Cash On Delivery"
    KHALTI = "KHALTI", "Khalti"


class Status(models.TextChoices):
    COMPLETED = "COMPLETED", "Completed"
    PENDING = "PENDING", "Pending"
    USER_CANCELLED = "USER_CANCELLED", "User Cancelled"


class Payment(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, related_name="payment"
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    payment_method = models.CharField(max_length=20, choices=PaymentMethods.choices)

    transaction_id = models.CharField(max_length=255, blank=True, null=True)

    pidx = models.CharField(max_length=255, blank=True, null=True)

    status = models.CharField(
        max_length=30, choices=Status.choices, default=Status.PENDING
    )

    location = models.TextField(null=True, blank=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
        return f"Payment #{self.id}"

    class Meta:
        db_table = "payment"
