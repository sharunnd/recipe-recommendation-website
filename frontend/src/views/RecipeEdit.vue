<template>
  <div class="flex items-center justify-center min-h-screen">
   <div class="w-full lg:w-1/2 md:w-250 sm:w-full md:px-10 sm:px-10">
    <form @submit.prevent="onUpdateRecipe" class="w-full">
      <div class="mb-4 ">
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

      <div class="flex items-center justify-between">
        <button type="submit" class="bg-[#10A37F] hover:bg-[#3ca48a] text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
          Update Recipe
        </button>
      </div>
    </form>
   </div>
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
      },
    };
  },
  created() {
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
      };
    },
    async onUpdateRecipe() {
      const recipeId = this.recipe.id;
      const updatedRecipeData = this.updatedRecipeData; // Get the updated data
      try {
        const response = await this.updateRecipe({ recipeId, updatedRecipeData });
        if (response.ok) {
          toast.success("Recipe updated successfully", {
            autoClose: 1000,
          });
        } else {
          toast.error("Something went wrong!", {
            autoClose: 1000,
          });
          console.error("Error updating recipe:", response.statusText);
        }
      } catch (error) {
        toast.error("You are not allowed to do this action!", {
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
