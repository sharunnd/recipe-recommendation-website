<template>
  <div class="relative">
    <div class="relative">
      <img src="../assets/images/img.png" class="w-full" alt="home image" />
      <div class="absolute inset-0 flex flex-col items-center justify-center">
        <h1 class="text-6xl font-extrabold text-white font-mono">
          Discover a World of Culinary Inspiration
        </h1>
        <h3
          class="text-4xl font-extrabold text-gray-100 mt-10 shadow-xl font-mono"
        >
          Experience AI-Powered Recipe Recommendations
        </h3>
        <button
          class="mt-4 px-6 py-3 bg-orange-500 text-white font-semibold rounded hover:bg-orange-700"
        ><router-link
        :to="'/ai/suggestions'"
        >
        Explore
      </router-link></button>
      </div>
    </div>
    <div class="px-4 text-center py-20">
      <h1 class="text-4xl font-bold font-mono">Explore Delicious Recipes</h1>
    </div>
    <div class="px-10">
      <div
        class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4"
      >
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
