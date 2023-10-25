from django.shortcuts import render
from .models import ShopCard
from .serializers import ShopCardSerializer
from rest_framework.response import Response
from rest_framework import status, views
from django.http import JsonResponse, HttpResponse
from django.db import models
# import pandas as pd
from drf_yasg.utils import swagger_auto_schema


class CreatedShopCard(views.APIView):
    queryset = ShopCard.objects.all()
    serializer_class = ShopCardSerializer
    @swagger_auto_schema(
        request_body=ShopCardSerializer,  
        responses={201: "CREATED"},
    )
    def post(self, request):
        data = request.data
        serializer = ShopCardSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class DeleteShopCard(views.APIView):
    @swagger_auto_schema(
        operation_description="In this page you can delete history of purchasing",
        operation_summary=""
    )
    def delete(self, request, pk):
        try:
            instance = ShopCard.objects.get(id=pk)
            instance.delete()
            return Response({200: "DELETED!"}, status=status.HTTP_200_OK)
        except ShopCard.DoesNotExist:
            return Response({404: "OBJECT DOES NOT FOUND!"}, status=status.HTTP_404_NOT_FOUND)

        
class AllShopCard(views.APIView):
    @swagger_auto_schema(
        operation_description="In this page you can see all of the purchasing",
        operation_summary=""
    )
    def get(self, request):
        shopcards = ShopCard.objects.all()
        serializer = ShopCardSerializer(shopcards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

        

class HistoryShopCard(views.APIView):
    @swagger_auto_schema(
        operation_description="In this page you can get history of purchasing",
        operation_summary=""
    )
    def get(self, request, pk):
        try:
            shopcards = ShopCard.objects.filter(owner__id=pk)
            serializer = ShopCardSerializer(shopcards, many=True)
            return JsonResponse(serializer.data, safe=False)
        except ShopCard.DoesNotExist:
            return JsonResponse({404: 'OBJECT DOES NOT FOUND!'}, status=status.HTTP_404_NOT_FOUND)
        

        
class RetrieveShopCard(views.APIView):
    @swagger_auto_schema(
        operation_description="In this page you can retrieve purchasing of shopcard!",
        operation_summary=""
    )
    def get(self, request, pk):
        try:
            instance = ShopCard.objects.get(id=pk)
            serializer = ShopCardSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ShopCard.DoesNotExist:
            return Response({404: "OBJECT DOES NOT FOUND!"}, status=status.HTTP_404_NOT_FOUND)


class CustomerPurchases(views.APIView):
    @swagger_auto_schema(
        operation_description="In thing page you can check purchasing sum!",
        operation_summary=""
    )
    def get(self, request, pk):
        try:
            total_purchase = ShopCard.objects.filter(owner__id=pk).aggregate(total=models.Sum('total_price'))['total']
            if total_purchase and total_purchase > 1000000:
                return JsonResponse({200: "Total sum is more than 1000000"}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({200: "Total sum is less than 1000000"}, status=status.HTTP_200_OK)
        except ShopCard.DoesNotExist:
            return JsonResponse({404: "OBJECT DOES NOT FOUND!"}, status=status.HTTP_404_NOT_FOUND)


class UpdateShopCard(views.APIView):
    @swagger_auto_schema(
        operation_description="In this page you can update purchasing ",
        operation_summary="",
        request_body=ShopCardSerializer
    )
    def put(self, request, pk):
        try:
            data = request.data
            instance = ShopCard.objects.get(id=pk)
            serializer = ShopCardSerializer(data=data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ShopCard.DoesNotExist:
            return Response({404: "OBJECT DOES NOT FOUND!"}, status=status.HTTP_404_NOT_FOUND)
        
