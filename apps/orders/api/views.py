from django.db import transaction
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.cart.models import Cart, CartItem
from apps.orders.models import Order, OrderItem
from apps.orders.api.serializer import OrderSerializer, OrderItemSerializer
from apps.payments.models import Payment, PaymentMethods, Status


# Order CRUD
class OrderView(GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request):
        orders = self.get_queryset()

        serializer = self.serializer_class(orders, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "Order created successfully"},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderUpdateDeleteView(GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_object(self, pk):
        return get_object_or_404(Order, id=pk)

    def put(self, request, pk):
        order = self.get_object(pk)

        serializer = self.serializer_class(order, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "Order updated successfully"}, status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order = self.get_object(pk)

        order.delete()

        return Response(
            {"message": "Order deleted successfully"}, status=status.HTTP_200_OK
        )


# OrderItem CRUD
class OrderItemView(GenericAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def get(self, request):
        items = self.get_queryset()

        serializer = self.serializer_class(items, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "Order Item created successfully"},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderItemUpdateDeleteView(GenericAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def get_object(self, pk):
        return get_object_or_404(OrderItem, id=pk)

    def put(self, request, pk):
        item = self.get_object(pk)

        serializer = self.serializer_class(item, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "Order Item updated successfully"},
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = self.get_object(pk)

        item.delete()

        return Response(
            {"message": "Order Item deleted successfully"}, status=status.HTTP_200_OK
        )


# Checkout
class CheckoutView(GenericAPIView):

    @transaction.atomic
    def post(self, request):

        cart = get_object_or_404(Cart, user=request.user)

        cart_items = CartItem.objects.filter(cart=cart)

        if not cart_items.exists():
            return Response(
                {"message": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST
            )

        shipping_address = request.data.get("shipping_address")

        payment_method = request.data.get("payment_method", PaymentMethods.COD)

        order = Order.objects.create(
            user=request.user, shipping_address=shipping_address
        )

        total_amount = 0

        for item in cart_items:

            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,
            )

            total_amount += item.product.price * item.quantity

        order.total_amount = total_amount
        order.save()

        payment = Payment.objects.create(
            order=order,
            amount=total_amount,
            payment_method=payment_method,
            status=Status.PENDING,
        )

        cart_items.delete()

        return Response(
            {
                "message": "Checkout successful",
                "order_id": order.id,
                "payment_id": payment.id,
                "total_amount": total_amount,
                "payment_method": payment.payment_method,
            },
            status=status.HTTP_201_CREATED,
        )
