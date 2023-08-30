from django.shortcuts import render
import openai
import os
from dotenv import load_dotenv
import re
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request
from typing import List, Dict
# @api_view(['POST'])
# def get_recipe_suggestions(request: Request):
#     if request.method == 'POST':
#         ingredients = request.data.get('ingredients_list', [])
#         placeholder_ingredients = ', '.join([f'ingredient {i + 1}' for i in range(len(ingredients))])

#         prompt = f"Generate 5 recipes suggestions based on ingredients {placeholder_ingredients}, and mention the quantity for each ingredient. e.g. 1 cup ingredient name 1, 1/2 cup ingredient name 2 etc. Generate at least 5 different types of recipes based on the ingredients given: {', '.join(ingredients)}"
        
#         response = openai.Completion.create(
#             engine="text-davinci-003",  
#             prompt=prompt,
#             max_tokens=500, 
#             temperature=1.2,  
#         )
        
#         suggestions = response.choices[0].text.strip()
        
#         return Response({'suggestions': suggestions})


@api_view(['POST'])
def get_recipe_suggestions(request: Request):
    if request.method == 'POST':
        ingredients = request.data.get('ingredients_list', [])
        placeholder_ingredients = ', '.join([f'ingredient {i + 1}' for i in range(len(ingredients))])
        
        prompt = f"Generate 5 recipes suggestions based on ingredients {placeholder_ingredients}, and mention the quantity for each ingredient. e.g. 1 cup ingredient name 1, 1/2 cup ingredient name 2 etc. Generate at least 5 different types of recipes based on the ingredients given: {', '.join(ingredients)}"
        
        response = openai.Completion.create(
            engine="text-davinci-003",  
            prompt=prompt,
            max_tokens=1000, 
            temperature=1.2,  
        )
        
        suggestions = response.choices[0].text.strip()
        # print("Suggestions:", suggestions) 
        # suggestions = "1. Carrot Onion Soup: 3 cups chopped carrots, 1 cup chopped onion, a tablespoons of vegetable oil, 1/4 cup heavy cream, 1/4 teaspoon nutmeg, 2 sprigs of thyme, 2 cups of chicken broth1. \n\n2. Curried Carrot & Onion Salad: 1 cup shredded carrots, ½ cup chopped onion, 2 tablespoons currants, ¼ cup diced yellow pepper, ¼ cup light mayonnaise, 1 teaspoon curry powder, ¼ teaspoon salt. \n\n3. Carrot and Onion Frittata: 6 eggs, 2 tablespoons of extra virgin olive oil, 2 cups diced onion, 2 cups shredded carrots, 1/2 teaspoon smoked paprika, 1/2 teaspoon ground black pepper, a pinch of sea salt, 1/2 cup grated cheese.\n\n4. Caramelized Onion & Carrot Pizza: 2 tablespoons olive oil, 1 cup chopped onion, 2 cloves of garlic minced, 1 ½ cups sliced carrots , 1 tablespoon of fresh thyme leaves, 1 teaspoon dark brown sugar, 1 premade pizza crust and 1 ½ cups grated cheese. \n\n5. Carrot Onion Curry: 1 tablespoon vegetable oil, 1/2 cup peeled and diced onion,1 tablespoon curry powder, 1/4 teaspoon chili powder, 1 teaspoon ginger garlic paste, 1 medium-size peeled and sliced carrot, 2 cups water, All purpose seasoning."
        print("Suggestions:", suggestions) 
          
        recipes = parse_suggestions(suggestions)
        
        return Response({'recipes': recipes})

def parse_suggestions(suggestions):
    recipe_list = []
    suggestions = suggestions.strip().split('\n\n')
    
    for suggestion in suggestions:
        parts = suggestion.split('. ')
        if len(parts) >= 2:
            heading = parts[1].split(': ', 1)[0].strip()
            ingredients = ". ".join(parts[1].split(': ', 1)[1:]).strip()
            
            recipe = {
                "heading": heading,
                "ingredients": ingredients
            }
            
            recipe_list.append(recipe)
    
    response = {
        "recipes": recipe_list
    }
    
    return response
