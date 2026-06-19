from django.urls import path

from .views import VendorView, VendorUpdateDeleteView

urlpatterns = [
    path("", VendorView.as_view(), name="vendor-list-create"),
    path("<int:pk>/", VendorUpdateDeleteView.as_view(), name="vendor-update-delete"),
]
