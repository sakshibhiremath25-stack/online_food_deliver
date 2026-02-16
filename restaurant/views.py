from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Restaurant
from .serializers import RestaurantSerializer, CategorySerializer


# --- Add Restaurant ---
class AddRestaurantAPIView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


# --- Add Category ---
class AddCategoryAPIView(generics.CreateAPIView):
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        restaurant = get_object_or_404(
            Restaurant,
            id=self.kwargs['restaurant_id']
        )
        serializer.save(restaurant=restaurant)