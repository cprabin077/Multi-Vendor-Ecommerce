from django.shortcuts import render, get_object_or_404

from apps.payments.models import Payment, Status
from apps.orders.models import Order


def callback_view(request):
    data = request.GET

    payment = get_object_or_404(Payment, pidx=data.get("pidx"))

    payment_status = data.get("status")

    if payment_status == "Completed":
        payment.status = Status.COMPLETED
        payment.transaction_id = data.get("tidx")

        # Update order status
        payment.order.status = "processing"
        payment.order.save()

    elif payment_status == "Pending":
        payment.status = Status.PENDING

    else:
        payment.status = Status.USER_CANCELLED

    payment.save()

    return render(request, "payments/callback.html", {"payment": payment})


