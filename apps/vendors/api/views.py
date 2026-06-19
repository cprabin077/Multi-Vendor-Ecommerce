from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.vendors.models import Vendor
from apps.vendors.api.serializer import VendorSerializer


class VendorView(GenericAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def get(self, request):
        vendors = self.get_queryset()
        serializer = self.serializer_class(vendors, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "Vendor created successfully"},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorUpdateDeleteView(GenericAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def get_object(self, pk):
        return Vendor.objects.get(id=pk)

    def put(self, request, pk):
        vendor = self.get_object(pk)

        serializer = self.serializer_class(vendor, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "Vendor updated successfully"}, status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        vendor = self.get_object(pk)
        vendor.delete()

        return Response(
            {"message": "Vendor deleted successfully"}, status=status.HTTP_200_OK
        )
