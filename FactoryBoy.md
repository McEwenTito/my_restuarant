# Start Writing Django Tests in 4 Minutes using FactoryBoy (and Faker)

Testing is a crucial part of Django development. It helps to make sure that your code works as expected. 

Testing is an important step in every development process for the following reasons:

- **It helps prevent bugs**. Testing helps you find and fix bugs before they cause problems for your users 
- **It improves the quality of your code**. Well-tested code is reliable, efficient, and maintainable.
- **It gives you confidence in your code**. When you write tests for your code, you can make changes to your code without breaking the entire application.


There are two main types of testing: **Integration testing** and **Unit testing.**


This guide will show you how to write unit tests in Django using **FactoryBoy** and **Faker**. FactoryBoy and Faker are awesome Python libraries for testing. Using them will help you create comprehensive, realistic, and reusable tests.

I will make this guide short and to the point. You should be able to finish it before your coffee runs cold.

## 1.0 Setting Up Your Django Project

Let's quickly set up our Django project. We will create a simple restaurant app. 



### 1.1 Install Python

Django requires Python 3.6 or higher. To install Python, you can use the following command:

```
sudo apt install python3
```
### 1.2 Create a virtual environment

A virtual environment is a sandboxed Python environment that allows you to install packages without affecting your system-wide Python installation. To create a virtual environment, run the following command:

```
python3 -m venv myvenv
```

### 1.3 Activate the virtual environment

To activate the virtual environment, run the following command:
```
source myvenv/bin/activate
```

### 1.4 Install Django

Once you have Python installed, you can install Django using pip:

```
pip install django
```

### 1.5 Create a new Django project

To create a new Django project, run the following command:

```
django-admin startproject my_restaurant
```

This will create a new directory called my_restuarant containing your Django project files.

### 1.6 Create a new Django app

To create a new Django app, run the following command:
```
django-admin startapp restaurant
```
This will create a new directory called restaurant containing your Django app files.

### 1.7 Add your app to your project's settings

To add your app to your project's settings, open the settings.py file in your project directory and add your app to the INSTALLED_APPS list.

### 1.8 Start the development server

To start the development server, run the following command:

```
python manage.py runserver
```
This will start the development server at http://localhost:8000/. You can now access your Django project in your web browser.

### 1.9 Create a superuser

To create a superuser, run the following command:
```
python manage.py createsuperuser
```

This will prompt you to enter your superuser account's username, email address, and password.

And we are done setting up Django for our app. Next, we will create models. 


## 2. Creating our app Models

Our restaurant app will have 3 models: Dish, Ingredient, and Restaurant. Let's go ahead and edit our restaurant/models.py file as follows:

**restaurant/models.py**

```python
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        
        
class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredient)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
        
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        
```

Awesome, now lets create and run migrations for our models:
```
python manage.py makemigrations
python manage.py migrate
```

## 3. Writing the First Test

Create a directory called tests. cd into that directory and an empty **\__init__.py** file and a tests.py file.

**restaurant/tests/tests.py**
```python
from django.test import TestCase
from .models import Restaurant, Ingredient, Dish

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


```

We can now run our first test scenarios for our new models with the command:

```
python manage.py test restaurant.tests
```

Congratulations! You have passed your first tests.

## 4. Using FactoryBoy and Faker

Let's face it, writing test scenarios is boring, even borderline unproductive. 

FactoryBoy and Faker are powerful libraries that remove repetitiveness from tests and improve efficiency. FactoryBoy allows you to define factories for your models, and Faker helps generate realistic-looking fake data.


### 4.1 Install the packages:
First, you need to install the factory_boy and faker packages. You can install them using pip:
```
pip install factory-boy faker
```

### 4.2 Create Factories:
Create factories for your models using Factory Boy. In your Django app directory, create a tests directory if you don't have one, and within that directory, create a file named factories.py. Define factories for your models in this file.

**restaurant/tests/factories.py**
```python
import factory
from faker import Faker
from .models import Restaurant, Ingredient, Dish

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
```
### 4.3 Use Factories in Tests:
Now, we can use these factories in our test cases to create instances of our models with fake data.

**restaurant/tests/test_models.py**
```python
from django.test import TestCase
from .models import Restaurant, Ingredient, Dish
from .factories import RestaurantFactory, IngredientFactory, DishFactory

class RestaurantModelTests(TestCase):

    def test_create_restaurant(self):
        """Test that a restaurant can be created."""
        restaurant = RestaurantFactory()
        self.assertEqual(restaurant.name, 'Restaurant 0')  


class IngredientModelTests(TestCase):

    def test_create_ingredient(self):
        """Test that an ingredient can be created."""
        ingredient = IngredientFactory()
        self.assertEqual(ingredient.name, 'Ingredient 0')  


class DishModelTests(TestCase):

    def test_create_dish(self):
        """Test that a dish can be created."""
        dish = DishFactory()
        self.assertEqual(dish.name, 'Dish 0')  



```
Go ahead and run the tests again.

## 5. Testing Views
Let's move on to views. We'll create basic views for listing, creating, updating, and deleting instances of the Restaurant, Ingredient, and Dish.

### 5.1 Create Views file
**restaurant/test_views.py**
```python
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Restaurant, Ingredient, Dish

class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurant_list.html'
    context_object_name = 'restaurants'

class RestaurantCreateView(CreateView):
    model = Restaurant
    template_name = 'restaurant_form.html'
    fields = ['name', 'address', 'phone_number']
    success_url = reverse_lazy('restaurant_list')

class RestaurantUpdateView(UpdateView):
    model = Restaurant
    template_name = 'restaurant_form.html'
    fields = ['name', 'address', 'phone_number']
    success_url = reverse_lazy('restaurant_list')

class RestaurantDeleteView(DeleteView):
    model = Restaurant
    template_name = 'restaurant_confirm_delete.html'
    success_url = reverse_lazy('restaurant_list')
```
Similar views can be created for Ingredient and Dish.

### 5.2 Create our urls

**restaurant/urls.py**
```python
from django.urls import path
from .views import RestaurantListView, RestaurantCreateView, RestaurantUpdateView, RestaurantDeleteView

urlpatterns = [
    path('restaurants/', RestaurantListView.as_view(), name='restaurant_list'),
    path('restaurants/new/', RestaurantCreateView.as_view(), name='restaurant_create'),
    path('restaurants/<int:pk>/edit/', RestaurantUpdateView.as_view(), name='restaurant_edit'),
    path('restaurants/<int:pk>/delete/', RestaurantDeleteView.as_view(), name='restaurant_delete'),
]
```

### 5.3 Create our html files

**restaurant/templates/restaurant_list.html:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Restaurant List</title>
</head>
<body>
    <h1>Restaurant List</h1>
    <ul>
        {% for restaurant in restaurants %}
            <li>{{ restaurant.name }} - {{ restaurant.address }} - {{ restaurant.phone_number }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```
**restaurant/templates/restaurant_form.html** 
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% if form.instance.pk %}Edit{% else %}Create{% endif %} Restaurant</title>
</head>
<body>
    <h1>{% if form.instance.pk %}Edit{% else %}Create{% endif %} Restaurant</h1>
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Save</button>
    </form>
</body>
</html>
```
**restaurant/templates/restaurant_confirm_delete.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Delete Restaurant</title>
</head>
<body>
    <h1>Delete Restaurant</h1>
    <p>Are you sure you want to delete the restaurant "{{ object }}"?</p>
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        <button type="submit">Confirm Delete</button>
    </form>
</body>
</html>
```
### 5.4 Create tests
**restaurant/tests/tests.py:**
```python
from django.test import TestCase
from django.urls import reverse
from .factories import RestaurantFactory, IngredientFactory, DishFactory

class RestaurantViewsTest(TestCase):

    def test_restaurant_list_view(self):
        response = self.client.get(reverse('restaurant_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant_list.html')

    def test_restaurant_create_view(self):
        response = self.client.get(reverse('restaurant_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant_form.html')

        data = {'name': 'New Restaurant', 'address': '123 New Street', 'phone_number': '987-654-3210'}
        response = self.client.post(reverse('restaurant_create'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission
        self.assertTrue(Restaurant.objects.filter(name='New Restaurant').exists())

    def test_restaurant_update_view(self):
        restaurant = RestaurantFactory()
        response = self.client.get(reverse('restaurant_edit', args=[restaurant.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant_form.html')

        data = {'name': 'Updated Restaurant', 'address': '456 Updated Street', 'phone_number': '111-222-3333'}
        response = self.client.post(reverse('restaurant_edit', args=[restaurant.pk]), data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission
        self.assertEqual(Restaurant.objects.get(pk=restaurant.pk).name, 'Updated Restaurant')

    def test_restaurant_delete_view(self):
        restaurant = RestaurantFactory()
        response = self.client.get(reverse('restaurant_delete', args=[restaurant.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant_confirm_delete.html')

        response = self.client.post(reverse('restaurant_delete', args=[restaurant.pk]))
        self.assertEqual(response.status_code, 302)  # Redirect after successful deletion
        self.assertFalse(Restaurant.objects.filter(pk=restaurant.pk).exists())
```

Repeat a similar structure for Ingredient and Dish views and tests.

### Run the tests:

```bash
python manage.py test restaurant.tests
```
## 6. Implementing HTMX for Interactive Testing

Let's kick things up a notch and add HTMX to our project. HTMX is a library that allows you to add dynamic, AJAX-style behavior to your web pages with minimal JavaScript. To integrate HTMX for dynamic and interactive testing of restaurant-related features in our Django project, we will follow these general steps:

### 6.1. Install HTMX:
Install HTMX using a package manager, such as pip:

```bash
pip install django-htmx
```

### 6.2. Include HTMX in Your Template:
Include the HTMX library in the <head> section of your base HTML template. You can use the CDN or include the library locally.

```html
<!-- Include HTMX from CDN -->
<script src="https://unpkg.com/htmx.org@latest/dist/htmx.min.js"></script>
```

### 6.3. Update Your Views and Templates:
Modify your Django views and templates to use HTMX attributes for dynamic behavior. For example, you can use the hx-get attribute to load content dynamically.

```html
{% extends 'base.html' %}

{% block content %}
    <h1>Restaurant List</h1>
    
    <ul>
        {% for restaurant in restaurants %}
            <li>
                <span hx-get="{% url 'restaurant:restaurant_edit' pk=restaurant.pk %}" hx-trigger="click">Edit</span>
                <span hx-get="{% url 'restaurant:restaurant_delete' pk=restaurant.pk %}" hx-trigger="click">Delete</span>
                {{ restaurant.name }} - {{ restaurant.address }} - {{ restaurant.phone_number }}
            </li>
        {% endfor %}
    </ul>

    <div hx-target="#restaurant-form-container">
        <a hx-get="{% url 'restaurant:restaurant_create' %}" hx-trigger="click">Add a Restaurant</a>
    </div>

    <div id="restaurant-form-container"></div>
{% endblock %}
```

### 6.4. Update Your Views to Return Partial HTML:
In your Django views, you might need to modify them to return partial HTML when requested by HTMX.

```python

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



```
### 6.5. Create Partial Templates:

Create partial templates for the parts of the page you want to load dynamically. For example, you can create a restaurant_form_partial.html template.

**restaurant/templates/restaurant_form_partial.html**
```html
{% extends 'base.html' %}

{% block content%}
<form method="post" action="{% url 'restaurant:restaurant_edit' pk=restaurant.pk %}" hx-include="#restaurant-form-container">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
</form>
{% endblock %}
```

### 6.6. Add HTMX Attributes to Your Forms:
In your forms, you can add HTMX attributes for dynamic behavior.

**restaurant/restaurant_form.html**
```html
{% extends 'base.html' %}

{% block content %}
    <h1>{% if form.instance.pk %}Edit{% else %}Create{% endif %}A Restaurant</h1>
    {% if form.instance.pk %}<form method="post" action="{% url 'restaurant:restaurant_edit' pk=restaurant.pk %}" hx-include="#restaurant-form-container">
    {% else%}<form hx-post="{% url 'restaurant:restaurant_create' %}" hx-include="#restaurant-form-container">
    {% endif %}
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Save</button>
    </form>

{% endblock %}
```

### 7. Test Your Interactive Features:
Now, when you click on "Edit" or "Add a Restaurant," HTMX will dynamically load the form without a full page reload. Make sure to test these features interactively to ensure everything works as expected.


### 8. Finally
You made it! I hope your coffee is not yet cold.





