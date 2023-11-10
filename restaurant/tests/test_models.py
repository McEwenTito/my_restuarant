from django.test import TestCase
from restaurant.models import Restaurant, Ingredient, Dish
from .factories import RestaurantFactory, IngredientFactory, DishFactory

class RestaurantModelTests(TestCase):

    def test_create_restaurant(self):
        """Test that a restaurant can be created."""
        restaurant = RestaurantFactory()
        self.assertEqual(restaurant.name, 'Restaurant 1')  
    # ... Other test methods ...

class IngredientModelTests(TestCase):

    def test_create_ingredient(self):
        """Test that an ingredient can be created."""
        ingredient = IngredientFactory()
        self.assertEqual(ingredient.name, 'Ingredient 0') 

    # ... Other test methods ...

class DishModelTests(TestCase):

    def test_create_dish(self):
        """Test that a dish can be created."""
        dish = DishFactory()
        self.assertEqual(dish.name, 'Dish 0')  

    # ... Other test methods ...
