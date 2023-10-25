from django.shortcuts import render
from .models import Items
from .serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework import status, views
from drf_yasg.utils import swagger_auto_schema


class CreatedItems(views.APIView):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer
    @swagger_auto_schema(
        request_body=ItemSerializer,  
        operation_description="In this page items is created!", 
        responses={201: "CREATED!"},
    )
    def post(self, request):
        data = request.data
        serializer = ItemSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)




class DeleteItems(views.APIView):
    @swagger_auto_schema(
        operation_description="In this page you can delete items!",
        operation_summary=""
    )
    def delete(self, request, pk):
        try:
            instance = Items.objects.get(id=pk)
            instance.delete()
            return Response({200: "DELETED!"}, status=status.HTTP_200_OK)
        except Items.DoesNotExist:
            return Response({404: "OBJECT DOES NOT FOUND!"}, status=status.HTTP_404_NOT_FOUND)


class AllItems(views.APIView):
    @swagger_auto_schema(
        operation_description="In this page you can see all of the items!",
        operation_summary=""
    )
    def get(self, request):
        items = Items.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




class RetrieveItems(views.APIView):
    @swagger_auto_schema(
        operation_description="In this page you can retrieve items!",
        operation_summary=""
    )
    def get(self, request, pk):
        try:
            instance = Items.objects.get(id=pk)
            serializer = ItemSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Items.DoesNotExist:
            return Response({404: "OBJECT DOES NOT FOUND"}, status=status.HTTP_404_NOT_FOUND)


class UpdateItems(views.APIView):
    @swagger_auto_schema(
        operation_description="In this page you can update items!",
        operation_summary="",
        request_body=ItemSerializer
    )
    def put(self, request, pk):
        try:
            data = request.data
            instance = Items.objects.get(id=pk)
            serializer = ItemSerializer(data=data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Items.DoesNotExist:
            return Response({404: "OBJECT DOES NOT FOUND!"}, status=status.HTTP_404_NOT_FOUND)
