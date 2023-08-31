from django.shortcuts import render
import openai
import os
from dotenv import load_dotenv
import re
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from .serializers import RecipeSerializer
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import Recipe
from typing import List, Dict


@api_view(['POST'])
def get_recipe_suggestions(request: Request):
    if request.method == 'POST':
        ingredients = request.data.get('ingredients_list', [])
        placeholder_ingredients = ', '.join([f'ingredient {i + 1}' for i in range(len(ingredients))])
        
        prompt = f"Generate 5 recipes suggestions based on ingredients {placeholder_ingredients}, and mention the quantity for each ingredient. e.g. 1 cup ingredient name 1, 1/2 cup ingredient name 2 etc. Generate at least 5 different types of recipes based on the ingredients given and give : (colon)after the heading of each recipe: {', '.join(ingredients)}"
        
        response = openai.Completion.create(
            engine="text-davinci-003",  
            prompt=prompt,
            max_tokens=1000, 
            temperature=1.2,  
        )
        
        suggestions = response.choices[0].text.strip()
          
        recipes = parse_suggestions(suggestions)
        
        return Response({'suggestions':suggestions,'recipes': recipes})

def parse_suggestions(suggestions):
    recipe_list = []
    suggestions = suggestions.strip().split('\n\n')
    
    for suggestion in suggestions:
        parts = suggestion.split(':')
        if len(parts) >= 2:
            heading = parts[0].strip()
            ingredients = parts[1].strip() if len(parts) > 1 else ""
            
            recipe = {
                "heading": heading,
                "ingredients": ingredients
            }
            
            recipe_list.append(recipe)
    
    response = {
        "recipes": recipe_list
    }
    
    return response


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_recipe(request):
    data = {
        'heading': request.data.get('heading'),
        'ingredients': request.data.get('ingredients'),
        'author': request.user.id,  # Use authenticated user as the author
        'image_url': request.data.get('image_url')
    }
    serializer = RecipeSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Recipe created successfully'}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_recipes(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_recipe(request, pk):  # Change parameter name to 'pk'
    try:
        recipe = Recipe.objects.get(id=pk)
    except Recipe.DoesNotExist:
        return Response({'message': 'Recipe not found'}, status=404)
    
    # Check if the logged-in user is the author of the recipe
    if request.user.id != recipe.author.id:
        return Response({'message': 'You do not have permission to update this recipe'}, status=403)
    
    serializer = RecipeSerializer(recipe, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Recipe updated successfully'})
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_recipe(request, pk):
    try:
        recipe = Recipe.objects.get(id=pk)
    except Recipe.DoesNotExist:
        return Response({'message': 'Recipe not found'}, status=404)
    
    # Check if the logged-in user is the author of the recipe
    if request.user.id != recipe.author.id:
        return Response({'message': 'You do not have permission to delete this recipe'}, status=403)
    
    recipe.delete()
    return Response({'message': 'Recipe deleted successfully'}, status=204)
