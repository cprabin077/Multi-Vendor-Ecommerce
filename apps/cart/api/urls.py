from django.urls import path

from .views import (
    CartView,
    CartUpdateDeleteView,
    CartItemView,
    CartItemUpdateDeleteView,
)

urlpatterns = [
   
   
    # Cart
    path("", CartView.as_view(), name="cart-list-create"),
    path("<int:pk>/", CartUpdateDeleteView.as_view(), name="cart-update-delete"),
   
   
    # Cart Item
    path("items/", CartItemView.as_view(), name="cartitem-list-create"),
    path("items/<int:pk>/", CartItemUpdateDeleteView.as_view(), name="cartitem-update-delete"),
]
