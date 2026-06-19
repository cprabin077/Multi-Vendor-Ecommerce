from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.products.models import Product
from apps.products.api.serializer import ProductSerializer


class ProductView(GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        products = self.get_queryset()
        serializer = self.serializer_class(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "Product created successfully"},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductUpdateDeleteView(GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_object(self, pk):
        return Product.objects.get(id=pk)

    def put(self, request, pk):
        product = self.get_object(pk)

        serializer = self.serializer_class(product, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "Product updated successfully"}, status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()

        return Response(
            {"message": "Product deleted successfully"}, status=status.HTTP_200_OK
        )
