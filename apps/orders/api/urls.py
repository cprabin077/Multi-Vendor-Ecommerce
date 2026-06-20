from django.urls import path

from .views import (
    OrderView,
    OrderUpdateDeleteView,
    OrderItemView,
    OrderItemUpdateDeleteView,
)

urlpatterns = [
    # Orders
    path("", OrderView.as_view(), name="order-list-create"),
    path("<int:pk>/", OrderUpdateDeleteView.as_view(), name="order-update-delete"),

    
    # Order Items
    path("items/", OrderItemView.as_view(), name="orderitem-list-create"),
    path("items/<int:pk>/", OrderItemUpdateDeleteView.as_view(), name="orderitem-update-delete"),
]
