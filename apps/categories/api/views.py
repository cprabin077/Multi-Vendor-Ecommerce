from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.categories.api.serializer import CategorySerializer
from apps.categories.models import Category


# LIST + CREATE
class CategoryView(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request):
        categories = self.get_queryset()
        serializer = self.serializer_class(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Category successfully created"},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryUpdateAndDelete(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_object(self, pk):
        return Category.objects.get(id=pk)

    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = self.serializer_class(category, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Category successfully updated"}, status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()

        return Response(
            {"message": "Category successfully deleted"}, status=status.HTTP_200_OK
        )
