# your_app_name/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Restaurant, Ingredient, Dish
from .forms import RestaurantForm, IngredientForm, DishForm

class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurant_list.html'
    context_object_name = 'restaurants'

class RestaurantCreateView(CreateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'restaurant_form.html'
    success_url = reverse_lazy('restaurant:restaurant_list')

class RestaurantUpdateView(UpdateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'restaurant_form_partial.html'
    context_object_name = 'restaurant'
    success_url = reverse_lazy('restaurant:restaurant_list')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Restaurant, pk=pk)

class RestaurantDeleteView(DeleteView):
    model = Restaurant
    template_name = 'restaurant_confirm_delete.html'
    success_url = reverse_lazy('restaurant:restaurant_list')
