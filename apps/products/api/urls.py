from django.urls import path
from .views import ProductView, ProductUpdateDeleteView

urlpatterns = [
    path("", ProductView.as_view(), name="product-list-create"),
    path("<int:pk>/", ProductUpdateDeleteView.as_view(), name="product-update-delete"),
]
