from django.shortcuts import render
from .models import Category
from .serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework import views, status
from product.models import Product
from django.db.models import Count
from drf_yasg.utils import swagger_auto_schema


class CreatedCategory(views.APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    @swagger_auto_schema(
        request_body=CategorySerializer,  
        operation_description="In this page category is created!",
        responses={201: "CREATED!"},
    )
    def post(self, request):
        data = request.data
        serializer = CategorySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    


class DeletedCategory(views.APIView):
    @swagger_auto_schema(
        operation_description="In this page you can delete categroy!",
        operation_summary=""
    )
    def delete(self, request, pk):
        try:
            instance = Category.objects.get(id=pk)
            instance.delete()
            return Response({200: "DELETED!"}, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({404: "OBJECT DOES NOT FOUND!"}, status=status.HTTP_404_NOT_FOUND)



class AllCategory(views.APIView):
    @swagger_auto_schema(
        operation_description="In this page you can see all of the categories!",
        operation_summary=""
    )
    def get(self, request):
        categorys = Category.objects.all()
        serializer = CategorySerializer(categorys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

        


class RetrieveCategory(views.APIView):
    @swagger_auto_schema(
        operation_description="In this page you can retrieve category! ",
        operation_summary=""
    )
    def get(self, request, pk):
        try:
            instance = Category.objects.get(id=pk)
            serializer = CategorySerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({404: "OBJECT DOES NOT FOUND!"}, status=status.HTTP_404_NOT_FOUND)



class MostSoldProducts(views.APIView):
    @swagger_auto_schema(
        operation_description="In this page you can find a list of the best selling products!",
        operation_summary=""
    )
    def get(self, request):
        categories = Category.objects.all()
        result = []

        for category in categories:
            most_sold_product = Product.objects.filter(category=categories).annotate(sold_count=Count('items')).order_by('-sold_count').first()

            if most_sold_product and most_sold_product.sold_count > 0:
                result.append({'category': category.name, 'product': most_sold_product.name, 'sold_count': most_sold_product.sold_count})

        return Response(result)

class UpdateCategory(views.APIView):
    @swagger_auto_schema(
        operation_description=" In this page you can update category!",
        operation_summary="",
        request_body=CategorySerializer
    )
    def put(self, request, pk):
        try:
            data = request.data
            instance = Category.objects.get(id=pk)
            serializer = CategorySerializer(data=data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({404: "OBJECT DOES NOT FOUND!"}, status=status.HTTP_404_NOT_FOUND)

