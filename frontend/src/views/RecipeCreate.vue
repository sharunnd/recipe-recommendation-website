<template>
  <div class="flex items-center justify-center border min-h-screen">
    <div class="recipe-create p-4 bg-white rounded-lg shadow-md w-1/3">
      <h1 class="text-2xl font-semibold mb-4 text-center">Create New Recipe</h1>
      <form @submit.prevent="submitRecipe">
        <div class="mb-4">
          <label for="heading" class="block text-sm font-medium text-gray-600"
            >Heading:</label
          >
          <input
            v-model="recipe.heading"
            type="text"
            id="heading"
            required
            class="w-full px-4 py-2 rounded-md border border-gray-300 focus:outline-none focus:ring-opacity-50 focus:ring-1 focus:ring-[#10A37F]"
          />
        </div>

        <div class="mb-4">
          <label
            for="ingredients"
            class="block text-sm font-medium text-gray-600"
            >Ingredients:</label
          >
          <textarea
            v-model="recipe.ingredients"
            id="ingredients"
            required
            class="w-full px-4 py-2 rounded-md border border-gray-300 focus:outline-none focus:ring-opacity-50 focus:ring-1 focus:ring-[#10A37F]"
          ></textarea>
        </div>

        <div class="mb-4">
          <label for="image_url" class="block text-sm font-medium text-gray-600"
            >Image URL:</label
          >
          <input
            v-model="recipe.image_url"
            type="text"
            id="image_url"
            class="w-full px-4 py-2 rounded-md border border-gray-300 focus:outline-none focus:ring-opacity-50 focus:ring-1 focus:ring-[#10A37F]"
          />
        </div>

        <div class="flex items-center justify-center">
          <button
            type="submit"
            class="bg-[#10A37F] text-white font-semibold px-4 py-2 rounded-md hover:bg-[#3fb799]"
          >
            Create Recipe
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { toast } from "vue3-toastify";
export default {
  data() {
    return {
      recipe: {
        heading: "",
        ingredients: "",
        image_url: "",
      },
    };
  },
  methods: {
    async submitRecipe() {
      try {
        const response = await fetch("http://localhost:8000/api/create/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${localStorage.getItem("token")}`,
          },
          body: JSON.stringify(this.recipe),
        });
        const responseData = await response.json();

        toast.success(responseData.message, {
          autoClose: 1000,
        });

        if (response.ok) {
          setTimeout(() => {
            this.$router.push("/");
          }, 2000); // Redirect to home page after successful creation
        } else {
          console.error("Failed to create recipe");
        }
      } catch (error) {
        toast.success("Something went wrong", {
          autoClose: 1000,
        });
        console.error("Error creating recipe:", error);
      }
    },
  },
};
</script>
