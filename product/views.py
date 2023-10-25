from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status, views
from datetime import datetime
from drf_yasg.utils import swagger_auto_schema


class CreatedProducts(views.APIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    @swagger_auto_schema(
        request_body=ProductSerializer,  
        responses={201: "CREATED!"},
    )
    def post(self, request):
        data = request.data
        serializer = ProductSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class DeleteProducts(views.APIView):
    @swagger_auto_schema(
        operation_description="In this page you can delete product",
        operation_summary=""
    )
    def delete(self, request, pk):
        try:
            instance = Product.objects.get(id=pk)
            instance.delete()
            return Response({200: "DELETED!"}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({404: "OBJECT DOES NOT FOUND!"}, status=status.HTTP_404_NOT_FOUND)


class AllProducts(views.APIView):
    @swagger_auto_schema(
        operation_description="In this page you can see all of the products!",
        operation_summary=""
    )
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class RetrieveProducts(views.APIView):
    @swagger_auto_schema(
        operation_description="In this page you can retrieve product!",
        operation_summary=""
    )
    def get(self, request, pk):
        try:
            instance = Product.objects.get(id=pk)
            serializer = ProductSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({404: "OBJECT DOES NOT FOUND!"}, status=status.HTTP_404_NOT_FOUND)
        


class ExpiredProducts(views.APIView):
    @swagger_auto_schema(
        operation_description="This is expired products!",
        operation_summary=""
    )
    def get(self, request):
        current_time = datetime.now()
        expired_products = Product.objects.filter(end_date__lt=current_time)
        data = [
            {
                'name': product.name,
                'end_date': product.end_date,
            }
            for product in expired_products
        ]
        return Response(data)

class UpdateProducts(views.APIView):
    @swagger_auto_schema(
        operation_description="In this page you can update products!",
        operation_summary="",
        request_body=ProductSerializer
    )
    def put(self, request, pk):
        try:
            data = request.data
            instance = Product.objects.get(id=pk)
            serializer = ProductSerializer(data=data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({404: "OBJECT DOES NOT FOUND!"}, status=status.HTTP_404_NOT_FOUND)


class CalculateTotalPrice(views.APIView):
    @swagger_auto_schema(
        operation_description="In this page you can get total price of product!",
        operation_summary=""
    )
    def get(self, request):
        products = Product.objects.all()
        if not products:
            return Response({404: "OBJECT DOEST NOT EXIST"}, status=status.HTTP_404_NOT_FOUND)
        total_price = sum(product.price for product in products)
        
        return Response({'total_price': total_price}, status=status.HTTP_200_OK)
    