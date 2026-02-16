from django.urls import path
from .views import AddRestaurantAPIView, AddCategoryAPIView

urlpatterns = [
    path('restaurants/', AddRestaurantAPIView.as_view(), name='add-restaurant'),
    path('restaurants/<int:restaurant_id>/categories/', AddCategoryAPIView.as_view(), name='add-category'),
]