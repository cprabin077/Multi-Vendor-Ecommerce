from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.orders.models import Order, OrderItem
from apps.orders.api.serializer import OrderSerializer, OrderItemSerializer


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


# Order Item CRUD
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
                {"message": "Order item created successfully"},
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
                {"message": "Order item updated successfully"},
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = self.get_object(pk)
        item.delete()

        return Response(
            {"message": "Order item deleted successfully"}, status=status.HTTP_200_OK
        )
