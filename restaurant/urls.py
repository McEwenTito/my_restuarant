from django.urls import path
from .views import RestaurantListView, RestaurantCreateView, RestaurantUpdateView, RestaurantDeleteView

app_name = 'restaurant'

urlpatterns = [
    path('restaurants/', RestaurantListView.as_view(), name='restaurant_list'),
    path('restaurants/new/', RestaurantCreateView.as_view(), name='restaurant_create'),
    path('restaurants/<int:pk>/edit/', RestaurantUpdateView.as_view(), name='restaurant_edit'),
    path('restaurants/<int:pk>/delete/', RestaurantDeleteView.as_view(), name='restaurant_delete'),
]

