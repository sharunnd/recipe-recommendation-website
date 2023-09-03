
<template>
  <div>
    <!-- Check if recipe data is available -->
    <div v-if="recipe.image_url" class="bg-white shadow-lg rounded-lg px-40 py-10 mx-10 mt-10">
      <img
        v-if="recipe.image_url"
        :src="recipe.image_url"
        alt="Recipe Image"
        class="w-full h-80 object-cover mb-4"
      />
      <h2 class="text-xl font-semibold mb-2">{{ recipe.heading }}</h2>
      <p class="text-gray-600 mb-4">{{ recipe.ingredients }}</p>
      <div class="flex justify-around items-center mt-10">
        <router-link
          :to="'/recipe/edit/' + recipe.id"
          class="text-blue-600 hover:text-blue-800"
        >
          edit
        </router-link>
        <button @click="onDeleteRecipe" class="text-red-600 hover:text-red-800">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="w-6 h-6"
          >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0"
          />
          </svg>
        </button>
      </div>
    </div>

    <!-- If there's no recipe data, display a message -->
    <div v-else class="mt-4 flex items-center justify-center">
      <h1 class="text-red-500 text-2xl">Recipe has been deleted!</h1>
    </div>
  <AddReview :recipeId="recipe.id"/>
  <AddRating :recipeId="recipe.id"/>
  </div>
  
</template>
<script>
import { mapActions, mapGetters } from "vuex";
import { toast } from "vue3-toastify";
import AddReview from "../components/AddReview.vue";
import AddRating from "../components/AddRating.vue";
export default {
  components: {
    // Register your custom components here
    AddReview,
    AddRating,
  },
  computed: {
    ...mapGetters(["recipeDetails"]),
    recipe() {
      return this.recipeDetails || {};
    },
  },
  methods: {
    ...mapActions(["fetchRecipeDetails", "deleteRecipe"]),
    async fetchRecipeData() {
      const recipeId = this.$route.params.id;
      await this.fetchRecipeDetails(recipeId);
    },
    async onDeleteRecipe() {
      
      const recipeId = this.recipe.id;
      try {
        const response = await this.deleteRecipe(recipeId);
        if (response.status == 204) {
          toast.success("Recipe deleted successfully", {
            autoClose: 1000,
          });
          setTimeout(() => {
            this.$router.push("/");
          }, 2000);
        } else if (response.status === 403) {
          // this.errorMessage = "You do not have permission to delete this recipe";
          toast.error("You do not have permission to delete this recipe", {
            autoClose: 1000,
          });
        } else {
          console.log(response.statusText)
        }
      } catch (error) {
        if (error.response && error.response.status === 403) {
          // Handle 403 Forbidden error with a toast message
          toast.error("You do not have permission to delete this recipe", {
            autoClose: 2000,
          });
        } else {
          // Handle other errors
          toast.error("You do not have permission to delete this recipe", {
            autoClose: 2000,
          });
          console.error("Error deleting recipe:", error);
        }
      }
    },
  },
  mounted() {
    this.fetchRecipeData();
  },
};
</script>

<style scoped>
/* Your styling here */
</style>
