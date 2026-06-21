import requests
from django.conf import settings


def khalti_payment(user, payment):

    url = "https://dev.khalti.com/api/v2/epayment/initiate/"

    payload = {
        "return_url": "http://127.0.0.1:8000/payments/callback/",
        "website_url": "http://127.0.0.1:8000/",
        "amount": int(payment.amount * 100),  # paisa
        "purchase_order_id": str(payment.order.id),
        "purchase_order_name": f"Order-{payment.order.id}",
        "customer_info": {
            "name": f"{user.first_name} {user.last_name}",
            "email": user.email,
        },
    }

    headers = {
        "Authorization": f"Key {settings.KHALTI_SECRET_KEY}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)

        # If API fails (404/500/etc)
        if response.status_code != 200:
            return {
                "error": "Khalti API failed",
                "status_code": response.status_code,
                "response": response.text,
            }

        return response.json()

    except requests.exceptions.RequestException as e:
        return {
            "error": "Network error while connecting to Khalti",
            "detail": str(e)
        }
