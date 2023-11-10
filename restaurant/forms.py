# your_app_name/forms.py
from django import forms
from .models import Restaurant, Ingredient, Dish

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'phone_number']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'price', 'ingredients', 'restaurant']
