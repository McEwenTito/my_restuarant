from django.test import TestCase
from django.urls import reverse
from .factories import RestaurantFactory, IngredientFactory, DishFactory
from restaurant.models import Restaurant



class RestaurantViewsTest(TestCase):

    def test_restaurant_list_view(self):
        response = self.client.get(reverse('restaurant:restaurant_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant_list.html')

    def test_restaurant_create_view(self):
        response = self.client.get(reverse('restaurant:restaurant_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant_form.html')

        data = {'name': 'New restaurant', 'address': '123 New Street', 'phone_number': '987-654-3210'}
        response = self.client.post(reverse('restaurant:restaurant_create'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission
        self.assertTrue(Restaurant.objects.filter(name='New Restaurant').exists())


class RestaurantViewsTests(TestCase):

    def setUp(self):
        # Create a Restaurant instance for testing
        self.restaurant = Restaurant.objects.create(name='Example Restaurant', address='123 Main Street', phone_number='555-1234')

    def test_edit_view(self):
        # Generate the edit URL using reverse
        edit_url = reverse('restaurant:restaurant_edit', kwargs={'pk': self.restaurant.pk})

        # Ensure the generated URL is correct
        self.assertEqual(edit_url, f'/restaurant/restaurants/{self.restaurant.pk}/edit/')

        # Example test client usage
        response = self.client.get(edit_url)
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on your views and template logic

    def test_delete_view(self):
        # Generate the delete URL using reverse
        delete_url = reverse('restaurant:restaurant_delete', kwargs={'pk': self.restaurant.pk})

        # Ensure the generated URL is correct
        self.assertEqual(delete_url, f'/restaurant/restaurants/{self.restaurant.pk}/delete/')

        # Example test client usage
        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on your views and template logic for the delete view