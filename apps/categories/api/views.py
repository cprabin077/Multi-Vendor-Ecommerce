from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.categories.api.serializer import CategorySerializer
from apps.categories.models import Category
# from rest_framework.permissions import IsAuthenticated


class CategoryView(GenericAPIView):
    queryset = Category.objects.all() 
    serializer_class = CategorySerializer


    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many = True)
        return Response(serializer.data, 200)
    
    def post(self, request):
        data = request.data
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Category Successfully created"}, 201)
        else:
            return Response(serializer.errors, 422)
        
        
class CategoryUpdateAndDelete(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    def put(self,request,pk):
        trainer = Category.objects.get(id=pk)
        data = request.data
        serializer = CategorySerializer(trainer, data =data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Category successfully updated!!"
            })
        else:
            return Response(serializer.errors,422)
        
    def delete(self, request,pk):
        category = Category.objects.filter(id=pk)
        category.delete()
        return Response({
            "message":"Category successfully deleted!!"
        },200)
        

        