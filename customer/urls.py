from django.urls import path
from .views import CreatedCustomer, DeleteCustomer, RetrieveCustomer, AllCustomer, UpdateCustomer

urlpatterns = [
    path('created_customer/', CreatedCustomer.as_view()),
    path('update_customer/<uuid:pk>/', UpdateCustomer.as_view()),
    path('all_customer/', AllCustomer.as_view()),
    path('delete_customer/<uuid:pk>/', DeleteCustomer.as_view()),
    path('retrieve_customer/<uuid:pk>/', RetrieveCustomer.as_view()),
]
