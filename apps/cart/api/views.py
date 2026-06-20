from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.cart.models import Cart, CartItem
from apps.cart.api.serializer import CartSerializer, CartItemSerializer


# Cart CRUD
class CartView(GenericAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get(self, request):
        carts = self.get_queryset()
        serializer = self.serializer_class(carts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "Cart created successfully"}, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartUpdateDeleteView(GenericAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_object(self, pk):
        return get_object_or_404(Cart, id=pk)

    def put(self, request, pk):
        cart = self.get_object(pk)

        serializer = self.serializer_class(cart, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "Cart updated successfully"}, status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cart = self.get_object(pk)
        cart.delete()

        return Response(
            {"message": "Cart deleted successfully"}, status=status.HTTP_200_OK
        )


# CartItem CRUD
class CartItemView(GenericAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get(self, request):
        items = self.get_queryset()
        serializer = self.serializer_class(items, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "Cart item added successfully"},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartItemUpdateDeleteView(GenericAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_object(self, pk):
        return get_object_or_404(CartItem, id=pk)

    def put(self, request, pk):
        item = self.get_object(pk)

        serializer = self.serializer_class(item, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "Cart item updated successfully"}, status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = self.get_object(pk)
        item.delete()

        return Response(
            {"message": "Cart item deleted successfully"}, status=status.HTTP_200_OK
        )
