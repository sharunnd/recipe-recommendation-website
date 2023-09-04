<template>
  <div>
    <!-- Check if recipe data is available -->
    <div
      v-if="recipe.image_url"
      class="bg-white shadow-lg rounded-lg px-40 py-10 mx-10 mt-10"
    >
      <img
        v-if="recipe.image_url"
        :src="recipe.image_url"
        alt="Recipe Image"
        class="w-full h-80 object-cover mb-4"
      />
      <h2 class="text-xl font-semibold mb-2">{{ recipe.heading }}</h2>
      <div class="flex">
        <h3 class="mr-1">Rating: {{ recipe.average_rating }}</h3>
        <div>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="gold"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            class="w-6 h-6"
            style="stroke: gold"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.040.701.663.321.988l-4.204 3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.563.563 0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-4.204-3.602a.563.563 0 01.321-.988l5.518-.442a.563.563 0 00.475-.345L11.48 3.5z"
            />
          </svg>
        </div>
      </div>

      <p class="text-gray-600 mb-4">{{ recipe.ingredients }}</p>

      <div class="flex justify-around items-center mt-10">
        <div>
          <AddRating :recipeId="recipe.id" />
        </div>
        <router-link
          :to="'/recipe/edit/' + recipe.id"
          class="text-blue-600 hover:text-blue-800"
        >
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
              d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L10.582 16.07a4.5 4.5 0 01-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 011.13-1.897l8.932-8.931zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0115.75 21H5.25A2.25 2.25 0 013 18.75V8.25A2.25 2.25 0 015.25 6H10"
            />
          </svg>
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
      <AddReview :recipeId="recipe.id" />
      <div class="mt-10">
        <ReviewList :reviews="recipeComments.reviews" />
      </div>
    </div>

    <!-- If there's no recipe data, display a message -->
    <div v-else class="mt-4 flex items-center justify-center">
      <h1 class="text-red-500 text-2xl">Recipe has been deleted!</h1>
    </div>
  </div>
</template>
<script>
import { mapActions, mapGetters } from "vuex";
import { toast } from "vue3-toastify";
import AddReview from "../components/AddReview.vue";
import AddRating from "../components/AddRating.vue";
import ReviewList from "../components/ReviewList.vue";
export default {
  components: {
    // Register your custom components here
    AddReview,
    AddRating,
    ReviewList,
  },
  computed: {
    ...mapGetters(["recipeDetails", "recipeComments"]),
    recipe() {
      return this.recipeDetails || {};
    },
  },
  methods: {
    ...mapActions([
      "fetchRecipeDetails",
      "deleteRecipe",
      "fetchRecipeComments",
    ]),
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
          console.log(response.statusText);
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
  async mounted() {
    const recipeId = this.$route.params.id;
    await this.fetchRecipeData();
    await this.fetchRecipeComments(recipeId); // Use the correct action name
  },
};
</script>

<style scoped>
/* Your styling here */
</style>
