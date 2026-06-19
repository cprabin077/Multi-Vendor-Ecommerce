from django.db import models
from django.contrib.auth.models import User


class Vendor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="vendor_profile"
    )

    store_name = models.CharField(max_length=255, unique=True)
    store_description = models.TextField(blank=True)

    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=15)

    store_logo = models.ImageField(upload_to="vendors/logos/", blank=True, null=True)

    address = models.TextField(blank=True)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.store_name
