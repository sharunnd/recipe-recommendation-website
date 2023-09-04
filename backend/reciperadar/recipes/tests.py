
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from recipes.models import Recipe,Review,Rating # Import your Recipe model
from recipes.serializers import RecipeSerializer,ReviewSerializer,RatingSerializer    # Import your Recipe serializer
from django.urls import reverse
from django.db.models import Avg
class CreateRecipeViewTests(TestCase):
    def setUp(self):
        # Create a test user and authenticate them
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

        # Create an authenticated client with the token
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_create_recipe(self):
        # Prepare a sample recipe data
        data = {
            'heading': 'Test Recipe',
            'ingredients': 'Ingredient 1, Ingredient 2',
            'image_url': 'https://example.com/test-image.jpg',
        }

        # Send a POST request to create the recipe
        response = self.client.post('/api/create/', data, format='json')

        # Check if the response status code is 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the response contains 'message'
        self.assertTrue('message' in response.data)

        # Check if the 'message' in the response is 'Recipe created successfully'
        self.assertEqual(response.data['message'], 'Recipe created successfully')

        # You can add more specific checks if needed, such as checking if the recipe was actually created in the database.

        # Print the response for debugging (optional)
        print(response.data)

class RecipeViewsTests(TestCase):
    def setUp(self):
        # Create a test user and authenticate them
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

        # Create an authenticated client with the token
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_get_all_recipes(self):
        # Create some sample recipes in the database
        recipe1 = Recipe.objects.create(author=self.user, heading='Recipe 1', ingredients='Ingredient 1, Ingredient 2')
        recipe2 = Recipe.objects.create(author=self.user, heading='Recipe 2', ingredients='Ingredient 3, Ingredient 4')

        # Send a GET request to retrieve all recipes
        url = reverse('get-all-recipes')  # Use reverse to generate the URL
        response = self.client.get(url)

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response data matches the serialized data of the created recipes
        expected_data = RecipeSerializer([recipe1, recipe2], many=True).data
        self.assertEqual(response.data, expected_data)

    def test_update_recipe(self):
        # Create a sample recipe in the database
        recipe = Recipe.objects.create(author=self.user, heading='Recipe 1', ingredients='Ingredient 1, Ingredient 2')

        # Prepare updated data for the recipe
        updated_data = {
            'heading': 'Updated Recipe',
            'ingredients': 'Updated Ingredient 1, Updated Ingredient 2',
            'image_url': 'https://example.com/updated-image.jpg',
        }

        # Send a PATCH request to update the recipe
        url = reverse('update-recipe', kwargs={'pk': recipe.id})  # Generate the URL
        response = self.client.patch(url, updated_data, format='json')

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response contains 'message'
        self.assertTrue('message' in response.data)

        # Check if the 'message' in the response is 'Recipe updated successfully'
        self.assertEqual(response.data['message'], 'Recipe updated successfully')

        # Refresh the recipe from the database to get the latest data
        recipe.refresh_from_db()

        # Check if the recipe data matches the updated data
        self.assertEqual(recipe.heading, updated_data['heading'])
        self.assertEqual(recipe.ingredients, updated_data['ingredients'])
        self.assertEqual(recipe.image_url, updated_data['image_url'])

        # You can add more specific checks if needed.

        # Print the response for debugging (optional)
        print(response.data)


class RecipeViewsTests(TestCase):
    def setUp(self):
        # Create a test user and authenticate them
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

        # Create an authenticated client with the token
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    # ... Other test methods ...

    def test_delete_recipe(self):
        # Create a sample recipe in the database
        recipe = Recipe.objects.create(author=self.user, heading='Recipe 1', ingredients='Ingredient 1, Ingredient 2')

        # Send a DELETE request to delete the recipe
        url = reverse('delete-recipe', kwargs={'pk': recipe.id})  # Generate the URL
        response = self.client.delete(url)

        # Check if the response status code is 204 No Content
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Attempt to retrieve the deleted recipe from the database
        with self.assertRaises(Recipe.DoesNotExist):
            Recipe.objects.get(pk=recipe.id)

        # You can add more specific checks if needed.

        # Print the response for debugging (optional)
        print(response.data)


class RecipeViewsTests(TestCase):
    def setUp(self):
        # Create a test user (if needed) and authenticate them
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

        # Create an authenticated client with the token
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    # ... Other test methods ...

    def test_get_recipe_by_id(self):
        # Create a sample recipe in the database
        recipe = Recipe.objects.create(author=self.user, heading='Recipe 1', ingredients='Ingredient 1, Ingredient 2')

        # Send a GET request to retrieve the recipe by its ID
        url = reverse('get-recipe-by-id', kwargs={'recipe_id': recipe.id})  # Generate the URL
        response = self.client.get(url)

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response data matches the serialized data of the created recipe
        expected_data = RecipeSerializer(recipe).data
        self.assertEqual(response.data, expected_data)

        # Print the response for debugging (optional)
        print(response.data)


class RecipeViewsTests(TestCase):
    def setUp(self):
        # Create a test user (if needed) and authenticate them
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

        # Create an authenticated client with the token
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    # ... Other test methods ...

    def test_create_review(self):
        # Create a sample recipe in the database
        recipe = Recipe.objects.create(author=self.user, heading='Recipe 1', ingredients='Ingredient 1, Ingredient 2')

        # Data for the review
        review_data = {
            'comment': 'This is a great recipe!',
            'rating': '4.5',  # Use an appropriate rating value
            'user_name': 'JohnDoe',  # User's name
        }

        # Send a POST request to create a review for the recipe
        url = reverse('create_review', kwargs={'recipe_id': recipe.id})  # Generate the URL
        response = self.client.post(url, review_data, format='json')

        # Check if the response status code is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the response contains 'message'
        self.assertTrue('message' in response.data)

        # Check if the 'message' in the response is 'Review created successfully'
        self.assertEqual(response.data['message'], 'Review created successfully')

        # Refresh the recipe from the database to get the latest data
        recipe.refresh_from_db()

        # Check if a review with the provided comment and user name exists for the recipe
        review = Review.objects.filter(recipe=recipe, comment=review_data['comment'], user_name=review_data['user_name']).first()
        self.assertIsNotNone(review)

        # You can add more specific checks if needed.

        # Print the response for debugging (optional)
        print(response.data)

class RecipeViewsTests(TestCase):
    def setUp(self):
        # Create a test user (if needed) and authenticate them
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

        # Create an authenticated client with the token
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    # ... Other test methods ...

    def test_create_rating(self):
        # Create a sample recipe in the database
        recipe = Recipe.objects.create(author=self.user, heading='Recipe 1', ingredients='Ingredient 1, Ingredient 2')

        # Data for the rating
        rating_data = {
            'rating': '4.5',  # Use an appropriate rating value
        }

        # Send a POST request to create a rating for the recipe
        url = reverse('create_rating', kwargs={'recipe_id': recipe.id})  # Generate the URL
        response = self.client.post(url, rating_data, format='json')

        # Check if the response status code is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the response contains 'message'
        self.assertTrue('message' in response.data)

        # Check if the 'message' in the response is 'Rating added successfully'
        self.assertEqual(response.data['message'], 'Rating added successfully')

        # Refresh the recipe from the database to get the latest data
        recipe.refresh_from_db()

        # Check if a rating with the provided value exists for the recipe
        rating = Rating.objects.filter(recipe=recipe, rating=rating_data['rating']).first()
        self.assertIsNotNone(rating)

        # Check if the average rating for the recipe has been updated
        recipe_rating = Rating.objects.filter(recipe=recipe).aggregate(Avg('rating'))
        self.assertEqual(recipe.average_rating, recipe_rating['rating__avg'])

        # You can add more specific checks if needed.

        # Print the response for debugging (optional)
        print(response.data)



class RecipeViewsTests(TestCase):
    def setUp(self):
        # Create a test user (if needed) and authenticate them
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

        # Create an authenticated client with the token
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    # ... Other test methods ...

    def test_get_reviews(self):
        # Create a sample recipe in the database
        recipe = Recipe.objects.create(author=self.user, heading='Recipe 1', ingredients='Ingredient 1, Ingredient 2')

        # Create some sample reviews for the recipe
        review1 = Review.objects.create(user=self.user, recipe=recipe, comment='Review 1')
        review2 = Review.objects.create(user=self.user, recipe=recipe, comment='Review 2')

        # Send a GET request to retrieve reviews for the recipe
        url = reverse('get_reviews', kwargs={'recipe_id': recipe.id})  # Generate the URL
        response = self.client.get(url)

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response contains 'message'
        self.assertTrue('message' in response.data)

        # Check if the 'message' in the response is 'Reviews retrieved successfully'
        self.assertEqual(response.data['message'], 'Reviews retrieved successfully')

        # Check if the response data matches the serialized data of the created reviews
        expected_data = ReviewSerializer([review1, review2], many=True).data
        self.assertEqual(response.data['reviews'], expected_data)

    def test_get_ratings(self):
        # Create a sample recipe in the database
        recipe = Recipe.objects.create(author=self.user, heading='Recipe 1', ingredients='Ingredient 1, Ingredient 2')

        # Create some sample ratings for the recipe
        rating1 = Rating.objects.create(user=self.user, recipe=recipe, rating='4.5')
        rating2 = Rating.objects.create(user=self.user, recipe=recipe, rating='5.0')

        # Send a GET request to retrieve ratings for the recipe
        url = reverse('get_ratings', kwargs={'recipe_id': recipe.id})  # Generate the URL
        response = self.client.get(url)

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response contains 'message'
        self.assertTrue('message' in response.data)

        # Check if the 'message' in the response is 'Ratings retrieved successfully'
        self.assertEqual(response.data['message'], 'Ratings retrieved successfully')

        # Check if the response data matches the serialized data of the created ratings
        expected_data = RatingSerializer([rating1, rating2], many=True).data
        self.assertEqual(response.data['ratings'], expected_data)

        # You can add more specific checks if needed.

        # Print the response for debugging (optional)
        print(response.data)