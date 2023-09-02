from django.urls import path
from . import views

urlpatterns = [
    path('api/get_recipe/', views.get_recipe_suggestions, name='get_recipe_suggestions'),
    path('api/create/', views.create_recipe, name='create-recipe'),
    path('api/all_recipes', views.get_all_recipes, name='get-all-recipes'),
    path('api/update_recipe/<int:pk>/', views.update_recipe, name='update-recipe'),
    path('api/delete_recipe/<int:pk>/', views.delete_recipe, name='delete-recipe'),
    path('api/recipe/<int:recipe_id>/', views.get_recipe_by_id, name='get-recipe-by-id'),
    # review and rating
    path('api/recipe/reviews/<int:recipe_id>/', views.create_review, name='create_review'),
    path('api/recipe/get/reviews/<int:recipe_id>/', views.get_reviews, name='get_reviews'),
    path('api/recipe/rate/<int:recipe_id>/', views.create_rating, name='create_rating'),
    path('api/recipe/get/ratings/<int:recipe_id>/', views.get_ratings, name='get_ratings'),
]
