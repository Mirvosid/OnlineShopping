from django.urls import path
from .views import (HistoryShopCard, CreatedShopCard, UpdateShopCard, CustomerPurchases, RetrieveShopCard, AllShopCard, DeleteShopCard)



urlpatterns = [
    path('history_shopcard/<uuid:pk>/', HistoryShopCard.as_view()),
    path('created_shopcard/', CreatedShopCard.as_view()),
    path('update_shopcard/<uuid:pk>/', UpdateShopCard.as_view()),
    path('retrieve_shopcard/<uuid:pk>/', RetrieveShopCard.as_view()),
    path('customer_pursache/<uuid:pk>/', CustomerPurchases.as_view()),
    path('delete_shopcard/<uuid:pk>/', DeleteShopCard.as_view()),
    path('all_shopcard/', AllShopCard.as_view()),
]
