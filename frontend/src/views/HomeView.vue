<template>
  <div class="relative">
    <div class="relative">
      <img src="../assets/images/img.png" class="w-full" alt="home image" />
      <div class="absolute inset-0 flex flex-col items-center justify-center">
        <h1 class="lg:text-6xl md:text-4xl sm:text-2xl font-extrabold text-white font-mono">
          Discover a World of Culinary Inspiration
        </h1>
        <h3 class="lg:text-4xl md:text-2xl sm:text-2xl font-extrabold text-gray-100 mt-10 shadow-xl font-mono">
          Experience AI-Powered Recipe Recommendations
        </h3>
        <button class="lg:mt-4 md:mt-2 sm:mt-1 lg:px-6 md:px-4 sm:px-2 lg:py-3 md:py-2 sm:text-sm bg-orange-500 text-white font-semibold rounded hover:bg-orange-700">
          <router-link :to="'/ai/suggestions'">
            Explore
          </router-link>
        </button>
      </div>
    </div>
    <div class="px-4 text-center py-20">
      <h1 class="lg:text-4xl md:text-2xl sm:text-2xl font-bold font-mono">Explore Delicious Recipes</h1>
    </div>
    <div class="px-4 md:px-10"> <!-- Adjust padding for medium screens and above -->
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
        <RecipeCard
          v-for="recipe in recipes"
          :key="recipe.id"
          :recipe="recipe"
        />
      </div>
    </div>
  </div>
</template>

<script>
import RecipeCard from "../components/RecipeCard.vue"; // Adjust the path
import axios from "axios";
export default {
  components: {
    RecipeCard,
  },
  data() {
    return {
      recipes: [], // Fetched recipe data from the API
    };
  },
  mounted() {
    this.fetchRecipes();
  },
  methods: {
    async fetchRecipes() {
      try {
        // Fetch recipe data from API using Axios or fetch
        // Example using Axios:
        const response = await axios.get(
          "http://localhost:8000/api/all_recipes"
        );
        this.recipes = response.data;
      } catch (error) {
        console.error("Error fetching recipes:", error);
      }
    },
  },
};
</script>

<style>
/* Add Tailwind classes here if needed */
</style>
