from django.shortcuts import render
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework import status, views
from drf_yasg.utils import swagger_auto_schema


class CreatedCustomer(views.APIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    @swagger_auto_schema(
        request_body=CustomerSerializer,
        operation_description="In this page customer is created!",  
        responses={201: "CREATED!"},
    )
    def post(self, request):
        data = request.data
        serializer = CustomerSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        


        
class DeleteCustomer(views.APIView):
    @swagger_auto_schema(
        operation_description="In this page you can delete customer's details!",
        operation_summary=""
    )
    def delete(self, request, pk):
        try:
            instance = Customer.objects.get(id=pk)
            instance.delete()
            return Response({200: "DELETED !"}, status=status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return Response({404: "OBJECT DOES NOT FOUND!"}, status=status.HTTP_404_NOT_FOUND)



class AllCustomer(views.APIView):
    @swagger_auto_schema(
        operation_description=" In this page you can see all of the customers!",
        operation_summary=""
    )
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


    
class RetrieveCustomer(views.APIView):
    @swagger_auto_schema(
        operation_description="In this page you can retrieve customer's details!",
        operation_summary=""
    )
    def get(self, request, pk):
        try:
            instance = Customer.objects.get(id=pk) 
            serializer = CustomerSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return Response({404: "OBJECT DOES NOT FOUND!"}, status=status.HTTP_404_NOT_FOUND)


class UpdateCustomer(views.APIView):
    @swagger_auto_schema(
        operation_description="In this page you can update cutomer's details!",
        operation_summary="",
        request_body=CustomerSerializer
    )
    def put(self, request, pk):
        try:
            data = request.data
            instance = Customer.objects.get(id=pk)
            serializer = CustomerSerializer(data=data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return Response({404: "OBJECT DOES NOT FOUND!"}, status=status.HTTP_404_NOT_FOUND)
    