from django.urls import path

from apps.payments.views import callback_view

urlpatterns = [
    path("callback/", callback_view, name="payment-callback"),
   
]
