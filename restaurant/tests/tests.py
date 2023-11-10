from django.test import TestCase
from restaurant.models import Restaurant, Ingredient, Dish

class RestaurantModelTests(TestCase):

    def test_create_restaurant(self):
        """Test that a restaurant can be created."""
        restaurant = Restaurant(name='Pizza Hut', address='123 Main Street', phone_number='123-456-7890')
        restaurant.save()

        self.assertEqual(restaurant.name, 'Pizza Hut')
        self.assertEqual(restaurant.address, '123 Main Street')
        self.assertEqual(restaurant.phone_number, '123-456-7890')

    def test_restaurant_str_method(self):
        """Test the __str__ method of the restaurant model."""
        restaurant = Restaurant(name='Pizza Hut', address='123 Main Street', phone_number='123-456-7890')
        self.assertEqual(str(restaurant), 'Pizza Hut')

class IngredientModelTests(TestCase):

    def test_create_ingredient(self):
        """Test that an ingredient can be created."""
        ingredient = Ingredient(name='Mozzarella')
        ingredient.save()

        self.assertEqual(ingredient.name, 'Mozzarella')

    def test_ingredient_str_method(self):
        """Test the __str__ method of the ingredient model."""
        ingredient = Ingredient(name='Mozzarella')
        self.assertEqual(str(ingredient), 'Mozzarella')

class DishModelTests(TestCase):

    def test_create_dish(self):
        """Test that a dish can be created."""
        restaurant = Restaurant(name='Pizza Hut', address='123 Main Street', phone_number='123-456-7890')
        restaurant.save()

        dish = Dish(name='Pizza', price=10.99, restaurant=restaurant)
        dish.save()

        self.assertEqual(dish.name, 'Pizza')
        self.assertEqual(dish.price, 10.99)
        self.assertEqual(dish.restaurant, restaurant)

    def test_add_ingredient_to_dish(self):
        """Test that an ingredient can be added to a dish."""
        ingredient = Ingredient(name='Mozzarella')
        ingredient.save()

        restaurant = Restaurant(name='Pizza Hut', address='123 Main Street', phone_number='123-456-7890')
        restaurant.save()

        dish = Dish(name='Pizza', price=10.99, restaurant=restaurant)
        dish.save()

        dish.ingredients.add(ingredient)
        dish.save()

        self.assertIn(ingredient, dish.ingredients.all())

    def test_dish_str_method(self):
        """Test the __str__ method of the dish model."""
        restaurant = Restaurant(name='Pizza Hut', address='123 Main Street', phone_number='123-456-7890')
        restaurant.save()

        dish = Dish(name='Pizza', price=10.99, restaurant=restaurant)
        self.assertEqual(str(dish), 'Pizza')
