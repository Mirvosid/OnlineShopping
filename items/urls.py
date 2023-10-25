from django.urls import path
from .views import CreatedItems, DeleteItems, AllItems, RetrieveItems, UpdateItems


urlpatterns = [
    path('created_items/', CreatedItems.as_view()),
    path('update_items/<uuid:pk>/', UpdateItems.as_view()),
    path('retrieve_items/<uuid:pk>/', RetrieveItems.as_view()),
    path('delete_items/<uuid:pk>/', DeleteItems.as_view()),
    path('all_items/', AllItems.as_view()),
]