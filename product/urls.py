from django.urls import path
from .views import CreatedProducts,  CalculateTotalPrice, UpdateProducts, AllProducts, RetrieveProducts, DeleteProducts, ExpiredProducts



urlpatterns = [
    path('expired_products/', ExpiredProducts.as_view()),
    path('created_products/', CreatedProducts.as_view()),
    path('update_products/<uuid:id>/', UpdateProducts.as_view()),
    path('retrieve_products/<uuid:pk>/', RetrieveProducts.as_view()),
    path('all_products/', AllProducts.as_view()),
    path('delete_products/<uuid:pk>/', DeleteProducts.as_view()),
    path('total_price/', CalculateTotalPrice.as_view()),
]

