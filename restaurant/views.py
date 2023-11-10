# your_app_name/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Restaurant, Ingredient, Dish
from .forms import RestaurantForm, IngredientForm, DishForm

class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurant_list.html'
    context_object_name = 'restaurants'

class RestaurantCreateView(CreateView):
    model = Restaurant
    template_name = 'restaurant_form.html'
    form_class = RestaurantForm
    success_url = reverse_lazy('restaurant:restaurant_list')

class RestaurantUpdateView(UpdateView):
    model = Restaurant
    template_name = 'restaurant_form.html'
    form_class = RestaurantForm
    success_url = reverse_lazy('restaurant:restaurant_list')

class RestaurantDeleteView(DeleteView):
    model = Restaurant
    template_name = 'restaurant_confirm_delete.html'
    success_url = reverse_lazy('restaurant:restaurant_list')
