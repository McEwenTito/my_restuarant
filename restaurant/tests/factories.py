import factory
from faker import Faker
from restaurant.models import Restaurant, Ingredient, Dish

fake = Faker()

class RestaurantFactory(factory.Factory):
    class Meta:
        model = Restaurant

    name = factory.Sequence(lambda n: f'Restaurant {n}')
    address = fake.address()
    phone_number = fake.phone_number()

class IngredientFactory(factory.Factory):
    class Meta:
        model = Ingredient

    name = factory.Sequence(lambda n: f'Ingredient {n}')

class DishFactory(factory.Factory):
    class Meta:
        model = Dish

    name = factory.Sequence(lambda n: f'Dish {n}')
    price = fake.random_number(2)
    restaurant = factory.SubFactory(RestaurantFactory)
