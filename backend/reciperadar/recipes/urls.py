from django.urls import path
from . import views

urlpatterns = [
    path('api/get_recipe/', views.get_recipe_suggestions, name='get_recipe_suggestions'),
]