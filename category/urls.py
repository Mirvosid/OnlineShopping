from django.urls import path
from .views import CreatedCategory, DeletedCategory, RetrieveCategory, UpdateCategory, AllCategory, MostSoldProducts


urlpatterns = [
    path('update_category/<uuid:pk>/', UpdateCategory.as_view()),
    path('created_category/', CreatedCategory.as_view()),
    path('most_sold_products/', MostSoldProducts.as_view()),
    path('retrieve_category/<uuid:pk>/', RetrieveCategory.as_view()),   
    path('delete_category/<uuid:pk>/', DeletedCategory.as_view()),
    path('all_category/', AllCategory.as_view()),
]