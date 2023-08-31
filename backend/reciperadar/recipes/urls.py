from django.urls import path
from . import views

urlpatterns = [
    path('api/get_recipe/', views.get_recipe_suggestions, name='get_recipe_suggestions'),
    path('api/create/', views.create_recipe, name='create-recipe'),
    path('api/all_reipes', views.get_all_recipes, name='get-all-recipes'),
]