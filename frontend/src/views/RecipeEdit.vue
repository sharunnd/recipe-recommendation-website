<template>
  <div>
    <!-- Display form for editing recipe data -->
    <form @submit.prevent="onUpdateRecipe">
      <div class="mb-4">
        <label for="title" class="block text-gray-700 font-bold mb-2">Title</label>
        <input
          type="text"
          id="title"
          v-model="updatedRecipeData.heading"
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          required
        />
      </div>
      <div class="mb-4">
        <label for="description" class="block text-gray-700 font-bold mb-2">Description</label>
        <textarea
          id="description"
          v-model="updatedRecipeData.ingredients"
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          rows="4"
          required
        ></textarea>
      </div>
      <!-- Add other form fields for updating recipe properties -->

      <div class="flex items-center justify-between">
        <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
          Update Recipe
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import { toast } from "vue3-toastify";

export default {
  data() {
    return {
      updatedRecipeData: {
        heading: "", // Initialize with empty values
        ingredients: "",
        // Add other properties here
      },
    };
  },
  created() {
    // Fetch the initial recipe data when the component is created
    this.fetchRecipeData();
  },
  computed: {
    ...mapGetters(["recipeDetails"]),
    recipe() {
      return this.recipeDetails || {};
    },
  },
  methods: {
    ...mapActions(["fetchRecipeDetails", "updateRecipe"]),
    async fetchRecipeData() {
      const recipeId = this.$route.params.id;
      await this.fetchRecipeDetails(recipeId);

      // Populate updatedRecipeData with the fetched data
      this.updatedRecipeData = {
        heading: this.recipe.heading || "",
        ingredients: this.recipe.ingredients || "",
        // Add other properties here
      };
    },
    async onUpdateRecipe() {
      const recipeId = this.recipe.id;
      const obj = this.updatedRecipeData
      try {
        // Call the updateRecipe action with updated data
        console.log(recipeId,obj);
        await this.updateRecipe(recipeId, this.updatedRecipeData);
        console.log("after",recipeId,obj);
        toast.success("Recipe updated successfully", {
          autoClose: 1000,
        });
        this.$router.push(`/recipe/${recipeId}`);
      } catch (error) {
        toast.error("Something went wrong!", {
          autoClose: 1000,
        });
        console.error("Error updating recipe:", error);
      }
    },
  },
};
</script>

<style scoped>
/* Your styling here */
</style>
