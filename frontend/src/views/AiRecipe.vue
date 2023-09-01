<template>
    <div class="flex items-center justify-center p-5">
      <div class="bg-white rounded-lg shadow-md p-4 space-y-4 w-1/2 border">
        <h1 class="text-4xl font-extrabold text-center text-[#34a0a4]">Unleash Culinary Creativity with AI</h1>
        <textarea
          v-model="ingredientsInput"
          class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-blue-400"
          placeholder="Enter ingredients E.g., Carrot, Onion"
        ></textarea>
        <div class="flex items-center justify-center">
          <button
            @click="searchRecipes"
            class="bg-[#34a0a4] text-white font-semibold px-4 py-2 rounded-md hover:bg-[#2e8487] focus:outline-none focus:ring focus:ring-blue-400"
            :disabled="isLoading"
          >
            <span v-if="isLoading">Loading...</span>
            <span v-else>Find Recipes!</span>
          </button>
        </div>
  
        <!-- Render the fetched recipes below the form -->
        <div v-if="recipes.length > 0" class="border p-5">
          <h2 class="text-lg font-semibold mb-5 text-[#168aad]">Matching Recipes:</h2>
          <ul class="list-disc pl-4">
            <li v-for="(recipe, index) in recipes" :key="index" class="mb-4 list-none">
              <h3 class="text-xl font-semibold">{{ recipe.heading }}</h3>
              <p class="text-gray-600">{{ recipe.ingredients }}</p>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        ingredientsInput: "",
        recipes: [],
        isLoading: false,
      };
    },
    methods: {
      async searchRecipes() {
        this.isLoading = true;
  
        const ingredientsList = this.ingredientsInput.split(",").map((ingredient) => ingredient.trim());
  
        try {
          const response = await fetch("http://localhost:8000/api/get_recipe/", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ ingredients_list: ingredientsList }),
          });
  
          if (response.ok) {
            const data = await response.json();
            this.recipes = data.recipes.recipes;
          } else {
            console.error("Error searching recipes:", response.statusText);
          }
        } catch (error) {
          console.error("Error searching recipes:", error);
        } finally {
          this.isLoading = false;
        }
      },
    },
  };
  </script>
  